from flask import render_template, request, Blueprint
from src.dbcon.db import conn
main = Blueprint('main', __name__)


@main.route("/home")
def home():
    # all_food_items = "SELECT * FROM food_items"
    # cur.execute(all_food_items) 
    # food_items = cur.fetchall()
    return render_template('home.html')


@main.route("/cart")
def menu_cart():
   
    return render_template('cart.html')


