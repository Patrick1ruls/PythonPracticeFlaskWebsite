from flask import Flask, render_template, url_for

app = Flask(__name__)


# Initialize variables
posts = [ # List (or JSON) of blog post
    {
         'author': 'Patrick Vermillion',
         'title': 'Blog Post 1',
         'content': 'First post content',
         'datePosted': 'April 1, 2019'
    },
    {
         'author': 'Corey Schafer',
         'title': 'Blog Post 2',
         'content': 'Second post content',
         'datePosted': 'April 5, 2019'
    } 
]


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", posts = posts)


@app.route("/about")
def about():
    return render_template("about.html", title = "About")


if __name__ == "__main__": # Starts program only when this file is called directly
    app.run(debug = True) # Starts the app in developer mode which shows changes without having to shut down the server
