"""Character comparison routes."""

from flask import Blueprint, render_template, jsonify, request
from app.data import get_all_characters, get_character_by_id_any_universe
from app.utils.battle import (
    calculate_win_probability,
    get_stat_percentages,
    get_power_rankings,
    get_stat_labels,
    get_stat_descriptions
)
import random

# Create Blueprint
compare_bp = Blueprint('compare', __name__)


@compare_bp.route("/compare")
def compare():
    """Character comparison page."""
    characters = get_all_characters()
    
    # Get selected characters from query params
    hero1_id = request.args.get('hero1')
    hero2_id = request.args.get('hero2')
    
    hero1 = None
    hero2 = None
    
    if hero1_id:
        hero1 = get_character_by_id_any_universe(hero1_id)
    
    if hero2_id:
        hero2 = get_character_by_id_any_universe(hero2_id)
    
    stat_labels = get_stat_labels()
    stat_descriptions = get_stat_descriptions()
    
    return render_template(
        'compare.html',
        characters=characters,
        hero1=hero1,
        hero2=hero2,
        stat_labels=stat_labels,
        stat_descriptions=stat_descriptions
    )


@compare_bp.route("/api/compare")
def api_compare():
    """API endpoint to compare two characters."""
    hero1_id = request.args.get('hero1')
    hero2_id = request.args.get('hero2')
    
    if not hero1_id or not hero2_id:
        return jsonify({'error': 'Two characters required for comparison'}), 400
    
    hero1 = get_character_by_id_any_universe(hero1_id)
    hero2 = get_character_by_id_any_universe(hero2_id)
    
    if not hero1:
        return jsonify({'error': f'Character {hero1_id} not found'}), 404
    
    if not hero2:
        return jsonify({'error': f'Character {hero2_id} not found'}), 404
    
    # Calculate win probability
    result = calculate_win_probability(
        hero1.get('stats', {}),
        hero2.get('stats', {})
    )
    
    # Get stat percentages
    percentages = get_stat_percentages(
        hero1.get('stats', {}),
        hero2.get('stats', {})
    )
    
    return jsonify({
        'hero1': {
            'id': hero1['id'],
            'name': hero1['name'],
            'universe': hero1['universe'],
            'category': hero1['category'],
            'image': hero1.get('image', ''),
            'stats': hero1.get('stats', {})
        },
        'hero2': {
            'id': hero2['id'],
            'name': hero2['name'],
            'universe': hero2['universe'],
            'category': hero2['category'],
            'image': hero2.get('image', ''),
            'stats': hero2.get('stats', {})
        },
        'comparison': result,
        'percentages': percentages
    })


@compare_bp.route("/api/battle")
def api_battle():
    """API endpoint to calculate battle winner probability."""
    hero1_id = request.args.get('hero1')
    hero2_id = request.args.get('hero2')
    
    if not hero1_id or not hero2_id:
        return jsonify({'error': 'Two characters required'}), 400
    
    hero1 = get_character_by_id_any_universe(hero1_id)
    hero2 = get_character_by_id_any_universe(hero2_id)
    
    if not hero1:
        return jsonify({'error': f'Character {hero1_id} not found'}), 404
    
    if not hero2:
        return jsonify({'error': f'Character {hero2_id} not found'}), 404
    
    result = calculate_win_probability(
        hero1.get('stats', {}),
        hero2.get('stats', {})
    )
    
    return jsonify({
        'hero1': hero1['name'],
        'hero2': hero2['name'],
        'hero1_probability': result['hero1_probability'],
        'hero2_probability': result['hero2_probability'],
        'factors': result['factors']
    })


@compare_bp.route("/api/rankings")
def api_rankings():
    """API endpoint to get character power rankings."""
    universe_id = request.args.get('universe')
    
    if universe_id:
        from app.data import get_characters_by_universe
        characters = get_characters_by_universe(universe_id)
    else:
        characters = get_all_characters()
    
    rankings = get_power_rankings(characters)
    
    return jsonify(rankings)


@compare_bp.route("/api/random-battle")
def api_random_battle():
    """API endpoint to get a random battle matchup."""
    characters = get_all_characters()
    
    if len(characters) < 2:
        return jsonify({'error': 'Not enough characters'}), 400
    
    # Pick two random characters
    hero1, hero2 = random.sample(characters, 2)
    
    result = calculate_win_probability(
        hero1.get('stats', {}),
        hero2.get('stats', {})
    )
    
    return jsonify({
        'hero1': {
            'id': hero1['id'],
            'name': hero1['name'],
            'universe': hero1['universe'],
            'image': hero1.get('image', '')
        },
        'hero2': {
            'id': hero2['id'],
            'name': hero2['name'],
            'universe': hero2['universe'],
            'image': hero2.get('image', '')
        },
        'winner_probability': result
    })
