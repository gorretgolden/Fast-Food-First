from foodapp.dbcon.db import conn
from flask import render_template, request, Blueprint
from flask import Blueprint, flash, jsonify, render_template, request
import psycopg2.extras
from flask_jwt_extended import get_jwt_identity,jwt_required

users = Blueprint('users', __name__, url_prefix='/users')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#all users endpoint
@users.route("/", methods=['GET'])
def all_users():
    #fetching all users
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    # return render_template('users.html', users=users)
    return jsonify({'users':users})
 
  
#getting a specific user 
@users.route('/<int:id>', methods= ['GET'])
def get_user(id):
  cur.execute('SELECT * FROM users WHERE id = %(id)s',{'id':id})
  user = cur.fetchone()  
  return jsonify({'user':user})
 
 

#making a food order   
@users.route('/orders', methods= ['POST','GET'])
@jwt_required()
def make_order():
  
  if request.method == "POST":
        quantity = request.json['quantity']
        user_id = get_jwt_identity()
        food_id = request.json['food_id']
        
     
        #getting the food price and total cost
        #getting food price
       
    
        #checking if food order exists
        cur.execute("SELECT * FROM orders WHERE food_id = %(food_id)s", {'food_id':food_id})
        food_order = cur.fetchone()
        
        #if order exists then return an error message
        if food_order:
              return jsonify({'error':'Food order  already exists checkout the update order endpoint to change the quantity!'})
              # flash('Food order  already exists checkout the update order endpoint to change the quantity!')   
         
        
        #inserting the order into the orders table if food order doesnt exist
        if food_id:
          cur.execute("SELECT * FROM menu_items WHERE id = %(food_id)s", {'food_id':food_id})
          item_food_price = cur.fetchone()
          total_cost = quantity * item_food_price['food_price']
          
          # new_total_cost = int(grand_total) + int(item_food_price['food_price'])
         
          cur.execute("INSERT INTO orders (user_id, food_id,quantity,total_cost) VALUES (%s,%s,%s,%s)", (user_id,food_id,quantity,total_cost))
          cur.execute("SELECT (SUM(total_cost)) FROM orders WHERE user_id = %(user_id)s",{'user_id':user_id})
          grand_total = cur.fetchone() 

          cur.execute("SELECT (SUM(quantity)) FROM orders WHERE user_id = %(user_id)s",{'user_id':user_id})
          total_orders = cur.fetchone()
          conn.commit()

          flash('New order made successfully!','success')
      #   return redirect(url_for('auth.login_user'))
  return jsonify({'info':{'message':'New order placed'},'user-id':user_id,'food-id':food_id,'quantity':quantity,"total_cost":total_cost,'grand_total':grand_total,"total_orders":total_orders})
  #return render_template('single-product.html')
  
 



#getting user order history for a particular user 
@users.route('/orders/<int:id>', methods= ['GET'])
@jwt_required(id)
def user_order_history(id):
  id = get_jwt_identity()

  cur.execute('SELECT * FROM orders WHERE  user_id = %(user_id)s',{'user_id':id})
  user_history = cur.fetchall() 

  cur.execute("SELECT (SUM(total_cost)) FROM orders WHERE user_id = %(user_id)s",{'user_id':id})
  grand_total = cur.fetchone() 

  cur.execute("SELECT (SUM(quantity)) FROM orders WHERE user_id = %(user_id)s",{'user_id':id})
  total_orders = cur.fetchone()

  # return render_template('user-ordered-food-history.html',user_history=user_history) 
  return jsonify({'orders_history':user_history,"grand_total":grand_total,"total_orders":total_orders})


 


