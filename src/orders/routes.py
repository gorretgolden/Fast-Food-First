from src.dbcon.db import conn
from flask import redirect, render_template, request, Blueprint, url_for
from flask import Blueprint, flash, jsonify, render_template, request
from flask_jwt_extended import get_jwt_identity
import psycopg2.extras

orders = Blueprint('orders', __name__, url_prefix='/orders')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


#getting all orders
@orders.route('/', methods= ['GET'])
def all_orders():
  cur.execute('SELECT * FROM orders')
  orders = cur.fetchall()  
  # return render_template('all-orders.html',orders = orders) 
  return jsonify({'orders':orders})

#getting a specific order
@orders.route('/<int:id>', methods= ['GET'])
def user_order(id):
  cur.execute('SELECT * FROM orders WHERE id = %(id)s',{'id':id})
  order = cur.fetchone()
  return jsonify({'order':order})


  
#getting a specific user 
@orders.route('/<int:id>', methods= ['GET'])
def get_order(id):
  cur.execute('SELECT * FROM orders WHERE id = %(id)s',{'id':id})
  order = cur.fetchone()  
  return jsonify({'order':order})

#updating a specific order
@orders.route("/update/<int:id>", methods=['POST'])
def update_menu_items(id):
   if request.method == "POST":
     food_id = request.json['food_name']
     user_id = request.json['food_description']
     total_cost = request.json['food_price']
     order_status = request.json['image_url']
     quantity = request.json['image_url']
    
     cur.execute("""
     
       UPDATE menu_items
       SET food_name = %s,
       food_description = %s,
       food_price = %s,
       image_url = %s,
       food_stock_quantity = %s
       
       WHERE id = %s 
     """,
     
         (food_id,user_id,order_status,total_cost,quantity,id)        
                 )
     conn.commit()
     flash('Food Item updated successfuly!','success')
    
     return redirect(url_for('admin.admin_dashboard'))
   
@orders.route('/create', methods= ['POST','GET'])
def make_order():
  
  if request.method == "POST":
        status = request.json['status']
        quantity = request.json['quantity']
        user_id = get_jwt_identity()
        food_id = request.json['food_id']
        total_cost = request.json['total_cost']
       
        
        
        #checking if email exists
        email_exists = cur.execute("SELECT email FROM users WHERE email = %(email)s", {'email':email})
        if email_exists:
              flash('Email address already exists!')
          
         #checking if username exists
        username_exists = cur.execute("SELECT username FROM users WHERE username = %(username)s", {'username':username})
        if username_exists:
              flash('Username already in use!')      
          
          
       #checking if phonenumber exists
        phone_number_exists = cur.execute("SELECT phone_number FROM users WHERE phone_number = %(phone_number)s", {'phone_number':phone_number})
        if phone_number_exists:
              flash('Phone number already in use!')     
        #do passwords match
        if password1!=password2:
              flash("Passwords don\t match!",'error')
        
        if len(password1) < 4:
          flash("Password is too short")  
        
        #username alphabetic
        if username.isalpha():
          flash('Username must be alphabetic')  
          
         #validate email
        if not validators.email(email):
          flash('Please enter a valid email address')      
        
        #creating a hashed password in the database
        hashed_password = generate_password_hash(password1,method="sha256")
        
        #inserting values
        cur.execute("INSERT INTO users (phone_number,username,email,user_address,user_password) VALUES (%s,%s,%s,%s,%s)", (phone_number,username,email,address,hashed_password))
        conn.commit()
      #   flash('New user added successfully!','success')
      #   return redirect(url_for('auth.login_user'))
  return jsonify({'name':username,'email':email,'phone':phone_number,'pasword':hashed_password})
