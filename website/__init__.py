from flask import Flask, render_template, request

def main_page():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '754891086'

    from .views import views
   
    app.register_blueprint(views, url_prefix='/')

    return app

