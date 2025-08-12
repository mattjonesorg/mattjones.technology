---
title: "TLS All The Things!"
date: 2016-09-04T03:16:14Z
tags: ["TLS", "HTTPS", "LetsEncrypt", "Kubernetes", "Security"]
categories: ["Uncategorized"]
---

We all know to use HTTPS and TLS on things that matter. For the last 15 years of work, without exception, I've used use https. But privately, I have quite a few domains for myself and for friends, and having TLS on a personal blog didn't seem worth the investment. But, thanks to [Lets Encrypt](https://letsencrypt.org/) it's now free to do.

And since nearly all of my non-work stuff is now running in a privately hosted [Kubernetes](https://kubernetes.io/) cluster, securing all the sites was really simple. The [kube-lego](https://github.com/jetstack/kube-lego/tree/master/examples/nginx) example on github was very simple to follow. Kube-lego will make the calls to letsencrypt.org when there isn't a certificate available.

One of the issues I had previously had with Kubernetes is that, when hosted in GKE, it creates an HTTP Load Balancer for each kubernetes service that you expose. Load Balancers aren't cheap. With this new approach, I use nginx to manage my ingress controllers and have reduced my external load balancers down to one.

All in all, for a couple hours of tinkering while not sleeping, I'm pretty happy. Now I'm ready to bring the rest of my self-hosted apps onto the cluster, with TLS this time around!
