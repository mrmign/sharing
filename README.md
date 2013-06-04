Sharing
===========

Share your RSS and Bookmarks together, and choose what others shared that attracts you.

this is a wonderful platform.

## Install
### Environment:

Linux, Python 2.7+, MySQL 5.5

### Software needed

1. Install tornado. 
>sudo easy_install tornado

2. Install storm. 
>* sudo add-apt-repository ppa:storm/ppa
>* sudo apt-get update
>* sudo apt-get install python-storm 

3. Install mysql.
>sudo apt-get install mysql-server

4. Install python-mysql
>sudo apt-get install python-mysqldb

5. Install beautifulsoup
>sudo easy_install beautifulsoup4

## Get the code

    git clone https://github.com/mrmign/sharing.git

## Configuration

* Import database tables
>$sh database/import.sh

 The default MySQL user and password are both root, 
if yours are not, please modify them in the `database/import.sh` file, then redo
the command.

* Modify the Database connection user and password.

In `models.database.py` line 84.

    _database = create_database("mysql://root:root@localhost:3306/share") 

change user:password to your own.

## Usage

Run the app with the command `python app.py`.  The default port is 8000, 
you can change the port with `python app.py 8080` or other ports.