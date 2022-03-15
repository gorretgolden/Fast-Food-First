import os
from flask import Flask


#Application Factory Function
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
       app.config.from_mapping(
        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    )
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    app.static_folder = 'static'
    from src.admin.routes import admin
    from src.users.routes import users
    from src.main.routes import main
    from src.menu.routes import menu
    from src.orders.routes import orders
    from src.auth.routes import auth
    #registering blueprints    
    app.register_blueprint(admin)
    app.register_blueprint(users)
    app.register_blueprint(menu)
    app.register_blueprint(main)    
    app.register_blueprint(orders)
    app.register_blueprint(auth)

    return app

