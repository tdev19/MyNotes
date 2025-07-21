Flask is a micro-web framework written in Python. ITs lightweight, flexible and easy to use.

==what is blueprint in flask?

Blueprint is a way to organize views, static files and templates in flask. It allows you to group functionality into reusable modules that can be mounted onto main application.



![[Pasted image 20240730131909.png]]

==WSGI -- Web Server Gateway Interface

WSGI is protocol through which webserver interacts with web application.

Jinja2 -- Web templating system... It is used to create dynamic web pages

![[Pasted image 20240730132324.png]]



==Creating Virtual Environment on Ubuntu 22.==

1) install virtualenv on machine using below command -- sudo apt install virtualenv
2) create virtual environment using --- virtualenv --python=python3 flask_env
3) activate virtual environment using --- source flask_env/bin/activate
4) run your file using ---- /home/Projects/flask/flask_env/bin/python3 /home/Projects/flask/proj1/app.py

==Why do we use  dunder name  ==  dunder Main while writing scripts in python?==

--> We use it to make sure that the functions in the script/module should only get called 
when it is directly being run and not when it is imported as a module to be used in some other script.

The dunder __name__ is a built-in special variable that evaluates the name of the current module.


==What is the use of debug=True option?

when we use this option while running our flask app. if any change is made in application the app gets restarted automatically and new changes get reflected.


==Creating URLs dynamically and passing variables 

```Python
from flask import Flask,redirect,url_for

  

###WSGI application

app = Flask(__name__)

  

#decorator

@app.route('/')

def welcome():

    return "This is my flask app! Is it though????"

  

@app.route('/success/<int:score>')

def success(score):

    return (f"Congratulations! You have passed and your score is {score} ")

  

@app.route('/fail/<int:score>')

def fail(score):

    return (f"We regret to inform you that you have not passed. your score is {score} ")

  

@app.route('/result/<int:marks>')

def result_checker(marks):

    result = ""

    if marks>=35:

        result = "success"

        #print(url_for(result))

        return redirect(url_for(result,score=marks))

    else:

        result = "fail"

        return redirect(url_for(result,score=marks))

  

if __name__=='__main__':

    app.run(debug = True)
```


==What is flask WTF?

IT is an extension of flask that provides support for handling HTML forms. IT includes features such as form validation, CSRF protection and file uploads.

==What is flask SQL Alchemy?

Its a flask extension which is used for database management through SQLAlchemy. It provides features to create, read, update and delete data using python objects and SQL queries.

==Flask REstful

Used for creating REST APIs It provides support for input validation, authentication and error handling. You can user Restful to define resources and their methods.

==Flask-JWT

Its a flask extension used for JWT authentication. for flask applications. We can use it by creation JWT object with required configuration and defining routes with decorators  provided by the extension.

==REad json in python

import json

# Sample JSON data
json_data = '''
{
  "people": [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "San Francisco"},
    {"name": "Mike", "age": 35, "city": "Chicago"}
  ]
}
'''

# Load JSON data
data = json.loads(json_data)

# Loop through nested list
for person in data['people']:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")






