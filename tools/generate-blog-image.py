#!/usr/bin/env python3
"""Generate featured images for blog posts using AWS Bedrock."""

import argparse
import base64
import io
import json
import sys
import textwrap
from pathlib import Path

try:
    import boto3
except ImportError:
    print("Error: boto3 is required. Install with: pip install boto3", file=sys.stderr)
    sys.exit(1)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    Image = None

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "static" / "images"

MODELS = {
    "titan": {
        "id": "amazon.titan-image-generator-v2:0",
        "region": "us-east-1",
    },
    "sd3-large": {
        "id": "stability.sd3-5-large-v1:0",
        "region": "us-west-2",
    },
}

# Titan valid dimensions (width x height) mapped from aspect ratios.
# Titan requires specific pixel pairs; these are the largest valid sizes for each ratio.
TITAN_ASPECT_RATIOS = {
    "1:1": (1024, 1024),
    "16:9": (1408, 768),
    "9:16": (768, 1408),
    "3:2": (1152, 768),
    "2:3": (768, 1152),
    "4:3": (1408, 1024),
    "3:4": (1024, 1408),
}


def build_titan_body(args, width, height):
    body = {
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {"text": args.prompt},
        "imageGenerationConfig": {
            "width": width,
            "height": height,
            "numberOfImages": 1,
        },
    }
    if args.negative_prompt:
        body["textToImageParams"]["negativeText"] = args.negative_prompt
    if args.seed is not None:
        body["imageGenerationConfig"]["seed"] = args.seed
    return body


def parse_titan_response(response_body):
    return base64.b64decode(response_body["images"][0]), None


def build_stability_body(args):
    body = {
        "prompt": args.prompt,
        "aspect_ratio": args.aspect_ratio,
        "output_format": "png",
    }
    if args.negative_prompt:
        body["negative_prompt"] = args.negative_prompt
    if args.seed is not None:
        body["seed"] = args.seed
    return body


def parse_stability_response(response_body):
    image_data = base64.b64decode(response_body["images"][0])
    seed = response_body.get("seeds", [None])[0]
    return image_data, seed


FONT_SEARCH_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "C:/Windows/Fonts/arialbd.ttf",
]


def overlay_title(image_data, title):
    """Render title text on top of the generated image using Pillow."""
    if Image is None:
        print(
            "Warning: Pillow not installed, skipping title overlay. "
            "Install with: pip install Pillow",
            file=sys.stderr,
        )
        return image_data

    img = Image.open(io.BytesIO(image_data)).convert("RGBA")
    draw = ImageDraw.Draw(img)
    img_w, img_h = img.size

    # Find a font
    font_path = None
    for p in FONT_SEARCH_PATHS:
        if Path(p).exists():
            font_path = p
            break

    # Size the font to fit ~90% of image width with word wrapping
    margin = int(img_w * 0.05)
    max_text_width = img_w - 2 * margin
    font_size = int(img_h * 0.08)

    # Binary search for the best font size and wrap combo
    while font_size > 16:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default(font_size)

        # Estimate chars per line from font metrics, then wrap
        avg_char_w = font.getlength("A")
        chars_per_line = max(10, int(max_text_width / avg_char_w))
        wrapped = textwrap.fill(title, width=chars_per_line)
        bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        if text_w <= max_text_width and text_h <= img_h * 0.4:
            break
        font_size -= 2

    # Position: top-left with padding
    x = margin
    y = margin

    # Draw shadow/outline for readability
    shadow_offset = max(2, font_size // 20)
    draw.multiline_text(
        (x + shadow_offset, y + shadow_offset),
        wrapped,
        font=font,
        fill=(0, 0, 0, 200),
    )
    draw.multiline_text((x, y), wrapped, font=font, fill=(255, 255, 255, 255))

    # Convert back to PNG bytes
    out = io.BytesIO()
    img.convert("RGB").save(out, format="PNG")
    return out.getvalue()


def main():
    parser = argparse.ArgumentParser(
        description="Generate featured images for blog posts using AWS Bedrock."
    )
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument(
        "--title",
        help='Blog title to render as text on the image (e.g. "Why I Switched to Claude")',
    )
    parser.add_argument(
        "--output", required=True, help="Output filename (e.g. my-post.png)"
    )
    parser.add_argument(
        "--model",
        choices=list(MODELS.keys()),
        default="titan",
        help="Model to use (default: titan)",
    )
    parser.add_argument(
        "--aspect-ratio",
        default="3:2",
        help="Aspect ratio (default: 3:2). Titan maps to closest valid pixel dimensions.",
    )
    parser.add_argument("--negative-prompt", help="What to avoid in the image")
    parser.add_argument("--seed", type=int, help="Seed for reproducibility")
    parser.add_argument(
        "--region",
        help="AWS region override (default: auto-selected per model)",
    )

    args = parser.parse_args()

    model_info = MODELS[args.model]
    model_id = model_info["id"]
    region = args.region or model_info["region"]

    output_path = OUTPUT_DIR / args.output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    is_titan = args.model == "titan"

    if is_titan:
        dims = TITAN_ASPECT_RATIOS.get(args.aspect_ratio)
        if not dims:
            valid = ", ".join(sorted(TITAN_ASPECT_RATIOS.keys()))
            print(
                f"Error: Unsupported aspect ratio '{args.aspect_ratio}' for Titan. "
                f"Valid ratios: {valid}",
                file=sys.stderr,
            )
            sys.exit(1)
        width, height = dims
        body = build_titan_body(args, width, height)
        print(f"Model:  {args.model} ({model_id})")
        print(f"Size:   {width}x{height} (from {args.aspect_ratio})")
    else:
        body = build_stability_body(args)
        print(f"Model:  {args.model} ({model_id})")
        print(f"Aspect: {args.aspect_ratio}")

    print(f"Region: {region}")
    if args.title:
        print(f"Title:  {args.title}")
    print(f"Prompt: {args.prompt}")
    if args.negative_prompt:
        print(f"Neg:    {args.negative_prompt}")
    if args.seed is not None:
        print(f"Seed:   {args.seed}")
    print()

    client = boto3.client("bedrock-runtime", region_name=region)

    print("Generating image...", flush=True)
    try:
        response = client.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body),
        )
    except client.exceptions.ClientError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    response_body = json.loads(response["body"].read())

    if is_titan:
        image_data, seed = parse_titan_response(response_body)
    else:
        image_data, seed = parse_stability_response(response_body)

    if args.title:
        print("Overlaying title text...", flush=True)
        image_data = overlay_title(image_data, args.title)

    output_path.write_bytes(image_data)
    print(f"Saved:  {output_path}")
    if seed is not None:
        print(f"Seed:   {seed}")

    relative_path = f"/images/{args.output}"
    print(f'\nFrontmatter:\n  image: "{relative_path}"')


if __name__ == "__main__":
    main()
