"""Hero-related routes for character details and search."""

from flask import Blueprint, render_template, jsonify, request, session
from app.data import (
    get_all_characters,
    get_character_by_id_any_universe,
    get_characters_by_universe,
    get_categories_by_universe,
    get_category_characters,
    search_characters,
    get_universe_by_id
)
import re

# Create Blueprint
heroes_bp = Blueprint('heroes', __name__)


# Hero name to image mapping (for backward compatibility)
HERO_IMAGE_MAP = {
    "ant-man": "ant-man.jpg",
    "black panther": "black panther.jpg",
    "black widow": "black widow.jpg",
    "captain america": "captain america.jpg",
    "captain marvel": "captain marvel.jpg",
    "deadpool": "deapool.jpg",
    "doctor octopus": "doctor octopus.jpg",
    "doctor strange": "doctor strange.jpg",
    "drax": "drax.jpg",
    "falcon": "falcon.jpg",
    "gamora": "gamora.jpg",
    "green goblin": "green goblin.jpg",
    "groot": "groot.jpg",
    "hawkeye": "hawkeye.jpg",
    "hulk": "hulk.jpg",
    "iron man": "Iron-Man.jpg",
    "loki": "loki.jpg",
    "magneto": "magneto.jpg",
    "mantis": "mantis.jpg",
    "nebula": "nebula.jpg",
    "professor x": "professor x.jpg",
    "quicksilver": "quicksilver.jpg",
    "rocket": "rocket.jpg",
    "scarlet witch": "scarlet witch.jpg",
    "spider-man": "spider-man.jpg",
    "star-lord": "star-lord.jpg",
    "storm": "storm.jpg",
    "thanos": "thanos.jpg",
    "thor": "thor.jpg",
    "ultron": "ultron.jpg",
    "venom": "venom.jpg",
    "vision": "vision.jpg",
    "war machine": "war machine.jpg",
    "wasp": "wasp.jpg",
    "winter soldier": "winter soldier.jpg",
    "wolverine": "wolverine.jpg",
}

# Hero slug to display name mapping
HERO_SLUG_MAP = {
    "iron-man": "Iron Man",
    "captain-america": "Captain America",
    "thor": "Thor",
    "hulk": "Hulk",
    "black-widow": "Black Widow",
    "hawkeye": "Hawkeye",
    "scarlet-witch": "Scarlet Witch",
    "vision": "Vision",
    "spider-man": "Spider-Man",
    "doctor-strange": "Doctor Strange",
    "black-panther": "Black Panther",
    "thanos": "Thanos",
    "loki": "Loki",
    "deadpool": "Deadpool",
    "wolverine": "Wolverine",
    "star-lord": "Star-Lord",
    "gamora": "Gamora",
    "rocket": "Rocket",
    "groot": "Groot",
    "falcon": "Falcon",
    "winter-soldier": "Winter Soldier",
    "war-machine": "War Machine",
    "ant-man": "Ant-Man",
    "wasp": "Wasp",
    "mantis": "Mantis",
    "nebula": "Nebula",
    "drax": "Drax",
    "venom": "Venom",
    "quicksilver": "Quicksilver",
    "storm": "Storm",
    "magneto": "Magneto",
    "ultron": "Ultron",
    "green-goblin": "Green Goblin",
    "doctor-octopus": "Doctor Octopus",
    "professor-x": "Professor X",
    "captain-marvel": "Captain Marvel",
    # Anime characters
    "gojo-satoru": "Satoru Gojo",
    "yuji-itadori": "Yuji Itadori",
    "sung-jin-woo": "Sung Jin-Woo",
    "tanjiro-kamado": "Tanjiro Kamado",
    "nezuko-kamado": "Nezuko Kamado",
    "zenitsu": "Zenitsu",
    "inosuke": "Inosuke",
    "sukuna": "Sukuna",
    "megumi-fushiguro": "Megumi Fushiguro",
    "nobara-kugisaki": "Nobara Kugisaki",
    # Telugu characters
    "amarendra-baahubali": "Amarendra Baahubali",
    "mahendra-baahubali": "Mahendra Baahubali",
    "bhallaladeva": "Bhallaladeva",
    "sivagami": "Sivagami",
    "alluri-sitarama-raju": "Alluri Sitarama Raju",
    "komaram-bheem": "Komaram Bheem",
    "pushpa-raj": "Pushpa Raj",
    "bhanwar-singh": "Bhanwar Singh Shekhawat",
    "deva": "Deva",
    "bhairava": "Bhairava",
    "ashwatthama": "Ashwatthama",
}


def get_image_for_hero(hero_name):
    """Get image filename for a hero with case-insensitive matching."""
    # Try various key formats for case-insensitive matching
    hero_key = hero_name.lower()
    
    # First try: direct lowercase match
    if hero_key in HERO_IMAGE_MAP:
        image_name = HERO_IMAGE_MAP[hero_key]
    else:
        # Second try: replace spaces with hyphens
        hero_key_hyphen = hero_key.replace(' ', '-')
        if hero_key_hyphen in HERO_IMAGE_MAP:
            image_name = HERO_IMAGE_MAP[hero_key_hyphen]
        else:
            # Third try: replace hyphens with spaces
            hero_key_space = hero_key.replace('-', ' ')
            if hero_key_space in HERO_IMAGE_MAP:
                image_name = HERO_IMAGE_MAP[hero_key_space]
            else:
                # Fallback: use the hero name with lowercase and hyphen replacement
                image_name = f"{hero_key.replace(' ', '-')}.jpg"
    
    # DEBUG: Log the image path being generated
    print(f"[DEBUG] get_image_for_hero('{hero_name}') -> image_name='{image_name}'")
    # Return full static path
    return f"/static/assets/{image_name}"


@heroes_bp.route("/hero")
def hero():
    """Hero listing page."""
    # Get optional universe filter
    universe_id = request.args.get('universe')
    
    if universe_id:
        characters = get_characters_by_universe(universe_id)
    else:
        characters = get_all_characters()
    
    universes = get_all_universes()
    
    return render_template(
        'hero.html',
        characters=characters,
        universes=universes,
        selected_universe=universe_id
    )


@heroes_bp.route("/hero/<hero_identifier>")
def hero_detail(hero_identifier):
    """Hero detail page - accepts both ID and name."""
    # First try to find by ID
    character = get_character_by_id_any_universe(hero_identifier)
    
    # If not found by ID, try to find by name
    if not character:
        character = get_character_by_id_any_universe(hero_identifier.replace('-', ' ').lower())
    
    # If still not found, try slug mapping
    if not character:
        display_name = HERO_SLUG_MAP.get(hero_identifier)
        if display_name:
            # Search through all characters
            all_chars = get_all_characters()
            for char in all_chars:
                if char['name'].lower() == display_name.lower():
                    character = char
                    break
    
    if not character:
        return render_template('error.html', message="Character not found"), 404
    
    # Get universe and category info
    universe = get_universe_by_id(character['universe'])
    categories = get_categories_by_universe(character['universe'])
    
    # Get image
    image = get_image_for_hero(character['name'])
    # DEBUG: Log what we're passing to template
    print(f"[DEBUG] hero_detail rendering - character['name']={character['name']}, image='{image}', hero_image variable will be: {image}")
    
    # Check if character is in user's favorites
    is_favorite = False
    if 'favorites' in session:
        favorites = session.get('favorites', [])
        is_favorite = character['id'] in favorites
    
    return render_template(
        'hero_detail.html',
        character=character,
        universe=universe,
        categories=categories,
        image=image,
        hero_image=image,  # DEBUG: Also pass as hero_image to match template
        is_favorite=is_favorite
    )


@heroes_bp.route("/search-heroes")
def search_heroes():
    """Search heroes by name or description."""
    query = request.args.get('q', '').strip()
    
    if not query:
        return jsonify([])
    
    # Search through all characters
    results = search_characters(query)
    
    # Format results
    formatted_results = []
    for char in results[:20]:  # Limit to 20 results
        formatted_results.append({
            'id': char['id'],
            'name': char['name'],
            'universe': char['universe'],
            'category': char['category'],
            'image': get_image_for_hero(char['name']),
            'description': char.get('description', '')[:100]
        })
    
    return jsonify(formatted_results)


@heroes_bp.route("/category-heroes/<universe>/<category>")
def get_category_heroes(universe, category):
    """Get heroes by category from a specific universe."""
    # If category is 'all', return all characters from the universe
    if category == 'all':
        characters = get_characters_by_universe(universe)
    else:
        characters = get_category_characters(universe, category)
    
    return jsonify([
        {
            'id': char['id'],
            'name': char['name'],
            'image': get_image_for_hero(char['name']),
            'description': char.get('description', '')
        }
        for char in characters
    ])


@heroes_bp.route("/hero-movies/<hero_name>")
def get_hero_movies(hero_name):
    """Get movie appearances for a hero (legacy endpoint)."""
    character = get_character_by_id_any_universe(hero_name)
    
    if not character:
        # Try slug mapping
        display_name = HERO_SLUG_MAP.get(hero_name)
        if display_name:
            all_chars = get_all_characters()
            for char in all_chars:
                if char['name'].lower() == display_name.lower():
                    character = char
                    break
    
    if not character:
        return jsonify({'error': 'Character not found'}), 404
    
    return jsonify({
        'name': character['name'],
        'movies': character.get('movie_appearances', [])
    })


@heroes_bp.route("/api/characters")
def api_get_characters():
    """API endpoint to get all characters."""
    universe_id = request.args.get('universe')
    
    if universe_id:
        characters = get_characters_by_universe(universe_id)
    else:
        characters = get_all_characters()
    
    # Format for API
    formatted = []
    for char in characters:
        formatted.append({
            'id': char['id'],
            'name': char['name'],
            'universe': char['universe'],
            'category': char['category'],
            'image': get_image_for_hero(char['name']),
            'description': char.get('description', '')
        })
    
    return jsonify(formatted)


@heroes_bp.route("/api/character/<character_id>")
def api_get_character(character_id):
    """API endpoint to get a single character."""
    character = get_character_by_id_any_universe(character_id)
    
    if not character:
        return jsonify({'error': 'Character not found'}), 404
    
    return jsonify(character)
