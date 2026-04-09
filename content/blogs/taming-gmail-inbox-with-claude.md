---
title: "Taming My Gmail Inbox with Claude"
date: 2026-04-08T00:00:00Z
tags: ["AI", "Claude", "Productivity", "Gmail", "Automation"]
description: "My Gmail inbox was out of control. I connected Claude to it, and in one conversation I had a cleanup plan and a filter file ready to import. Here's how you can do the same."
image: "/images/taming-gmail-inbox.svg"
---

My personal Gmail inbox was overwhelming, and I needed to figure something out.

And since it's 2026, I did what any self-respecting technologist would do: I asked Claude to help me. I connected it to my Gmail, and it looked through my inbox and made pretty great suggestions for what could be filtered out, batch read later, archived, or deleted. Within a few minutes I had a clear picture of where the clutter was coming from and a plan to deal with it.

## Filters That Haven't Aged Well

I've had Gmail filters for years, but they hadn't aged well and needed a good refresher. Services I'd signed up for in 2018 were still hitting my inbox. Newsletters I'd lost interest in were piling up unread. Notification emails from tools I no longer use were mixed in with things that actually mattered. Claude was able to spot all of this just by scanning what was there and asking a few clarifying questions.

## The XML Trick

In this process, I learned something I hadn't known: Gmail has a way to let you upload an XML file defining the filters you want to add. So, of course, Claude generated that for me.

Any AI chatbot can do this part, and if you want to try it yourself, here's a prompt to get started:

> "Look through my email and suggest filters and labels I should have to keep things organized, so that only the emails I actually need to focus on stay in my inbox. Once we agree on a plan, generate a mailFilters.xml file that implements the rules we decide on."

To import the file:

1. Click the gear icon in Gmail, then **"See all settings."**
2. Go to the **"Filters and Blocked Addresses"** tab.
3. Scroll to the bottom and click **"Import filters."**
4. Choose your file, and hit **"Create filters."**

What would have been an afternoon of clicking through the Gmail UI to manually create filters becomes a single conversation and a file upload.


