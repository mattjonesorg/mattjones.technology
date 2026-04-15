---
title: "The Principle of Subsidiarity and Enterprise Architecture"
date: 2026-04-15T00:00:00Z
tags: ["Enterprise Architecture", "Governance", "AI", "Leadership"]
description: "Subsidiarity holds that decisions should be made at the lowest level positioned to make them well. It should drive how enterprise architecture teams operate."
image: "/images/subsidiarity-enterprise-architecture.svg"
---

Enterprise architects love centralization. It's in our DNA. We see inconsistency across teams and our instinct is to fix it with a standard. One framework. One pipeline. One way.

But there's a principle that suggests a better path. Not centralize everything, and not hands-off either. Something more nuanced.

The principle of subsidiarity holds that decisions should be made at the lowest level positioned to make them well, and that centralized authority exists to support and enable other levels, not to absorb their responsibilities. It cuts both ways: the center has real authority over things that are genuinely universal, while teams own what requires local knowledge.

I first encountered subsidiarity through Catholic social teaching, where it has been a core principle for nearly a century. But the idea has broader reach. It's written into the EU treaties as the principle governing which decisions belong at the European level versus with member states. It shows up anywhere an organization wrestles with the question of what to centralize and what to leave local.

It should drive how enterprise architecture teams operate.

## The Temptation of Two Extremes

Most EA teams fall into one of two failure modes. The first is over-centralization: detailed standards for everything, review boards that become bottlenecks, mandates that ignore the reality of what teams actually need. The architect becomes a gatekeeper, and teams learn to route around the architecture function entirely.

The second is abdication: the architecture team publishes a few reference documents, runs a quarterly review, and otherwise stays out of the way. Teams make all their own decisions. Some make great ones. Others make choices that create security exposure, operational fragility, or vendor lock-in that won't surface for years.

Subsidiarity rejects both extremes. The answer isn't "center decides" or "teams decide." It's both levels collaborating to decide what each is positioned to decide well.

## What Belongs at the Center

Some decisions genuinely belong with the architecture team. Language and runtime versions are a good example: mandating that teams use languages generally supported by the organization, and that the versions running are actively receiving security patches is a legitimate central concern. So is selecting supported frameworks to ensure fungibility, so that engineers can move between teams without learning an entirely new stack. API design standards, security baselines, and CI/CD pipeline requirements all belong here too.

These are organization-wide concerns: security posture, talent mobility, operational consistency. The architecture team is positioned to guide these decisions because they require an enterprise-wide view that no single team has.

## What Belongs with the Team

Engineering teams know their domain. They know their codebase conventions, their test strategy, their legacy constraints. The architecture team doesn't have that context at the level of specificity required to make good decisions, and shouldn't pretend to.

When centralized authority takes on decisions it isn't positioned to make well, the result isn't order. It's dysfunction wearing a governance badge.

## A Concrete Example: AI Agent Harnesses

An area where I've been thinking a lot about central versus distributed control is in the AI development harnesses every organization needs to be creating right now. Tools like Claude Code, GitHub Copilot, and Cursor all support configuration that shapes how AI agents work within your codebase.  In all the demos, it's usually files in your local repository, which is a really fast way for teams to get started, but it defers all of the decisions to the local team, and misses an opportunity to centralize some things that should be centralized.  

The answer should be a layered framework, and we need to create it. In this ideal harness, the architecture team would manage a base layer containing universal standards: security rules every agent must follow, approved runtimes, supported frameworks, API conventions, minimum testing requirements. This base layer would be part of every team's harness. It is not optional.

The team owns the second layer: domain-specific agent definitions, codebase conventions, test structure, the skills and patterns their agents need. The team knows these things because they live in this code every day.

Universal standards are part of everyone's work. Local expertise makes each harness effective. 

## The Architect's Real Job

Subsidiarity redefines the architect's role. Not gatekeeper. Not absentee. The job is to own what's genuinely universal, make teams capable of owning everything else, and have the discipline to know which is which.

That's harder than writing standards. It requires judgment about where the center's responsibility ends and the team's begins. But the best governance isn't the governance that controls the most. It's the governance that puts each decision where it will be made best.

---
*The views expressed here are my own and do not represent the views of my employer.*
