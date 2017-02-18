# Simple Blog using web.py

## Setup

Install web.py

	$ pip instal 'web.py>=0.40.dev'

Clone this repo.

	$ git clone git://github.com/anandology/simple-webpy-blog.git

Intialize the database:

	$ sqlite3 blog.db < schema.sql

Run the blog application:
	
	$ python blog.py
	http://0.0.0.0:8080/

The app is up and running now. Visit <http://0.0.0.0:8080/> in your browser to see it working.
