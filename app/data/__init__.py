"""Data package for character information across all universes."""

from . import marvel
from . import anime
from . import telugu


def get_all_universes():
    """Get all available universes."""
    return [
        marvel.UNIVERSE_CONFIG,
        anime.UNIVERSE_CONFIG,
        telugu.UNIVERSE_CONFIG
    ]


def get_universe_by_id(universe_id):
    """Get universe configuration by ID."""
    universes = {
        "marvel": marvel.UNIVERSE_CONFIG,
        "anime": anime.UNIVERSE_CONFIG,
        "telugu": telugu.UNIVERSE_CONFIG
    }
    return universes.get(universe_id)


def get_all_characters():
    """Get all characters from all universes."""
    return (
        marvel.get_all_characters() +
        anime.get_all_characters() +
        telugu.get_all_characters()
    )


def get_character_by_id_any_universe(character_id):
    """Search for a character across all universes by ID."""
    # Check Marvel
    character = marvel.get_character_by_id(character_id)
    if character:
        return character
    
    # Check Anime
    character = anime.get_character_by_id(character_id)
    if character:
        return character
    
    # Check Telugu
    character = telugu.get_character_by_id(character_id)
    if character:
        return character
    
    return None


def search_characters(query):
    """Search characters by name across all universes."""
    query = query.lower()
    results = []
    
    for universe_module in [marvel, anime, telugu]:
        characters = universe_module.get_all_characters()
        for character in characters:
            if query in character['name'].lower():
                results.append(character)
            elif query in character.get('description', '').lower():
                results.append(character)
    
    return results


def get_characters_by_universe(universe_id):
    """Get all characters from a specific universe."""
    if universe_id == "marvel":
        return marvel.get_all_characters()
    elif universe_id == "anime":
        return anime.get_all_characters()
    elif universe_id == "telugu":
        return telugu.get_all_characters()
    return []


def get_categories_by_universe(universe_id):
    """Get all categories for a specific universe."""
    if universe_id == "marvel":
        return marvel.get_categories()
    elif universe_id == "anime":
        return anime.get_categories()
    elif universe_id == "telugu":
        return telugu.get_categories()
    return []


def get_category_characters(universe_id, category_id):
    """Get all characters in a specific category."""
    universe_module = None
    if universe_id == "marvel":
        universe_module = marvel
    elif universe_id == "anime":
        universe_module = anime
    elif universe_id == "telugu":
        universe_module = telugu
    
    if universe_module:
        return universe_module.get_characters_by_category(category_id)
    return []
