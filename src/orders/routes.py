from src.dbcon.db import conn
from flask import redirect, render_template, request, Blueprint, url_for
from flask import Blueprint, flash, jsonify, render_template, request
import psycopg2.extras

orders = Blueprint('orders', __name__, url_prefix='/orders')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


#getting all orders
@orders.route('/', methods= ['GET'])
def all_orders():
  cur.execute('SELECT * FROM orders')
  orders = cur.fetchall()  
  return render_template('all-orders.html',orders = orders) 


#getting a specific order
@orders.route('/<int:id>', methods= ['GET'])
def user_order(id):
  cur.execute('SELECT * FROM orders WHERE id = %(id)s',{'id':id})
  return render_template('user-order.html') 


#updating a specific order
@orders.route("/update/<int:id>", methods=['POST'])
def update_menu_items(id):
   if request.method == "POST":
     food_id = request.form['food_name']
     user_id = request.form['food_description']
     total_cost = request.form['food_price']
     order_status = request.form['image_url']
     quantity = request.form['image_url']
    
     cur.execute("""
     
       UPDATE menu_items
       SET food_name = %s,
       food_description = %s,
       food_price = %s,
       image_url = %s,
       food_stock_quantity = %s
       
       WHERE id = %s 
     """,
     
         (food_id,user_id,order_status,total_cost,quantity)        
                 )
     conn.commit()
     flash('Food Item updated successfuly!','success')
    
     return redirect(url_for('admin.admin_dashboard'))