from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    # from .models import User, Note

    return app
