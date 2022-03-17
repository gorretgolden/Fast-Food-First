from src.dbcon.db import conn
from flask import render_template, request, Blueprint
from flask import Blueprint, flash, jsonify, render_template, request
import psycopg2.extras

users = Blueprint('users', __name__, url_prefix='/users')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#all users endpoint
@users.route("/", methods=['GET'])
def all_users():
    #fetching all users
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template('users.html', users=users)
  
@users.route('/orders', methods= ['GET',"POST"])
def get_all_orders():
  return render_template('users.html') 

@users.route('/', methods= ['GET'])
def get_all_users():
  return render_template('users.html') 

@users.route('/', methods= ['GET'])
def get_user_account():
  return render_template('users.html') 


 


