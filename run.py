"""Entry point for running the Flask application."""

import os
from app import create_app

# Get environment from environment variable or default to development
env = os.environ.get('FLASK_ENV', 'development')

# Create the application
app = create_app()

if __name__ == "__main__":
    # Run the development server
    port = int(os.environ.get('PORT', 5000))
    debug = env == 'development'
    
    print(f"Starting Marvel Fan Made in {env} mode...")
    print(f"Server running on http://localhost:{port}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
