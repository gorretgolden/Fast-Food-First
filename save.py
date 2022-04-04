# @users.route('/orders', methods= ['GET',"POST"])
# def get_all_orders():
#   if request.method == 'POST':
#      food_id = request.args['food_name']
#      user_id = request.args['food_description']
#      total_cost = request.args['food_price']
#      order_status = request.args['image_url']
#      quantity = request.args['image_url']
     
#      #creating a new order   
#      cur.execute('INSERT INTO orders (food_id,user_id,total_cost,order_status,quantity) VALUES (%s,%s,%s,%s,%s)', (food_id,user_id,total_cost,order_status,quantity))
#      conn.commit()
#      flash('You successfully made an order','success')
     
#   return render_template('all-orders.html') 
   #updating the total cost
        # cur.execute("UPDATE orders SET total_cost = %(quantity)s * %(item_food_price)s ", {'quantity':quantity,'item_food_price':item_food_price})
          #update the quantity of  the order
        
        # cur.execute("UPDATE orders SET quantity = %(quantity)s ", {'quantity':quantity})
          #update the total cost of  the order
        # cur.execute(""""
        #             UPDATE orders
        #             SET orders.total_cost = (%(quantity)s * %(item_food_price)s)
        #             """, (int(quantity),("SELECT food_price  FROM menu_items WHERE id = %(foodId)",({'id':food_id}))))  
# @main.route('/add', methods=['POST','GET'])
# def add_food_to_cart():
   #b6e565     bfde8a
#    try:
#        _quantity = int(request.form['quantity'])
#        id  = request.form['id']
       
#        if request.method == 'POST': 
       
#            cur.execute("SELECT * FROM menu_items WHERE id=%(id)s",{'id':id})
#            row = cur.fetchone()
#            itemArray = { row['id'] : {'name' : row['food_name'], 'quantity' : _quantity, 'price' : row['food_price'], 'image' : row['image_url'], 'total_price': _quantity * row['food_price']}}
           
#            all_total_price = 0
#            all_total_quantity = 0
           
#            session.modified = True
           
#            if 'cart_item' in session:
#                if row['id'] in session['cart_item']:
#                    for key, value in session['cart_item'].items():
#                        if row['id'] == key:
#                            old_quantity = session['cart_item'][key]['quantity']
#                            total_quantity = old_quantity + _quantity
#                            session['cart_item'][key]['quantity'] = total_quantity
#                            session['cart_item'][key]['total_price'] = total_quantity * row['food_price']
                           
#                else:
#                     session['cart_item'] = array_merge(session['cart_item'], itemArray)
                    
                
#                for key, value in session['cart_item'].items():
#                     individual_quantity = int(session['cart_item'][key]['quantity'])
#                     individual_price = float(session['cart_item'][key]['total_price'])
#                     all_total_quantity = all_total_quantity + individual_quantity
#                     all_total_price = all_total_price + individual_price
                    
#            else:
#                session['cart_item'] = itemArray
#                all_total_quantity = all_total_quantity + _quantity
#                all_total_price = all_total_price + _quantity * row['food_price']
#                session['all_total_price'] = all_total_price    
#                session['all_total_quantity'] = all_total_quantity
               
              
            
           
            
#            return redirect(url_for('main.menu_cart'))
#        else:
#            flash('Item not added to cart')
#    except Exception as e:
#        print(e)   
          
    

# def array_merge( first_array, second_array ):
#     if isinstance( first_array, list ) and isinstance( second_array, list ):
#         return first_array + second_array
    
#     elif isinstance( first_array, dict ) and isinstance( second_array, dict ):
#         return dict( list( first_array.items() ) + list( second_array.items() ) )
    
#     elif isinstance( first_array, set ) and isinstance( second_array, set ):
#         return first_array.union( second_array )
    
#     return False		

        
    
# @main.route('/empty')
# def empty_cart():
#     try:
#         session.clear()
#         return redirect(url_for('main.all_menu_products'))
#     except Exception as e:
#         print(e)
# def handle_cart():
#     products = []
#     grand_total = 0
#     index = 0
#     quantity_total = 0

#     for item in session['cart']:
       
#         cur.execute("SELECT * FROM menu_items WHERE id=%(id)s",{'id':item['id']})
#         product = cur.fetchone()
#         quantity = int(item['quantity'])
#         total = quantity * product.price
#         grand_total += total

#         quantity_total += quantity

#         products.append({'id': product.id, 'name': product.food_name, 'price':  product.food_price,
#                          'image': product.image_url, 'quantity': quantity, 'total': total, 'index': index})
#         index += 1

#     grand_total_plus_shipping = grand_total + 1000

#     return products, grand_total, grand_total_plus_shipping, quantity_total


# @main.route('/add-to-cart', methods=['POST'])
# def add_food_to_cart():
#     if 'cart' not in session:
#         session['cart'] = []

#     id = request.form['id']
#     quantity = int(request.form['quantity'])

#     session['cart'].append({'id': id, 'quantity':quantity})             
#     session.modified = True

#     return redirect(url_for('main.menu_cart'))

# @main.route('/remove-from-cart/<index>')
# def remove_from_cart(index):
#     del session['cart'][int(index)]
#     session.modified = True
#     return redirect(url_for('main.menu_cart'))


 

# @main.route('/delete/<int:id>')
# def delete_product(id):
#     try:
#         all_total_price = 0
#         all_total_quantity = 0
#         session.modified = True
        
#         for item in session['cart_item'].items():
#             if item[0] == id:				
#                 session['cart_item'].pop(item[0], None)
#                 if 'cart_item' in session:
#                     for key, value in session['cart_item'].items():
#                         individual_quantity = int(session['cart_item'][key]['quantity'])
#                         individual_price = float(session['cart_item'][key]['total_price'])
#                         all_total_quantity = all_total_quantity + individual_quantity
#                         all_total_price = all_total_price + individual_price
#                 break
        
#         if all_total_quantity == 0:
#             session.clear()
#         else:
#             session['all_total_quantity'] = all_total_quantity
#             session['all_total_price'] = all_total_price
        

#         return redirect(url_for('.products'))
#     except Exception as e:
#         print(e)
        
# @main.route('/add-to-cart', methods=['POST'])
# def add_food_to_cart():
#     if 'cart' not in session:
#         session['cart'] = []

#     id = request.form['id']
#     quantity = int(request.form['quantity'])

#     session['cart'].append({'id': id, 'quantity':quantity})             
#     session.modified = True

#     return redirect(url_for('main.menu_cart'))