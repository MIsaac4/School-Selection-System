from flask import Blueprint, render_template

# Index blueprint
index_bp = Blueprint("user", __name__)

@index_bp.route("/")
def index():
    return render_template("index.html")