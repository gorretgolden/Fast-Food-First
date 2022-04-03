from foodapp.dbcon.db import conn
from flask import redirect, render_template, request, Blueprint, url_for
from flask import Blueprint, flash, jsonify, render_template, request
from flask_jwt_extended import get_jwt_identity,jwt_required
import psycopg2.extras

#DictCursor enables us to work with requests in json format
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#defining a blueprint for the orders
orders = Blueprint('orders', __name__, url_prefix='/orders')


#getting all orders by the admin
@orders.route('/', methods= ['GET'])
def all_orders():
  cur.execute('SELECT * FROM orders')
  orders = cur.fetchall()  
  # return render_template('all-orders.html',orders = orders) 
  return jsonify({'orders':orders})


#getting a specific order for a logged in user, by admin
@orders.route('/<int:id>', methods= ['GET'])
def user_order(id):
  cur.execute('SELECT * FROM orders WHERE id = %(id)s',{'id':id})
  order = cur.fetchone()
  return jsonify({'order':order})


#updating a specific order , by an admin
@orders.route("/<int:id>", methods=['PUT'])
def update_orders(id):
   if request.method == "PUT":
     user_id = request.json['user_id']
     order_status = request.json['status']
     quantity = request.json['quantity']
     food_id = request.json['food_id']
     
    
     cur.execute("SELECT food_price FROM menu_items WHERE id = %(food_id)s", {'food_id':food_id})
     food_details = cur.fetchone()
     item_food_price = food_details['food_price']
     total_cost = quantity * item_food_price
     cur.execute("""
     
       UPDATE orders
       SET user_id = %s,
       food_id = %s,
       status = %s,
       quantity = %s,
       total_cost = %s 
       
       WHERE id = %s 
      """,
     
      (user_id,food_id,order_status,quantity,total_cost,id))
     cur.execute("SELECT (SUM(total_cost)) FROM orders WHERE user_id = %(user_id)s",{'user_id':user_id})
     grand_total = cur.fetchone() 

     cur.execute("SELECT (SUM(quantity)) FROM orders WHERE user_id = %(user_id)s",{'user_id':user_id})
     total_orders = cur.fetchone()            
     conn.commit()
       #flash('Food Order updated successfuly!','success')
    
       #return redirect(url_for('admin.admin_dashboard'))
     return jsonify({'message':'Order updated sucessfully','grand_total':grand_total,'total_orders':total_orders})
  

  #deleting a food order from the database
@orders.route("/remove/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_food_order(id):
     cur.execute("DELETE FROM orders WHERE id = %(id)s", {'id':id})
     conn.commit()
     #flash('Item deleted successfuly!','success')
     #return redirect(url_for('admin.admin_dashboard'))
     return jsonify({'message':'Order deleted sucessfully'})