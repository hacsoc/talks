Using Git
=========

Contained herein are the notes I used for the talk I gave on the git 
version control system. This is essentially a list of commands I issued 
during the talk with some notes mixed in. GitHub has an awesome source 
browser that will let you seamlessly switch between branches and commits. 
If you're shaky on any of the things I covered in the talk, poke around 
the file browser a little bit. Things might seem a little clearer.

Seriously, though, check out GitHub's git tutorial. 
It's **way** better than anything I'd be able to come up with. You can find 
it here: http://help.github.com/

* main.py - contains fib and main
* run main.py as example
* git init
* ls -a
* git status
* staging vs. staging
	* git add main.py
	* git status
	* git rm main.py
	* git status
	* git add .
* git status
* Committing
	* git commit -m "First commit!"
* git status
* git log
* Move fib() to a new file, util.py
* Run main.py to make sure everything works
* git status
* a nasty .pyc file appears!
* vim .gitignore
* git add .
* git status
* git commit -m "Moved fib to util, gitignore"
* git branch main_arg
* Add import of sys
* git checkout -- main.py
* Add argument support to main.py
* git status
* git add .
* git commit -m "Argument support for main.py"
* git checkout master
* Look at the differences between these branches!
* git merge main_arg
* Now let's add a mean function
* git branch mean_func
* Write the mean fund sum(n) / len(n)
* git stash
* git stash list
* git checkout master
* git branch hot_fix
* if max_fib > 50: raise Exception
* git status
* git commit -am "Fixed arguments too big"
* git checkout master
* git merge hot_fix
* git checkout mean_func
* git status
* git stash pop
* git status
* Add a call to mean in main.py
* git commit -am "Finished mean"
* git checkout master
* git merge mean_func



* Create github repo
* git remote add origin git@github.com:fxh32/git_talk.git
* git push
* Checkout github
* Collaboration etc}