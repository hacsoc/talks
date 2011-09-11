# Linux intro and installation

## Background

Linux is an operating system for my computer, in the same sense as Windows 7 and Mac OS X.  It provides the basic set of functionality under which my computer operates.

The actual word Linux refers only to a very small subset of what we expect from an operating system.  People take this bit, called the kernel, and package it with other tools to make it fully-functional.  There are many different packaged "distributions" out there.  The one I use most often is called Ubuntu [1], and I'm going to install it on my computer right now.   When I'm done, I will have both Windows and Ubuntu on my computer.  I'll be able to choose between the two of them every time I turn my computer on.

## Preparation

I've downloaded a 700MB file from [ubuntu.com](http://ubuntu.com) and put it on a flash drive.  When you do this, I recommend burning it on a CD.  You can use [Infra Recorder](http://infrarecorder.org/) according to the [guide here](http://www.ubuntu.com/download/ubuntu/download).  To start the installation, I need instruct my computer to boot up and run the code that came on the CD.  I'll start by rebooting my computer.

The hardest part of the whole thing might be just getting the Ubuntu CD to boot up.  My computer is configured to boot from the internal hard drive when it starts, so I'll have to explicitly tell it to look on the CD instead.  On my laptop I do this by pressing F12 when the computer first turns on, but there are different steps for different computers.  Look for instructions at the bottom of the screen when your computer first turns on.

Once Ubuntu boots up, I'll have an opportunity to use the operating system just from the CD.  I can use Ubuntu in nearly the same way I normally would, but without making any permanent changes to my computer.  The permanent changes only happen when I press "Install."

## Installation

When I start the installation, the installer program will ask me a bunch of questions.  The only real important question is where to put Ubuntu.  I'm choosing "Install Ubuntu alongside Windows 7" because it will allow me to choose between Windows 7 and Ubuntu when I start up the computer.  This is called dual-booting.  When dual-booting, the hard drive will be split up into partitions, one for Ubuntu and another for Windows.  The Windows partition will have to be shrunk to make room for the Ubuntu one.  Because of this, I will lose some of my space available to Windows.  The installer will do its business for a while.

### Note

There is another way to install Ubuntu, using a tool called Wubi.  I haven't done this myself, so I can't endorse it, but it may suit your needs.

## Open-source

Linux is open-source.  The code that powers it is freely available, unlike other operating systems.  Here is [some code](http://lxr.linux.no/linux+v3.0.4/mm/huge_memory.c) that makes up the Linux kernel.  As a practical matter, this means that if you want to make tweaks to your system, you are free to do so. 

## What to do when you get stuck
Using a new operating system is...different.  You will sometimes be in situations where you don't know what to do.  Other people almost always have had your issue before.  Oftentimes the best problem-solving tool is Google.  Search for your issue with some key terms.  If there is an error message, include it.  This works 9 times out of 10.
