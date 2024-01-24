from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.post_Model import Post
from flask_app.models.user_Model import User

from flask import flash

######## BLEND ROUTES ########

# 01 ROUTES | 
@app.route("/dashboard_02")
def recipes_home():
    # if "user_id" not in session:
    #     return redirect("/logout")
    # data = {
    #     "id" : session["user_id"]
    # }
    # print("My 01 list of REC!")
    # recipes = Recipe.get_all()
    # print("My 02 list of REC!")

    # user=User.get_by_id(data)

    return render_template("home.html")
    # return render_template("home.html", user=user, recipes=recipes)

######## GET ROUTES ########

# # 02 ROUTES | Render Pages Details PAge for One Recipe
# @app.route("/recipes/<recipe_id>")
# def recipe_details(recipe_id):
#     recipe = Recipe.get_one_recipe_id(recipe_id)

#     return render_template("recipe_detail.html", recipe=recipe)

# # 03 ROUTES | Render Page with Create Form
# @app.route("/recipes/new")
# def create_page():
#     user = session["user_id"]
    
#     return render_template("create_recipe.html", user=user)

# # 04 ROUTES | Render Page with Edit Form 
# @app.route("/recipes/edit/<recipe_id>")
# def edit_page(recipe_id):
    
#     recipe = Recipe.get_one_recipe_id(recipe_id)
#     return render_template("edit_recipe.html", recipe=recipe)


# #GET Action Routes:
# # 05 ROUTES | Delete Route (GET request)
# @app.route("/recipes/delete/<recipe_id>")
# def delete_recipe(recipe_id):
#     Recipe.delete_by_recipe_id(recipe_id)

#     return redirect("/dashboard_02")


# ######## POST ROUTES ########

# # 06 ROUTES | CREATE (Process form)
# @app.route("/recipes", methods=["POST"])
# def create_recipe():
#     is_valid = Recipe.is_valid(request.form)
#     if is_valid:
#         Recipe.save(request.form)
#         return redirect("/dashboard_02")
    
#     return redirect("recipes/new")


# # 07 ROUTES | UPDATE (Process form)
# @app.route("/recipes/update", methods=["POST"])
# def update_recipe():
#     is_valid = Recipe.is_valid(request.form)
#     if is_valid:
#         Recipe.update_recipe(request.form)
#         return redirect("/dashboard_02")
        
#     return redirect(f"/recipes/edit/{request.form["id"]}")
