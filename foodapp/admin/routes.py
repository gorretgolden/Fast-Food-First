from foodapp.dbcon.db import conn
from flask import render_template, request, Blueprint
import psycopg2.extras

admin = Blueprint('admin', __name__,url_prefix="/admin")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

@admin.route("/dashboard", methods=['GET'])
def admin_dashboard():
   
    return render_template('admin-dashboard.html')


@admin.route("/food", methods=['GET'])
def admin_food_items():
    #fetching all products
    cur.execute("SELECT * FROM menu_items")
    items = cur.fetchall()
    return render_template('admin-food-items.html', items=items)



