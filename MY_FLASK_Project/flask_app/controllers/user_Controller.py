from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user_Model import User
# from flask_bcrypt import Bcrypt        
# bcrypt = Bcrypt(app) 

######## BLEND ROUTES ########

# 00 ROUTES | INDEX Login Page
@app.route("/")
def index():
    return render_template("index.html")

# 01 ROUTES | DASHBOARD 
@app.route("/dashboard")
def dashboard():
#     if "user_id" not in session:
#         return redirect("/logout")
#     data = {
#         "id" : session["user_id"]
#     }

#     print("I got my 03 LIST of", data)
    return render_template("home.html")
#     return render_template("home.html", user=User.get_by_id(data))

######## GET ROUTES ########


# 00 ROUTES | LOGOUT
@app.route("/logout")
def logout():
    session.clear()

    print("Session CLEARED!")
    return redirect("/")


# ######## POST ROUTES ########

# # 00 ROUTES | REGISTER (Process form)
# @app.route("/register", methods=["POST"])
# def register():
    
#     if not User.validate_register(request.form):
#         return redirect("/")
#     data = {
#         "first_name" : request.form["first_name"],
#         "last_name" : request.form["last_name"],
#         "email" : request.form["email"],
#         "password" : bcrypt.generate_password_hash(request.form["password"])
#     }
#     id = User.save(data)
#     session["user_id"] = id
#     return redirect("/dashboard_02")


# # 00 ROUTES | LOGIN (Process form)
# @app.route("/login", methods=["POST"])
# def login():
#     user = User.get_by_email(request.form)

#     if not user:
#         flash("Invalid Email", "login")
#         return redirect("/")
#     if not bcrypt.check_password_hash(user.password, request.form["password"]):
#         flash("Invalid Password", "login")
#         return redirect("/")
    
#     session["user_id"] = user.id

#     return redirect("/dashboard_02")
