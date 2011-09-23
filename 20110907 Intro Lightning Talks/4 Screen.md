Terminal Multiplexing and YOU!
==========

Screen gives you a terminal which can persist after your SSH connection has closed.

Reasons to use a terminal multiplexer:
---------

- Run a lengthy program (crunching, or a Minecraft server, etc.) even after you disconnect.
- Allows you to resume working exactly where you left off, after your connection breaks or you switch computers.
- Additionally gives you a sort of "tab"-like interface for terminals.

How to use screen:
----------

1. SSH into your server. Screen is pretty ubiquitous on server environments.
2. Type the command "screen" to begin a new screen session.
3. Profit!!

Screen basics:
--------
- Every screen has a name. This is how you get back to it later.

Navigating Screen:
-------

    =======================================================================================
                       Outer Terminal: 
      Command                               Description     
    =======================================================================================
    screen                   Opens a new screen.
    screen -S [name]         Creates a screen 
    screen -ls               Lists all open screens and their names.
    screen -r [name]         Reattaches the screen whose name begins with [name].
    
    =======================================================================================
                       Inside A Screen: 
      Key Sequence                          Description     
    =======================================================================================
    Ctrl+a, d                 "Detaches" the screen and returns you to outer terminal.
    Ctrl+a, c                 Creates a new "tab" in the open screen.
    Ctrl+a, (p, n, or Ctrl+a) Flips through your open tabs (previous, next, or last selected)
    Ctrl+a, [number]          Goes to the n-th tab that's open.
    Ctrl+a, "                 "Select a 'tab'" menu.

Cons of Screen:
-------

- Is no longer actively developed (latest version came out in 2008).
- Has little-to-no user interface.

Enter Tmux!
========

There are other terminal multiplexers! Check out tmux!
`$ sudo apt-get install tmux`

Similar key bindings to screen
---------
Except by default it uses Ctrl+b as its hotkey. You can change this by placing the following three lines in ~/.tmux.conf

    set -g prefix C-a
    unbind C-b
    bind C-a send-prefix

Differences from screen
-------------
Then it should be similar to screen. Except for the following differences:

- Sort of "task bar" down at the bottom tells you what program is running and where you currently are.
- Tmux sessions are identified by a small number starting at 0, this number is the leftmost number in the task bar.
- To get back into session n, the command is tmux attach -t[n], but if you only have one, you can leave out the -t part.

So hopefully that gives you a bit of a primer on what your workflow could look like with a more flexible terminal provided by screen or tmux.
