from src.dbcon.db import conn
from flask import render_template, request, Blueprint


menu = Blueprint('menu', __name__,url_prefix="/menu")

@menu.route("/", methods=['GET', 'POST'])
def all_menu_products():
   
    return render_template('all-menu-items.html')

@menu.route("/single", methods=['GET'])
def single_menu_item():
   
    return render_template('single-product.html')