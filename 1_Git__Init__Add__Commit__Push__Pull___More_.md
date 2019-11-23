## Python: Code, Test, Deploy

# Git: Init, Add, Commit, Push, Pull & More!
 ---

# Synopsis

#  Git: Init, Add, Commit, Push, Pull & More!
Source: https://git-scm.com/doc

[Official book (free)](https://git-scm.com/book/en/v2)

## Requirements for this module
* [Download and Install Git](https://git-scm.com/downloads)

## Task: Learn the following commands
### General Stuff
* ```git --version``` print the current version of git
* ```git --help``` print list of common commands
* ```git clone <url>``` clone a remote repo to current dir
* ```git pull <branch> <remoteurl/remotename>``` get the latest version of your project from your repo
### From Start to Pushing your first commit
* ```git init``` initialize the current directory as a git project
* ```git config --global user.email "first.last@example.com"``` set your git email
* ```git config --global user.name "first_name last_name"``` set your git name
* ```git status``` print the current state of your git project
* ```git add .``` add all the files in the current directory to your git project
* ```git commit -m "updated README.md"``` create a new commit, and include a message
* ```git push <remoteurl/remotename> <branch>``` push your new branch to your repo
### Branches
* ```git branch``` lists all the branches in the current git project
* ```git checkout -b <name>``` create a new branch and switch to it
* ```git branch -d <name>``` delete a branch
* ```git merge <name>``` merge changes from named branch to current branch
* ```git switch <name>``` switch to a different branch
### History
* ```git log``` view list of most recent commits
### Edit messages
* ```git commit --amend -m "new commit text"``` edit a previous commit 
### Connect Local repo to remote repo
* ```git remote add <remote_name> <remote_url>```
### Other useful commands
* ```git stash -u``` save your progress without creating a commit (great for quick fixes)
* ```git gui``` start the git GUI interface

## Exercise #1
Using the above guide complete the following steps in your terminal:
1. create a new repo
2. set up your git email
3. set up your git name
4. create a new file named ```README.md```
5. create a new folder name ```my_app```
6. move ```README.md``` into ```my_app``` using the command ```mv README.md my_app/example.txt```
7. commit your changes
8. check the status of your local repo
9. create a new repo in your [Github](https://github.com/) named ```python_in_1_day```
10. push this commit to the new Github repo **HINT**:See ```remote add...``` command above
11. make a change using the Github web interface
12. commit the change in the Github web interface
13. check status of your local repo
14. pull the changes you just made in the Github web interface to your local machine

**Congraulations!**: You've learned the basics of GIT and put your knowledge to use