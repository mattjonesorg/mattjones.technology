---
title: "Wordpress on Kubernetes"
date: 2016-01-23T17:23:44Z
tags: ["WordPress", "Kubernetes", "Docker", "Hosting", "DevOps"]
categories: ["Uncategorized"]
---

This [wordpress](https://wordpress.org/) instance is hosted on a private [kubernetes](http://kubernetes.io/) cluster. The default wordpress docker image has an upload limit of 8MB, which made it difficult to upload this theme and to migrate from another provider.

So, I created a new docker image that increases the upload limit to 128MB. If you'd like to use it, simply use mattjonestechnology/wordpress as your docker image.

It's available on [docker hub](https://hub.docker.com/r/mattjonestechnology/wordpress/), and the source is in the wordpress branch of [my-docker-images](https://github.com/mattjonesorg/my-docker-images/tree/wordpress) on github. Pull requests are welcome!
