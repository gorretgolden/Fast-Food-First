import re
from tkinter import E
from flask import flash,redirect, render_template, request, Blueprint, session, url_for
from foodapp.dbcon.db import conn
import psycopg2, psycopg2.extras

main = Blueprint('main', __name__)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
@main.route("/")
def home():
    
    if "cart" in session.keys():
        pass
    else:
        session["cart"] = []
    return render_template('home.html')


@main.route('/cart')
def menu_cart():
    products, grand_total, grand_total_plus_shipping, quantity_total = handle_cart()

    return render_template('cart.html', products=products, grand_total=grand_total, grand_total_plus_shipping=grand_total_plus_shipping, quantity_total=quantity_total)

import re
from tkinter import E
from flask import flash,redirect, render_template, request, Blueprint, session, url_for
from foodapp.dbcon.db import conn
import psycopg2, psycopg2.extras

main = Blueprint('main', __name__)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
@main.route("/")
def home():
    
    return render_template('home.html')


@main.route('/cart')
def menu_cart():
    

    return render_template('cart.html')









 






