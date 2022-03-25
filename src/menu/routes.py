from src.dbcon.db import conn
from flask import flash, jsonify, redirect, render_template, request, Blueprint, url_for
import psycopg2.extras
from flask_jwt_extended import jwt_required

menu = Blueprint('menu', __name__,url_prefix="/menu")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#retrieving all menu iitems
@menu.route("/", methods=['GET'])

def all_menu_products():
    #fetching all products
    cur.execute("SELECT * FROM menu_items")
    items = cur.fetchall()
    return render_template('all-menu-items.html',items=items)
#   return jsonify({'menu':items})


#retrieving single menu item
@menu.route("/<int:id>", methods=['GET'])
def single_menu_item(id):
    cur.execute('SELECT * FROM menu_items WHERE id = %(id)s',{'id':id})
    item = cur.fetchone()
    return render_template('single-product.html',item = item)
    # return jsonify({'id':data['id'],'name':data['food_name'],'price':data['food_price'],'description':data['food_description'],'stock':data['food_stock_quantity']})

#creating menu-item
@menu.route("/create", methods=['GET',"POST"])
def new_menu_item():
    if request.method == "POST":
        food_name = request.json['food_name']
        food_description = request.json['food_description']
        food_price = request.json['food_price']
        image_url = request.json['image_url']
        food_stock_quantity = request.json['food_stock_quantity']
       
        #inserting values into the menu_table
        cur.execute("INSERT INTO menu_items (food_name,food_description,food_price,image_url,food_stock_quantity) VALUES (%s,%s,%s,%s,%s)", (food_name,food_description,food_price,image_url,food_stock_quantity))
        conn.commit()
        flash("New menu item added successfully!!",'success')
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('admin-dashboard.html')
    # return jsonify({'message':'new food item created','food name':food_name,'food price':food_price,'food description':food_description,'stock quantity':food_stock_quantity})


#view menu-item
# @menu.route("/<int:id>", methods=['GET'])
# def view_menu_item(id):
#     #obtaining menu id
#     cur.execute("SELECT * FROM menu_items WHERE id = %(id)s", {'id':id})
#     data = cur.fetchone()
#     return jsonify({'id':data['id'],'name':data['food_name'],'price':data['food_price'],'description':data['food_description'],'stock':data['food_stock_quantity']})

#editing menu-item
@menu.route("/edit/<id>", methods=['POST','GET'])
def edit_menu_items(id):
   
    #obtaining menu id
    cur.execute("SELECT * FROM menu_items WHERE id = %(id)s", {'id':id})
    data = cur.fetchone()
    return render_template('admin-edit-food.html',item = data)

#updating a specific menu item
@menu.route("/update/<int:id>", methods=['POST',"GET"])
def update_menu_items(id):
   if request.method == "POST":
     food_name = request.form['food_name']
     food_description = request.form['food_description']
     food_price = request.form['food_price']
     image_url = request.form['image_url']
     food_stock_quantity = request.form['food_stock_quantity']
    
     cur.execute("""
     
       UPDATE menu_items
       SET food_name = %s,
       food_description = %s,
       food_price = %s,
       image_url = %s,
       food_stock_quantity = %s WHERE id = %s 
        """,
     
         (food_name,food_description,food_price,image_url,food_stock_quantity,id)        
                 )
     conn.commit()
     flash('Food Item updated successfuly!','success')
     return redirect(url_for('admin.admin_dashboard'))
 
 
#removing a menu item 
@menu.route("/remove/<int:id>", methods=['DELETE'])
def delete_menu_item(id):
     cur.execute("DELETE FROM menu_items WHERE id = %(id)s", {'id':id})
     conn.commit()
     flash('Food Item deleted successfuly!','success')
     return redirect(url_for('admin.admin_dashboard'))