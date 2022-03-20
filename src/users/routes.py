from src.dbcon.db import conn
from flask import render_template, request, Blueprint
from flask import Blueprint, flash, jsonify, render_template, request
import psycopg2.extras
from flask_jwt_extended import get_jwt_identity

users = Blueprint('users', __name__, url_prefix='/users')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#all users endpoint
@users.route("/", methods=['GET'])
def all_users():
    #fetching all users
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template('users.html', users=users)
 
 
#place an order for food and view orders  
@users.route('/orders', methods= ['GET',"POST"])
def get_all_orders():
  if request.method == 'POST':
     food_id = request.args['food_name']
     user_id = request.args['food_description']
     total_cost = request.args['food_price']
     order_status = request.args['image_url']
     quantity = request.args['image_url']
     
     #creating a new order   
     cur.execute('INSERT INTO orders (food_id,user_id,total_cost,order_status,quantity) VALUES (%s,%s,%s,%s,%s)', (food_id,user_id,total_cost,order_status,quantity))
     conn.commit()
     flash('You successfully made an order','success')
     
  return render_template('all-orders.html') 

 
#getting a specific user order history
@users.route('/<int:id>', methods= ['GET'])
def get_user_order_history(id):
  id = get_jwt_identity
  cur.execute('SELECT * FROM orders WHERE id = %(id)s',{'id':id})
  return render_template('user-order.html') 



 


