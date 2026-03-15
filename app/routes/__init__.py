"""Routes package for the application."""

from .main import main_bp
from .heroes import heroes_bp
from .compare import compare_bp
from .auth import auth_bp

__all__ = ['main_bp', 'heroes_bp', 'compare_bp', 'auth_bp']
