from foodapp.dbcon.db import conn
from flask import render_template, request, Blueprint
from flask import Blueprint, flash, jsonify, render_template, request
import psycopg2.extras
from flask_jwt_extended import get_jwt_identity,jwt_required

users = Blueprint('users', __name__, url_prefix='/users')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#all users endpoint
@users.route("/", methods=['GET'])
@jwt_required()
def all_users():
    #fetching all users
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    # return render_template('users.html', users=users)
    return jsonify({'users':users})
 
  
#getting a specific user 
@users.route('/<int:id>', methods= ['GET'])
@jwt_required()
def get_user(id):
  cur.execute('SELECT * FROM users WHERE id = %(id)s',{'id':id})
  user = cur.fetchone()  
  return jsonify({'user':user})
 
 

#making a food order   
@users.route('/orders', methods= ['POST','GET'])
@jwt_required()
def make_order():
  
  if request.method == "POST":
        quantity = int(request.json['quantity'])
        user_id = get_jwt_identity()
        food_id = request.json['food_id']
     
        #getting the food price and total cost
        cur.execute("SELECT food_price FROM menu_items WHERE id = %(food_id)s", {'food_id':food_id})
        food_details = cur.fetchone()
        item_food_price = food_details['food_price']
        initial_cost = 0
        total_cost = initial_cost + (quantity * item_food_price)
        
    
        #checking if food order exists
        cur.execute("SELECT * FROM orders WHERE food_id = %(food_id)s", {'food_id':food_id})
        food_order = cur.fetchone()
        
        #if order exists then return an error message
        if food_order:
              return jsonify({'error':'Food order  already exists checkout the update order endpoint to change the quantity!'})
              # flash('Food order  already exists checkout the update order endpoint to change the quantity!')   
          
        #inserting the order into the orders table if food order doesnt exist
        cur.execute("INSERT INTO orders (user_id, food_id,quantity,total_cost) VALUES (%s,%s,%s,%s)", (user_id,food_id,quantity,total_cost))
      
        conn.commit()
        flash('New order made successfully!','success')
      #   return redirect(url_for('auth.login_user'))
  return jsonify({'info':{'message':'New order placed'},'user-id':user_id,'food-id':food_id,'quantity':quantity,'food_price':item_food_price,'total_cost':total_cost})
  #return render_template('single-product.html')
  
 
#getting a specific user order history
@users.route('/<int:id>', methods= ['GET'])
@jwt_required()
def get_user_order_history(id):
  id = get_jwt_identity()
  cur.execute('SELECT * FROM orders WHERE id = %(id)s',{'id':id})
  history = cur.fetchone()
  return render_template('user-order.html','Order-history',history) 



#getting user order history for a particular user 
@users.route('<int:user_id>/orders/<int:id>', methods= ['GET'])
@jwt_required()
def user_order_history(id,user_id):
  user_id = get_jwt_identity()
  cur.execute('SELECT * FROM orders WHERE id = %(id)s AND user_id = %(user_id)s',{'id':id,'user_id':user_id})
  user_history = cur.fetchone()  
  # return render_template('user-ordered-food-history.html',user_history=user_history) 
  return jsonify({'orders_history':user_history})


 


