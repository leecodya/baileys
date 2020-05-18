from flask import Flask, render_template, redirect, url_for, request, session, flash
#from datetime import timedelta

app = Flask(__name__)
company_name = "Bailey's Poultry"
short_name="Bailey's"

@app.route("/")
def home():
    return render_template("index.html", name=company_name)

@app.route("/about")
def about():
    return render_template("about.html", name=company_name, short_name=short_name)

@app.route("/equipment")
def equipment():
    return render_template("equipment.html")

@app.route("/install")
def install():
    return render_template("install.html")

@app.route("/sales")
def sales():
    return render_template("sales.html", name=company_name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<some_page>")
def invalid_page(some_page):
    return render_template("404.html")

# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         session.permanent = True
#         name = request.form["nm"]
#         session["user"] = name
#         flash("Login Successful")
#         return redirect(url_for("user"))
#     else:
#         if "user" in session:
#             flash("Already logged in")
#             return redirect(url_for("user"))

#         return render_template("login.html")
            

# @app.route("/user")
# def user():
#     if "user" in session:
#         user = session["user"]
#         return render_template("user.html", user=user)
#     else:
#         flash("You are not logged in")
#         return redirect(url_for("login"))

# @app.route("/logout")
# def logout():
#     if "user" in session:
#         user = session["user"]
#         flash(f"You have been logged out, {user}", "info")
#     session.pop("user", None)
#     return redirect(url_for("login"))