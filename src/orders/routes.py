from src.dbcon.db import conn
from flask import render_template, request, Blueprint
from flask import Blueprint, flash, jsonify, render_template, request


orders = Blueprint('orders', __name__, url_prefix='/orders')




@orders.route('/', methods= ['GET'])
def get_all_orders():
  return render_template('all-orders.html') 

@orders.route('/single', methods= ['GET'])
def user_order():
  return render_template('user-order.html') 



