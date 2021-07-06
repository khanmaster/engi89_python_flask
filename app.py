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