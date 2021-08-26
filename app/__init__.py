""""
    Author: NSMichelJ
    Github: https://github.com/NSMichelJ
    Create Date: 21/08/2021
"""

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Api

from app.todo import db, ma
from app.todo.resources import api_bp

migrate = Migrate()

def create_app(settings_module="config.default"):
    """
    create the app
    """

    app = Flask(__name__)
    app.config.from_object(settings_module)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(api_bp)

    Api(app, catch_all_404s=True)

    app.url_map.strict_slashes = False

    register_error_handlers(app)

    return app

def register_error_handlers(app):
    """
    register errors
    """
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'message': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'message': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'message': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'message': 'Not Found error'}), 404
