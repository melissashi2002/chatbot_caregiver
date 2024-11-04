from flask import Flask
from flask_mail import Mail

mail = Mail()  # Create a Mail instance outside the create_app to use it across your application

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    # Configuring mail settings
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'jiayueshi1207@gmail.com'
    app.config['MAIL_PASSWORD'] = 'xmac vykf wrba hjba'
    #app.config['MAIL_DEFAULT_SENDER'] = 'mshi24@illinois.edu'  # Optional: Default sender

    mail.init_app(app)  # Initialize the Mail object with app

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # Optional: If you have other blueprints for handling different routes
    # app.register_blueprint(views, url_prefix='/with')
    # app.register_blueprint(views, url_prefix='/without')
    # app.register_blueprint(chatbot_with, url_prefix='/with')
    # app.register_blueprint(chatbot_without, url_prefix='/without')

    return app



