from src.dbcon.db import conn
from flask import flash, redirect, render_template, request, Blueprint, url_for
import psycopg2.extras

menu = Blueprint('menu', __name__,url_prefix="/menu")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#retrieving all menu iitems
@menu.route("/", methods=['GET'])
def all_menu_products():
    #fetching all products
    cur.execute("SELECT * FROM menu_items")
    menu_items = cur.fetchall()

    return render_template('all-menu-items.html', menu_items= menu_items)

@menu.route("/single", methods=['GET'])
def single_menu_item():
   
    return render_template('single-product.html')

#creating menu-item
@menu.route("/create", methods=['GET',"POST"])
def new_menu_item():
    if request.method == "POST":
        food_name = request.form['food_name']
        food_description = request.form['food_description']
        food_price = request.form['food_price']
        image_url = request.form['image_url']
        food_stock_quantity = request.form['food_stock_quantity']
       
        #inserting values into the menu_table
        cur.execute("INSERT INTO menu_items (food_name,food_description,food_price,image_url,food_stock_quantity) VALUES (%s,%s,%s,%s,%s)", (food_name,food_description,food_price,image_url,food_stock_quantity))
        conn.commit()
     
        flash("New menu item added successfully!!",'success')
        return redirect(url_for('admin.admin_dashboard'))
   
    return render_template('admin-dashboard.html')

#editin menu-item
@menu.route("/edit/<id>", methods=['POST','GET'])
def edit_menu_items(id):
   
    #obtaining menu id
    cur.execute("SELECT * FROM menu_items WHERE id = %(id)s", {'id':id})
    data = cur.fetchall()
    cur.close()
    print(data['id'])
     
   
    return render_template('admin-edit-food.html',food = data['id'])

@menu.route("/update/<int:id>", methods=['POST'])
def update_menu_items(id):
   if request.method == "POST":
     food_name = request.form['food_name']
     food_description = request.form['food_description']
     food_price = request.form['food_price']
     image_url = request.form['image_url']
     food_stock_quantity = request.form['food_stock__quantity']
    
     cur.execute("""
     
       UPDATE menu_items
       SET food_name = %s,
       food_description = %s,
       food_price = %s,
       image_url = %s,
       food_stock_quantity = %s
       
       WHERE id = %s 
     """,
     
         (food_name,food_description,food_price,image_url,food_stock_quantity)        
                 )
     conn.commit()
     flash('Food Item updated successfuly!','success')
    
     return redirect(url_for('admin.admin_dashboard'))
 
@menu.route("/delete/<string:id>", methods=['DELETE'])
def delete_menu_item(id):
 
     cur.execute("DELETE FROM menu_items WHERE id = {0}".format(id))
     conn.commit()
     flash('Food Item deleted successfuly!','success')
    
     return redirect(url_for('admin.admin_dashboard'))