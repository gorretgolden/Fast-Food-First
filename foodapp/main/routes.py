from flask import flash, jsonify,redirect, render_template, request, Blueprint, session, url_for
from foodapp.dbcon.db import conn
import psycopg2, psycopg2.extras
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

main = Blueprint('main', __name__)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
@main.route("/")
def home():
    
    # return jsonify({'message':'Welcome'})
    return render_template('main.html')


@main.route('/cart')
def menu_cart():
    

    return render_template('cart.html')



@main.route("/api/spec")
def spec():
  swag = swagger(app, prefix='/api')
  swag['info']['base'] = "http://localhost:5000"
  swag['info']['version'] = "1.0"
  swag['info']['title'] = "Fast Food First API"
  return jsonify(swag)
swaggerui_blueprint = get_swaggerui_blueprint('/api/docs', '/api/spec', config={'app_name': "Fast Food First API"})







 






