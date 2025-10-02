---
title: "Containerize the old stuff!"
date: 2016-09-30T20:25:25Z
tags: ["Docker", "Kubernetes", "Legacy Applications", "Containerization", "DevOps"]
categories: ["Uncategorized"]
---

[Docker](https://www.docker.com/) and container cluster managers like [Kubernetes](https://kubernetes.io) have helped our industry to embrace microservice architectures. Where I [work](https://www.fitchsolutions.com/), we are building cloud native applications at an incredible pace previously inconceivable with a team our size. The productivity gains of a modern stack including Docker, Kubernetes, Spring Boot, and AWS are undeniable. We spend more time focusing on our applications, and less time focusing on releases, though we do release often.

One would probably be foolish to start a new project today without at least considering these amazing tools. But what about the old stuff? What about those apps we wrote 5, 10, or 15 years ago that everybody is afraid to touch? Can we benefit from containerizing these? I think so! If you've been a software engineer for more than about 5 years, you probably have some side projects running on old servers that you may have had to upgrade periodically. For me, these ran on shared hosting, VPS's, and eventually cloud VMs that I managed. Each time a provider was either going out of business or forced me to change servers, I had to redeploy my application to a new server with a new configuration.

I've had this theory for a while of just containerizing the old stuff to reduce maintenance on it. To test this theory, I took a website that I wrote shortly after September 11, [www.prayersforpeace.org](https://www.prayersforpeace.org) and moved it onto my Kubernetes cluster hosted in Google Container Engine. I'm not particularly proud of the architecture of this 15 year old application, but I think that's fair since it was one of my first web applications. I've learned and grown a lot since then and I'd never do it the same way. I did have to make some changes to the code to receive some of the configuration from the environment (because really, hardcoded passwords are so 15 years ago). Overall it was a pretty easy process. Here are the advantages of containerizing this old site:

*   One less server to run saves me money!
*   Explicit configuration of the environment via Docker means I don't have to remember the details of how the old server is configured.
*   That 6 year old version of Linux that probably had a lot of vulnerabilities is gone. Keeping the container up to date is much easier.
*   The attack surface of a container is smaller than a VM.
*   I can make changes locally and test them out without having to worry about breaking the fragile server.
*   Healthchecks! As a cluster manager, Kubernetes automates nearly any task I previously would have done to restart a service.
*   [TLS All The Things!](/blogs/tls-all-the-things/) -- Automated, free SSL certificate renewal. Need I say more?

Docker and Kubernetes certainly support microservices, but there's still huge benefits for the monoliths to be containerized. All of my side projects are now running on this cluster. The next step is to test the theory professionally. If you have containerized a "[legacy](https://twitter.com/drewlesueur/status/767122443102097409)" application, please comment with your experiences!
