# Day 3 (Flask-LFH)

We missed something yesterday ie `generators`

```
In [1]: def do_twice(func): 
   ...:     def wrap(): 
   ...:         func() 
   ...:         func() 
   ...:     return wrap 
   ...:                                                                                                                                                                                                            

In [2]: def hello(): 
   ...:     print("Welcome to LFH") 
```

### Without generators

```
In [4]: do_twice(hello)()                                                                                                                                                                                          
Welcome to LFH
Welcome to LFH
```

### With generators?

```
In [6]: @do_twice 
   ...: def hello(): 
   ...:     print("Welcome back") 
   ...:                            
```

Any Django users here? If yes, name a generator in Django

## Templates and web forms

You’ve written the authentication views for your application, but if you’re running the server and try to go to any of the URLs, you’ll see a TemplateNotFound error. That’s because the views are calling render_template(), but you haven’t written the templates yet. The template files will be stored in the templates directory inside the flaskr package.
Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. 

> Flask uses the Jinja template library to render templates.

### Flask file structure

```
project
| hello.py
| requirements.txt
|___ app
     |___ init.py
     |___ routes.py
     |___ templates/
          |___ index.html
          |___ other html files
```

### Without templates

```

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    user = {'username': 'Micheal'}
    return '''
<html>
    <head>
        <title>Tinkerhub LFH | Python Track</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + ''' , Welcome to day 03</h1>
    </body>
</html>'''

if __name__ == '__main__':
   app.run(debug = True)
```

## With Templates


Make directory templates

> (venv) $ mkdir app/templates

Create an templates/index.html file

**app/routes.py**
```
from flask import Flask , render_template
app = Flask(__name__)


@app.route('/')
def index():
    user = {'username': 'Miguel'}
    return render_template('hellob.html', user=user)

```

**app/templates/index.html
```

<html>
    <head>
        <title>TinkerHub LFH Programe</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>

```

## Conditional Statements

```
<html>
    <head>
        <title>Tinkerhub LFH Programe</title>
    </head>
    <body>
        {% if username %}
        <h1>Hello, {{ user.username }}!</h1>
        {% else %}
        <h1>Hey There!</h1>
        {% endif %}
    </body>
</html>
```

# Don't Worry

## For-loops

```
<html>
    <head>
        <title>TinkerHub LFH Programe</title>
    </head>
    <body>
        <h1> Welcome to program!</h1>
        {% for i in users%}
          <p>{{i.username}} </p>
        {% endfor %}

    </body>
</html>

```

## Forms

Let create a basic form at first:

```
<html>
   <body>
      
      <form action = "login" method = "POST">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nm" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>

   </body>
</html>

```
Then modify routes with more contents:

```
@app.route("/")
def welcome():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    user = request.form['nm']
    opstring = 'Hey ' + user + ', Welcome to The Tinkerhub LFH Program'
    return opstring 
```

## Task

We learned Forms & Templates yesterday. Create forms for creative things - chuck the regular Registration forms and see you can create a form for something fun. Once it's done, post the screenshot in the group. It would be fun! Super cool if you can figure out how to make it pretty [ Psst- Remember CSS and the static folder?]


### References

- [Templates Docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/)
- [Mega tutorial flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [Flask quick start](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
