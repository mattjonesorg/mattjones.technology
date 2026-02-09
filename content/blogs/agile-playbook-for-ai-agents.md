---
title: "Your Agile Playbook Already Works for AI Agents — You Just Don't Know It Yet"
date: 2026-02-09T00:00:00Z
tags: ["AI", "Agile", "Claude", "Software Engineering", "Productivity", "Anthropic"]
description: "The agile practices we've been refining for years are exactly what agentic AI systems need. If you've led engineering teams, you already have the mental model."
image: "/images/agile_playbook.png"
---

I spent this weekend deep in Claude Code, building with AI agents in a way that finally clicked. Not because the technology suddenly got better — but because I stopped treating it like a new thing and started treating it like a team.

Here's the punchline: the agile practices we've been refining for years are exactly what these agentic systems need. The ceremonies, the roles, the feedback loops — they're not just transferable, they're essential. We probably need to refine some of them for this new context, but the core elements — communication, small teams, a prioritized backlog, sprint demos, and retrospectives — they all still apply.

If you've led engineering teams, you already have the mental model. You just need to map it.

## The Orchestration Layer Changes Everything

Claude Code recently shipped a feature called [Agent Teams](https://code.claude.com/docs/en/agent-teams) that makes this concrete. It introduces an orchestration layer where one session acts as the team lead while specialized teammates each run in their own context window — meaning the backend agent isn't confused by all the frontend context or user advocate context in its runtime. Each agent only sees what it needs to see, which keeps it focused and effective. Teammates communicate with each other directly, coordinate through a shared task list, and the lead synthesizes their work.

And if you've ever run standups, the orchestrator's role will feel familiar too. It checks in with each agent, asks what they're working on, identifies blockers, and makes sure everyone is moving toward the right goals. It's the scrum master of the agent team — keeping communication flowing and course-correcting before small misalignments become big problems.

As much as we've wanted developers to be full-stack generalists, in the AI agent world, that's too much context for one agent to handle well. I had much better results when I stopped asking a single agent to do everything and instead introduced a **backend engineer agent** and a **frontend engineer agent**, each with their own specialization, and let them communicate with each other.

Think of it less like one senior dev and more like a small scrum team — each member knows their domain, and the orchestration layer acts as the communication bus between them.

## Build the Whole Team

Once I committed to the idea that agents work better with specialization, I kept going. Beyond the frontend and backend engineers, I added:

An **architecture agent** that doesn't write code but knows all the best practices that need to apply to the codebase. It reviews decisions, enforces patterns, and keeps the system coherent — the same role a principal engineer plays on a human team, except it never gets pulled into a production incident and forgets to review your PR.

A **QA agent** that tests alongside the engineers and provides immediate feedback on what needs to be fixed. This is the inner loop — catching bugs and regressions as code is being written, before it ever gets to a user-facing review.

A **docs agent** that keeps documentation current as features are built, rather than treating docs as an afterthought that never gets done.

Each of these agents has a distinct perspective and set of concerns, just like their human counterparts would. The architecture agent and the QA agent work during development. The user advocate agent — which I'll get to next — comes in after, looking at the finished product from an entirely different angle.

## The Backlog Has Never Looked This Good

I introduced a **product manager agent** whose job is to prioritize my GitHub issues and flesh them out into proper specifications. The results have been remarkable.

I can say something as simple as *"add an issue to ensure that all API calls check the JWT properly and run in the context of the current user,"* and within seconds, the PM agent expands it into a full specification — one that understands my application's architecture and conventions. Acceptance criteria, edge cases, implementation notes — all of it, contextualized to my codebase.

My backlog has never looked this good. And more importantly, it's never been this *actionable*. The agents downstream can pick up these issues and run with them because the specifications are clear and complete.

## The User's Voice in the Room

Here's a problem every team knows: we try to have engineers or product managers proxy for real users, and the feedback is slow, infrequent, and filtered through a technical lens. We know we should be getting user feedback continuously, but in practice it happens at the end of a sprint — or worse, after release.

I added a **user advocate agent** that represents the end users and their needs. Crucially, this agent doesn't think like an engineer. It thinks like the person who's going to sit down and actually use the thing. It complains if something is too hard to find. It pushes back if a workflow requires too many clicks. It provides feedback to the frontend engineer and the team lead while each feature is being built — not after.

And here's what makes this so powerful: when the user is providing feedback during development, it's a game changer whether that user is a real person or an AI agent. The feedback loop tightens from days to minutes. By the time I'm looking at the work, the AI has already reviewed it from the user's perspective.

The user advocate agent also writes a demo script — step by step, it tells me exactly where to click to exercise the new features. This addresses an issue I'd been hitting repeatedly with AI code generation: the agent would confidently do a bunch of work, declare it done, and I'd spend hours hunting down all the things that didn't actually work.

Introducing the user advocate step in the feedback loop activated turbo mode. I went from "let me spend an hour verifying this" to "let me walk through this script and confirm." The difference in velocity is hard to overstate.

## The Retrospective: Teaching the System to Learn

Every team gets better through retrospectives, and AI agents are no different. Whenever Claude fails — which happens less and less — I ask it a simple question:

*"What could I have put into claude.md or the agent instruction file that would have caught this?"*

Then I take that answer and commit it. The failure becomes a guardrail. The system literally learns from its mistakes, not through fine-tuning or retraining, but through better instructions — the same way a team improves through better processes and documentation.

This is the retrospective in its purest form: inspect, adapt, commit.

## The Bigger Picture

The patterns here aren't new. They're the same ones we've been applying to human teams for years:

- **Small, specialized teams** beat monolithic generalists — for humans and for agents.
- **A well-groomed backlog** is the difference between productive sprints and chaos — whether your developers are people or AI.
- **Fast feedback loops** catch problems early — and a user advocate agent never gets tired of testing.
- **Retrospectives drive continuous improvement** — and `claude.md` is your team's living knowledge base.

If AI agents feel like an entirely new discipline you have to learn from scratch — I'd push back on that. The discipline is the one you've already been practicing. The agents are new. The playbook isn't.

Trust it.
