from src.dbcon.db import conn
from flask import render_template, request, Blueprint
from flask import Blueprint, flash, jsonify, render_template, request
# import validators
from werkzeug.security import check_password_hash,generate_password_hash
# from flask_jwt_extended import create_access_token,create_refresh_token

users = Blueprint('users', __name__, url_prefix='/users')



@users.route('/orders', methods= ['GET',"POST"])
def get_all_orders():
  return render_template('users.html') 

@users.route('/', methods= ['GET'])
def get_all_users():
  return render_template('users.html') 

@users.route('/', methods= ['GET'])
def get_user_account():
  return render_template('users.html') 


 


