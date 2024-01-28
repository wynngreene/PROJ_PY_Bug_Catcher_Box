from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user_Model import User
from flask_app.models.post_Model import Post
from flask import flash

######## BLEND ROUTES ########

# 01 ROUTES | 
@app.route("/dashboard_02")
def posts_home():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : session["user_id"]
    }
    
    print("01- My list of IDS!")
    posts = Post.get_all()
    print("02- My list of POST!", posts)

    user=User.get_by_id(data)

    return render_template("home.html", user=user, posts=posts)

######## GET ROUTES ########

# 02 ROUTES | Render Pages Details PAge for One post
@app.route("/posts/<post_id>")
def post_details(post_id):
    post = Post.get_one_post_id(post_id)

    return render_template("post_detail.html", post=post)

# 03 ROUTES | Render Page with Create Form
@app.route("/posts/new")
def create_page():
    print("Where is my Create page? ")
    user = session["user_id"]

    return render_template("post_create.html", user=user)

# 04 ROUTES | Render Page with Edit Form 
@app.route("/posts/edit/<post_id>")
def edit_page(post_id):
    
    post = Post.get_one_post_id(post_id)
    return render_template("post_edit.html", post=post)


#GET Action Routes:
# 05 ROUTES | Delete Route (GET request)
@app.route("/posts/delete/<post_id>")
def delete_post(post_id):
    Post.delete_by_post_id(post_id)

    return redirect("/dashboard_02")


# ######## POST ROUTES ########

# 06 ROUTES | CREATE (Process form)
@app.route("/posts", methods=["POST"])
def post_create():
    is_valid = Post.is_valid(request.form)
    if is_valid:
        Post.save(request.form)
        print(request.form)
        return redirect("/dashboard_02")
    
    return redirect("posts/new")

# 07 ROUTES | UPDATE (Process form)
@app.route("/posts/update", methods=["POST"])
def update_post():
    is_valid = Post.is_valid(request.form)
    if is_valid:
        Post.update_post(request.form)
        return redirect("/dashboard_02")
        
    return redirect(f"/posts/edit/{request.form["id"]}")
