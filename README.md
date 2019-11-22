# Elements of Python: Code, Test, Deploy
A very short workshop that will teach you the essentials required to get started with Python programming

## Schedule

1. Workshop Guidelines(9:15-9:20)
2. Git: Init, Add, Commit, Push, Pull & More! (9:20 - 10:30) 25min wstępu, 30min zadań, 15min przerwa
3. Enough Python to build something (10:30 - 11:30) 15min, 30min, 15min
4. Write all sorts of tests (11:30 - 12:30) 15min, 30min, 15min
5. Working with databases (12:30 - 13:00)
6. Lunch (13:00 - 14:00)
7. Flask 1: A Web app in an hour (14:00 - 15:00) 15min, 30min, 15min
8. Flask 2: A Rest API in an hour (15:00 - 16:00) 15min, 30min, 15min
9. Deploy Flask App to Heroku (16:00 - 16:30)
10. Other course info (16:30 - 16:40)
11. App Ideas: What do you want to build now? (16:40 - 17:00)

# Workshop Guidelines
* format is step-by-step tutorial w/basic theory
* lunch is at 13:00-14:00
* the core content is based on free materials so you can expore all these topics further!

## Required Accounts 
* Register for a free account at [Heroku](https://www.heroku.com/)
* Register for a free acount at [Github](https://github.com/)

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

# Enough Python to build something
Source: https://docs.python.org/3/






## Bonus Python Links!
Free resources to practice programming
* [Code Kata](http://codekata.com/)
* [The Python Challenge](http://www.pythonchallenge.com/)
* [Code Wars](https://www.codewars.com/)
* [Project Euler](https://projecteuler.net/)

# Write all sorts of tests
Source: https://docs.pytest.org/en/latest/

## Bonus Testing Links!
* [The Hitchhiker's Guide to Python: Testing Your Code](https://docs.python-guide.org/writing/tests/)

# Working with databases
Source: https://docs.mongodb.com/

## Bonus Database Links!
* [The Little MongoDB Book](https://www.openmymind.net/mongodb.pdf)

# Lunch
Source: PIZZA!

# Flask 1: A Web app in an hour
Source: https://flask.palletsprojects.com/en/1.1.x/

## Bonus: Flask Extensions
### Flask Security
Source: https://pythonhosted.org/Flask-Security/
### Flask Testing
Source: https://pythonhosted.org/Flask-Testing/

# Flask 2: A Rest API in an hour
Source: https://flask-restful.readthedocs.io/en/latest/

# Deploy Flask App to Heroku 
Source: https://github.com/datademofun/heroku-basic-flask

---
# Free Stuff
## Books
* [Long list of programming books](https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md#python)

## Tools

### IDE
* [Visual Studio Code](https://code.visualstudio.com/)

### Networking
* [Wireshark: network protocol analyzer](https://www.wireshark.org)

## Labs/Environment
### Pen Testing
* [Hack the Box: Pen-Testing Labs](https://www.hackthebox.eu/)

### Machine Learning
* [Google Colab: Includes free GPU time*](https://colab.research.google.com/)
*Free GPU limited to 12-hours per month
* [Keras: The Python Deep Learning Library](https://keras.io/)
* [Tensorflow:End-to-end open source machine learning platform](https://www.tensorflow.org/)
* [Pytorch:An open-source machine learning framework](https://pytorch.org/)

## Data sets
* [Google Public Data Search](https://www.google.com/publicdata/directory#!)
* [Kaggle Datasets](https://www.kaggle.com/datasets)
* [Project Gutenburg: 60,000 free e-books*](https://www.gutenberg.org/)
*most are public domain and can be used for various purposes
* [Big Data: 33 Brilliant and Free Data Sources anyone can use](https://www.forbes.com/sites/bernardmarr/2016/02/12/big-data-35-brilliant-and-free-data-sources-for-2016/)

