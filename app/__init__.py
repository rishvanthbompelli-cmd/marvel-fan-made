"""Flask application factory."""

import os
from flask import Flask
from flask_cors import CORS

from .config import get_config
from .routes import main_bp, heroes_bp, compare_bp, auth_bp
from .routes.auth import init_db as init_auth_db


def create_app(config_name=None):
    """Create and configure the Flask application."""
    
    app = Flask(__name__)
    
    # Load configuration
    if config_name:
        app.config.from_object(config_name)
    else:
        config = get_config()
        app.config.from_object(config)
    
    # Configure static and template paths
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app.config['STATIC_FOLDER'] = os.path.join(base_dir, 'static')
    app.config['TEMPLATE_FOLDER'] = os.path.join(base_dir, 'templates')
    
    # Initialize Flask-CORS
    CORS(app, supports_credentials=True)
    
    # Initialize database connection (optional)
    db = None
    cursor = None
    
    try:
        import mysql.connector
        db = mysql.connector.connect(
            host=app.config.get('DB_HOST', 'localhost'),
            user=app.config.get('DB_USER', 'root'),
            password=app.config.get('DB_PASSWORD', 'sura123'),
            database=app.config.get('DB_NAME', 'otp_login')
        )
        cursor = db.cursor()
        
        # Initialize auth blueprint with database connection
        init_auth_db(db, cursor)
    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Running without database (session-based auth only)")
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(heroes_bp)
    app.register_blueprint(compare_bp)
    app.register_blueprint(auth_bp)
    
    # Add custom template filters
    @app.template_filter('slugify')
    def slugify(text):
        """Convert text to URL-friendly slug."""
        import re
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-')
    
    @app.template_filter('get_image')
    def get_image(hero_name):
        """Get image filename for a hero."""
        hero_key = hero_name.lower().replace(' ', '-')
        mapping = {
            "iron-man": "Iron-Man.jpg",
            "captain-america": "captain america.jpg",
            "black-widow": "black widow.jpg",
            "scarlet-witch": "scarlet witch.jpg",
            "spider-man": "spider-man.jpg",
            "doctor-strange": "doctor strange.jpg",
            "black-panther": "black panther.jpg",
            "star-lord": "star-lord.jpg",
            "winter-soldier": "winter soldier.jpg",
            "war-machine": "war machine.jpg",
            "ant-man": "ant-man.jpg",
            "green-goblin": "green goblin.jpg",
            "doctor-octopus": "doctor octopus.jpg",
            "professor-x": "professor x.jpg",
            "captain-marvel": "captain marvel.jpg",
        }
        return mapping.get(hero_key, f"{hero_key}.jpg")
    
    @app.context_processor
    def inject_universes():
        """Make universe data available to all templates."""
        from app.data import get_all_universes
        return {
            'universes': get_all_universes()
        }
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
    
    return app
