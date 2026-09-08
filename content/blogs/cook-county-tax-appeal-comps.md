---
title: "How to Appeal Your Cook County Property Taxes (Without Paying a Lawyer Half Your Savings)"
date: 2026-09-07T00:00:00Z
tags: ["Cook County", "Property Taxes", "Open Data", "Python", "Automation"]
description: "Cook County reassesses your home, your tax bill jumps, and a lawyer offers to appeal it for half of whatever they save you. Here's how to do it yourself in an afternoon, and a tool that does most of the work for you."
image: "/images/cook-county-tax-appeal.svg"
---

Every three years, Cook County reassesses your property, and every three years a wave of postcards shows up in your mailbox from law firms offering to appeal your new assessment for you. The pitch is always the same: no upfront cost, they only get paid if they win, and if they win they keep 33-50% of your **first year's** tax savings. Sounds fair, but "no upfront cost" doesn't mean cheap: 33-50% of a year's savings is still real money -- often hundreds of dollars -- for work you can do yourself for free in an afternoon.

Here's the thing: the entire process a lawyer runs on your behalf is public. The Assessor's office publishes the same comparable-sales and assessment data they'd pull, the online appeal filer is open to any property owner, and the argument that wins the vast majority of Cook County residential appeals -- **lack of uniformity** -- is just a spreadsheet exercise. You're not proving your house is worth less money. You're proving the county assessed it higher per square foot than similar houses nearby.

## The manual process

If you wanted to do this yourself with no tools beyond a browser, here's what it takes:

1. **Find your PIN.** Your Property Index Number is on your tax bill or reassessment notice, or searchable by address at the [Assessor's website](https://www.cookcountyassessor.com/).
2. **Look up your own property record** in the Assessor's CookViewer tool -- your property class, township, neighborhood code, building square footage, land square footage, age, construction type, and current assessed value.
3. **Run CookViewer's "Comparable Properties" tool**, which searches for other parcels in the same class, township, and neighborhood code, within about half a mile, within 10% of your building and land square footage, within 15 years of your building's age, and of the same construction type. This is the county's own definition of "comparable" -- use it, because it's the same definition the Board of Review will apply when they review your appeal.
4. **Export the results to CSV** and start working through them by hand: calculate assessed value per square foot for every comp, and sort out which ones are actually assessed lower than your property.
5. **Strengthen your case.** A comp is much harder for the Board of Review to dismiss if you can also show it recently sold for less than its assessment implies, or if it was already reduced on a prior appeal -- meaning the county has already agreed, in writing, that that specific property was over-assessed. That means separately searching the Assessor's Parcel Sales open dataset and the Board of Review's Appeal Decision History dataset for every comp you're considering, and cross-referencing by PIN.
6. **Pick your strongest 3-6 comps.** More isn't better here -- a handful of tight, well-evidenced comps beats a long list of loosely similar ones.
7. **Write your narrative.** Cook County's appeal filer wants a Desired Market Value, a reason for appeal, and a short explanation -- capped at 40 characters -- justifying it, plus a longer narrative attachment tying each comp back to your property.
8. **Track down a photo of your property and each comp** for the narrative PDF, since the filer expects supporting exhibits, not just a table of numbers.
9. **File it all** at [propertytaxfilings.cookcountyil.gov](https://propertytaxfilings.cookcountyil.gov/), a multi-tab form where you re-search for each comp's PIN, check it, and attach your narrative and PIN list.

None of this is conceptually hard. It's just tedious, and it's exactly the tedium a law firm is charging you for.

## Enter the repo

I got tired of doing this by hand every reassessment cycle, so I wrote [`cook-county-tax-appeal-comps`](https://github.com/mattjonesorg/cook-county-tax-appeal-comps), a small Python tool that pulls straight from Cook County's own ArcGIS and open-data APIs and does steps 2 through 8 for you.

```
python3 comps.py 16-07-204-019-0000
```

Give it a PIN, and it:

- Looks up your property's own characteristics and exact parcel geometry.
- Searches for comps using CookViewer's own default criteria, so the results line up with what the Board of Review will see.
- Cross-references every comp against Cook County's Parcel Sales and Board of Review Appeal Decision History datasets, flagging the ones with the strongest evidence -- a recent below-assessment sale, or a prior successful appeal.
- Filters down to comps assessed lower than yours, per square foot of building and land, and ranks them strongest-evidence-first.
- Suggests a Desired Market Value (by default, the 25th percentile $/sqft of your strongest comps -- a plain median tends to be too generous a starting ask), the appeal reason checkboxes to select, and draft text for each required "Explain..." box.
- Builds a ready-to-file narrative, a PDF exhibit with property photos, and a plain PIN list -- the exact three attachments the online filer asks for.

A few minutes and one command later, you have every file the appeal filer needs, mapped tab-by-tab to exactly where each one goes. The [README](https://github.com/mattjonesorg/cook-county-tax-appeal-comps#filing-your-appeal) walks through the whole filer, tab by tab, with a note on which pieces of output go where.

## Try it yourself

The data's public, the form is public, and now the query is too. If your reassessment notice just landed and the number made you wince, don't reach for the postcard on your counter -- grab your PIN, run `python3 comps.py`, and file it yourself.

Not in Cook County? There's also an early [DuPage County version](https://github.com/mattjonesorg/dupage-county-tax-appeal-comps) taking shape, since the same idea -- public comps data plus a public appeal form -- holds everywhere, not just here.
