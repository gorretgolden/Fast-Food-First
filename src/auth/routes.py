from src.dbcon.db import conn
from flask import redirect, render_template, request, Blueprint, url_for
from flask import Blueprint, flash, jsonify, render_template, request
import validators
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token
import psycopg2.extras

auth = Blueprint('auth', __name__, url_prefix='/auth')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

@auth.route('/signup', methods= ['POST','GET'])
def register_user():
  
  if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['user_address']
        password1 = request.form['user_password']
        password2 = request.form['password2']
        
        
        #checking if email exists
        # email_exists = cur.execute("SELECT * FROM users WHERE email =email ")
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
        flash('New user added successfully!','success')
        return redirect(url_for('auth.login_user'))
  return render_template('user-sign-up.html')  


@auth.route('/login', methods= ['POST','GET'])
def login_user():
      # if request.method == "POST":
      #     email = request.form['email']
      #     password = request.form['password']
      #     # user = cur.execute('SELECT FROM users WHERE email = '%s')
       
            
  return render_template('user-login.html')  




 


