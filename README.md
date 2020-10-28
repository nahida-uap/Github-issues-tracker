Project Name : issue_tracker
Description: This is a a simple GitHub issue browser. When the app will start, it will display the list of issues with some basic information (title, issue #, state). Then it will display the list of issues 10 at a time by implementing pagination on the issue list. When an issue is clicked, it will redirect to another screen that displays more information on the issue.
Author: Nahida Sultana Chowdhury


# create virtual environemnt
$ python -m venv env
# activate the virtual environment
$ env\Scripts\activate
# deactivate
$ deactivate


Installation
============
# copy the "issue_tracker" folder

# change the working directory to "issue_tracker"
$ cd issue_tracker

# install the requirements
$ python -m pip install -r requirements.txt

# to check all the requirements successfully installed or not
$ pip freeze

# To run using command prompt
python manage.py runserver

# The development server will be start at http://127.0.0.1:8000/
# To quit Clt+c

# database located at: issue_tracker/db.sqlite3