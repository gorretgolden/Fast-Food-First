from src.dbcon.db import conn
from flask import render_template, request, Blueprint


admin = Blueprint('admin', __name__,url_prefix="/admin")


@admin.route("/dashboard", methods=['GET'])
def admin_dashboard():
   
    return render_template('admin-dashboard.html')


# @admin.route("/food", methods=['GET'])
# def admin_food_items():
   
#     return render_template('admin-food-items.html')



