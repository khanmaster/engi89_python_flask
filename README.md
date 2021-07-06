# Model View Controller (MVC) with Python Flask
## Python Flask
# This lesson covers MVC with Flask in Python

## MVC - Model View Controller
### Display data on the browser using HTML, CSS JS and BOOTSTRAP

- HTML - Hyper Text markup language
- CSS - Cascading Style sheet
- JS - Java Script 
- BOOTSTRAP

**Building our API***
- display data from python flask to specific API call/URL/end point/
 
 **WHY FLASK and USE CASES**
 - Flask is a web app frame work
 - Very powerful to interact with DB and user interface/browsers etc
 - Flask can be used to create an API
 - It allows us to integrate with HTML, CSS JS 
 - It allows us to map HTTP requests to python functions - URL - HTTP GET
 - It allows us to set the API path as URL to view in the browser 
 
 - Let's install Flask
 - `pip install flask`
- Ensure flask is installed

- How to run the flask app - command
```
flask run
```
**interacting with HTML**
- Naming conventions are essential
- we need create templates folder in our dir
- flask looks for templates folder and anything inside the folder
- we will create index.html inside our templates folder


- Bootstrap to design our page with HTML, CSS JS 
- Flask is python micro-framework 
- Flask is used to develop web apps 
- Let's create app.py
```python
# creating a file called app.py
# Let's see how can we use Python Flask to interact with our browser
# Install flask:
# pip install flask

from flask import Flask, redirect, url_for, render_template
# we have to create an object of this class
app = Flask(__name__) # creating an app instance

# Let's create a function to link to our home/default page
# Let's connect this function to our browser
@app.route("/") # decorating our function with @app.route to set route in our browser
def index():
    return "Welcome to Engineering 89 DevOps team"

# flask run

# Let's create a welcome page
@app.route("/welcome/")# / at the end is best practice to have as it would load the page in both cases
def welcome():
    return render_template("welcome.html")

@app.route("/login/")
def login(): # redirect and url_for we need to import to redirect the users
    #return "Please login with correct details"
    return redirect(url_for("welcome")) # this will redirect the user to welcome page

@app.route("/<username>/") # passing variable provided by the user in the browser
def greet_user(username):
    return f"Welcome to flask web app dear {username}" # display the name back to user in the browsser

if __name__ == "__main__":
    app.run(debug=True)
#  Let's add our HTML file to redirect from Python flask to .html file
# we need to create a folder called templates
# project folder
    # templates folder
        #welcome.html
   #  app.py
# what if the login page is unavailable
# We would to redirect the users if they visit login page -





# create a decorator to route traffic to login page
# display 2 messages of your choice in form of h1 and h2
```
- Let's create templates folder and welcome.html

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Engineering 89 DevOps</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <nav class="navbar navbar-dark bg-dark">
  <!-- Navbar content -->
</nav>

<nav class="navbar navbar-dark bg-primary">
  <!-- Navbar content -->
</nav>

<nav class="navbar navbar-light" style="background-color: #e3f2fd;">
  <!-- Navbar content -->
</nav>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar scroll</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarScroll">
      <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarScrollingDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Link
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarScrollingDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Link</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
</head>
<body>
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

 <h1>Navigation Bar has been added</h1>
 <h2>Please login with correct details </h2>
 <form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</body>
</html>
```
- API
```python
# # https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Stream': 'DevOps'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```
