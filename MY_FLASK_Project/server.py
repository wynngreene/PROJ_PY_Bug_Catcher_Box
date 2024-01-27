from flask_app import app
from flask_app.controllers import user_Controller
from flask_app.controllers import post_Controller

if __name__ == "__main__":
    app.run(debug=True)