from src.dbcon.db import conn
from flask import render_template, request, Blueprint
from flask import Blueprint, flash, jsonify, render_template, request
import validators
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token
import psycopg2.extras
auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup', methods= ['POST','GET'])
def register_user():
  return render_template('user-sign-up.html')  


@auth.route('/login', methods= ['POST','GET'])
def login_user():
  return render_template('user-login.html')  




 


