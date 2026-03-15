"""Main routes for the application (landing, world, universe pages)."""

from flask import Blueprint, render_template, jsonify, request
from app.data import (
    get_all_universes,
    get_universe_by_id,
    get_characters_by_universe,
    get_categories_by_universe,
    get_category_characters
)

# Create Blueprint
main_bp = Blueprint('main', __name__)


@main_bp.route("/")
def home():
    """Landing page."""
    universes = get_all_universes()
    return render_template('landing.html', universes=universes)


@main_bp.route("/world")
def world():
    """World page showing all universes."""
    universes = get_all_universes()
    return render_template('world.html', universes=universes)


@main_bp.route("/universe/<universe_id>")
def universe(universe_id):
    """Universe detail page showing all categories."""
    universe = get_universe_by_id(universe_id)
    if not universe:
        return render_template('error.html', message="Universe not found"), 404
    
    categories = get_categories_by_universe(universe_id)
    characters = get_characters_by_universe(universe_id)
    
    return render_template(
        'universe.html',
        universe=universe,
        categories=categories,
        characters=characters
    )


@main_bp.route("/universe/<universe_id>/category/<category_id>")
def category(universe_id, category_id):
    """Category page showing characters in a specific category."""
    universe = get_universe_by_id(universe_id)
    if not universe:
        return render_template('error.html', message="Universe not found"), 404
    
    characters = get_category_characters(universe_id, category_id)
    categories = get_categories_by_universe(universe_id)
    
    # Find current category
    current_category = None
    for cat in categories:
        if cat['id'] == category_id:
            current_category = cat
            break
    
    return render_template(
        'hero.html',
        universe=universe,
        category=current_category,
        categories=categories,
        characters=characters
    )


@main_bp.route("/timeline")
def timeline():
    """Timeline page showing Marvel movie chronology."""
    universes = get_all_universes()
    return render_template('timeline.html', universes=universes)


@main_bp.route("/achievements")
def achievements():
    """Achievements page."""
    universes = get_all_universes()
    return render_template('achievements.html', universes=universes)


@main_bp.route("/recommendations")
def recommendations():
    """Recommendations page."""
    universes = get_all_universes()
    return render_template('recommendations.html', universes=universes)


@main_bp.route("/trending")
def trending():
    """Trending characters page."""
    universes = get_all_universes()
    return render_template('trending.html', universes=universes)


@main_bp.route("/world-map")
def world_map():
    """Interactive world map page."""
    universes = get_all_universes()
    return render_template('world_map.html', universes=universes)


@main_bp.route("/api/universes")
def api_get_universes():
    """API endpoint to get all universes."""
    universes = get_all_universes()
    return jsonify(universes)


@main_bp.route("/api/universe/<universe_id>")
def api_get_universe(universe_id):
    """API endpoint to get universe details."""
    universe = get_universe_by_id(universe_id)
    if not universe:
        return jsonify({"error": "Universe not found"}), 404
    
    categories = get_categories_by_universe(universe_id)
    characters = get_characters_by_universe(universe_id)
    
    return jsonify({
        "universe": universe,
        "categories": categories,
        "character_count": len(characters)
    })
