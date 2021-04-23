import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("index.html")


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/search", methods=["GET", "POST"])
def search():
    """search:
    * Queries database for strings entered in search bar.

    \n Args:
    * None.

    \n Returns:
    * Template with the search query filtering books\
    containing search words.
    """

    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    """register:
    * Checks if username exists in db.
    * Will return user to registration page with a flash\
    error message if user not new.

    \n Args:
    * None.

    \n Returns:
    * user profile template if successful.
    * register page with flash displaying error if unsuccessful.
    """

    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """login:
    * Checks if username exists in db.
    * Logs user in if credentials match.
    * Appends username to session['user'] cookie.

    \n Args:    
    * None.

    \n Returns:    
    * User profile template if successful.
    * Login page with flash displaying error if unsuccessful.
    """

    if request.method == 'POST':
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """profile:
    * Searches for a users' book reviews 

    \n Args:    
    * username

    \n Returns:    
    * User book reviews for their profile page.     
    """

    # grab the session user's username from db
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if session["user"] == username:
            books = list(mongo.db.books.find({"created_by": username}))
            return render_template("profile.html", books=books, username=username)

        return redirect(url_for("get_books"))

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """logout:
    * Removes user from session. 

    \n Args:    
    * None

    \n Returns:    
    *   Confirmation user is logged out.  
    """

    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """add_review:
    * Posts user review from form to MongoDB

    \n Args:    
    * None.

    \n Returns:    
    * Submits user review form to MongoDB 
    """

    if "user" in session: 
        if request.method == "POST":
            books = {
                "genre_name": request.form.get("genre_name"),
                "book_title": request.form.get("book_title"),
                "author": request.form.get("author"),
                "book_review": request.form.get("book_review"),
                "book_rating": request.form.get("book_rating"),
                "image_url": request.form.get("image_url"),
                "buy_link": request.form.get("buy_link"),
                "created_by": session["user"]
            }
            mongo.db.books.insert_one(books)
            flash("Review Successfully Added")
            return redirect(url_for("get_books"))

        genres = mongo.db.genres.find().sort("genre_name", 1)
        return render_template("add_review.html", genres=genres)

    return redirect(url_for("login"))


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    """edit_book:
    * Allows user to submit changes to own review.
    * Allows admin to allow update reviews and post\
        affiliate links. 

    \n Args:    
    * book_id

    \n Returns:    
    * Updated review if changes were submitted successfully.     
    """

    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        if book["created_by"] == username or session["user"] == "admin":
            if request.method == "POST":
                submit = {
                    "genre_name": request.form.get("genre_name"),
                    "book_title": request.form.get("book_title"),
                    "author": request.form.get("author"),
                    "book_review": request.form.get("book_review"),
                    "book_rating": request.form.get("book_rating"),
                    "image_url": request.form.get("image_url"),
                    "buy_link": request.form.get("buy_link"),
                    "created_by": session["user"]
                }
                mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
                flash("Review Successfully Updated")

            genres = mongo.db.genres.find().sort("genre_name", 1)
            return render_template(
                "edit_review.html", book=book, 
                genres=genres)

        return redirect(url_for("get_books"))

    return redirect(url_for("login"))


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    """delete_book:
    * Allows user to delete own review.
    * Allows admin to delete book reviews. 

    \n Args:    
    * book_id

    \n Returns:    
    * Delete review and confirm successful.     
    """

    if "user" in session: 
        username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        if book["created_by"] == username or session["user"] == "admin":

            mongo.db.books.remove({"_id": ObjectId(book_id)})
            flash("Book Review Successfully Deleted")
            return redirect(url_for("get_books"))

        return redirect(url_for("get_books"))

    return redirect(url_for("login"))


@app.route("/get_genres")
def get_genres():
    """get_genres:    
    * Allows admin to access the manage genres\
        page. 

    \n Args:    
    * None.

    \n Returns:    
    * Renders manage genres webpage.
    """

    if "user" in session: 
        if session["user"] == "admin":

            genres = list(mongo.db.genres.find().sort("genre_name", 1))
            return render_template("genres.html", genres=genres)

        return redirect(url_for("get_books"))

    return redirect(url_for("login"))


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    """add_genre:
    * Allows admin to add new genres. 

    \n Args:    
    * None.

    \n Returns:    
    * Posts new genre to MongoDB and confirms successful.
    """

    if "user" in session: 
        if session["user"] == "admin":
            if request.method == "POST":
                genre = {
                    "genre_name": request.form.get("genre_name")
                }
                mongo.db.genres.insert_one(genre)
                flash("New Genre Added")
                return redirect(url_for("get_genres"))

            return render_template("add_genre.html")

        return redirect(url_for("get_books"))

    return redirect(url_for("login"))


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    """edit_genre:    
    * Allows admin to update genres.  

    \n Args:    
    * genre_id

    \n Returns:    
    * Updated genre and confirmation message if successful.  
    """

    if "user" in session: 
        if session["user"] == "admin":

            if request.method == "POST":
                submit = {
                    "genre_name": request.form.get("genre_name")
                }
                mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
                flash("Genre Successfully Updated")
                return redirect(url_for("get_genres"))

            genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
            return render_template("edit_genre.html", genre=genre)

        return redirect(url_for("get_books"))

    return redirect(url_for("login"))


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    """delete_genre:    
    * Allows admin to remove genre.

    \n Args:    
    * genre_id

    \n Returns:    
    * Deletes genre and confirms if it was succesful.
    """

    if "user" in session: 
        if session["user"] == "admin":

            mongo.db.genres.remove({"_id": ObjectId(genre_id)})
            flash("Genre Successfully Deleted")
            return redirect(url_for("get_genres"))

        return redirect(url_for("get_books"))

    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(e):
    """page_not_found:
    * Responds to 404 error when page not found. 

    \n Args:    
    * e

    \n Returns:    
    * Error message.  
    """

    return render_template("error.html"), 404


@app.errorhandler(500)
def internal_error(e):
    """internal_error:
    * Responds to 500 internal error.

    \n Args:    
    * e

    \n Returns:    
    * Error message.  
    """

    return render_template("error.html"), 500


@app.errorhandler(503)
def service_unavailable(e):
    """service_unavailable:
    * Responds to 503 when service unavailable.

    \n Args:    
    * e

    \n Returns:    
    * Error message.  
    """

    return render_template("error.html"), 503


# Reminder: change to debug=False before submission!
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)