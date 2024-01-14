from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsadasdfv4rfewf'

    from .views import views
    from .auth import auth

    # url_prefix means we can set up a prefix e.g. apple so that every route in the views
    # file will start with apple in our website (www.gordon.com/apple/view1)
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(auth, url_prefix='/')


    return app

