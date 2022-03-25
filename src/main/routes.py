import re
from tkinter import E
from flask import flash,redirect, render_template, request, Blueprint, session, url_for
from src.dbcon.db import conn
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





def handle_cart():
    products = []
    grand_total = 0
    index = 0
    quantity_total = 0

    for item in session['cart']:
       
        cur.execute("SELECT * FROM menu_items WHERE id=%(id)s",{'id':item['id']})
        product = cur.fetchone()
        quantity = int(item['quantity'])
        total = quantity * product.price
        grand_total += total

        quantity_total += quantity

        products.append({'id': product.id, 'name': product.food_name, 'price':  product.food_price,
                         'image': product.image_url, 'quantity': quantity, 'total': total, 'index': index})
        index += 1

    grand_total_plus_shipping = grand_total + 1000

    return products, grand_total, grand_total_plus_shipping, quantity_total


@main.route('/add-to-cart', methods=['POST'])
def add_food_to_cart():
    if 'cart' not in session:
        session['cart'] = []

    id = request.form['id']
    quantity = int(request.form['quantity'])

    session['cart'].append({'id': id, 'quantity':quantity})             
    session.modified = True

    return redirect(url_for('main.menu_cart'))

@main.route('/remove-from-cart/<index>')
def remove_from_cart(index):
    del session['cart'][int(index)]
    session.modified = True
    return redirect(url_for('main.menu_cart'))


 
