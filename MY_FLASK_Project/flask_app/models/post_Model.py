from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user_Model


class Post:
#---START---DONE
    DB = "bug_box_schema"

    def __init__(self, post):
        self.id = post["id"]
        self.title = post["title"]
        self.description = post["description"]
        self.link = post["link"]
        self.created_at = post["created_at"]
        self.updated_at = post["updated_at"]
        self.user = None

#---cRud|READ (GET_ONE_post)---
    @classmethod
    def get_one_post_id(cls, post_id):
        pass
        query = """SELECT * FROM posts
        JOIN users on posts.user_id = users.id
        WHERE posts.id = %(id)s;"""

        data = {
            "id":post_id
        }

        get_one_results = connectToMySQL(cls.DB).query_db(query, data)
        post_dict = get_one_results[0]

        post_obj = Post(post_dict)

        user_obj = user_Model.User({
            "id" : post_dict["users.id"],
            "first_name" : post_dict["first_name"],
            "last_name" : post_dict["last_name"],
            "email" : post_dict["email"],
            "password" : post_dict["password"],
            "created_at" : post_dict["users.created_at"],
            "updated_at" : post_dict["users.updated_at"]
        })

        post_obj.user = user_obj

        return post_obj

#---Crud|CREATE (SAVE)---
    @classmethod
    def save(cls, posts_data):
        query = """
                INSERT INTO posts ( title, description, link, created_at, updated_at, user_id)
                VALUES ( %(title)s, %(description)s, %(link)s, NOW(), NOW(), %(user_id)s );
                """
        save_result = connectToMySQL(cls.DB).query_db(query, posts_data)
        return save_result

#---cRud|READ (GET_ALL_USER)---
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM posts
        JOIN users on posts.user_id = users.id;"""

        results = connectToMySQL(cls.DB).query_db(query)

        posts = []

        for post_dict in results:
            post_obj = Post(post_dict)
            user_obj = user_Model.User({
                "id" : post_dict["users.id"],
                "first_name" : post_dict["first_name"],
                "last_name" : post_dict["last_name"],
                "email" : post_dict["email"],
                "password" : post_dict["password"],
                "created_at" : post_dict["users.created_at"],
                "updated_at" : post_dict["users.updated_at"]
            })
            # Associate user with post
            post_obj.user = user_obj
            # Append to List
            posts.append(post_obj)
        # Return the list of Posts
        return posts
    

    
#---crUd|UPDATE (UPDATE posts)---
    @classmethod
    def update_post(cls, post_data):
        query = """UPDATE posts
        SET title = %(title)s, description = %(description)s, link = %(link)s
        WHERE id = %(id)s;"""


        update_results = connectToMySQL(cls.DB).query_db(query, post_data)
        return update_results

#---cruD|DELETE (DELETE posts)---
    @classmethod
    def delete_by_post_id(cls, post_id):
        query = """DELETE FROM posts
        WHERE id = %(id)s;"""
        data = {
            "id": post_id
        }
        results = connectToMySQL(cls.DB).query_db(query, data)
        return

#---VALIDATION (Valid Inputs)---
    @staticmethod
    def is_valid(post_dict):
        valid = True

        if len(post_dict["title"]) == 0:
            valid = False
            flash("Title is required.")

        if len(post_dict["description"]) == 0:
            valid = False
            flash("Description is required.")

        elif len(post_dict["description"]) < 3:
            valid = False
            flash("Description must be at least 3 characters.")

        if len(post_dict["link"]) == 0:
            valid = False
            flash("A URL link are required.")
        elif len(post_dict["link"]) < 3:
            valid = False
            flash("link must be at least 3 characters.")

        return valid