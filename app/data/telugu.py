"""Telugu Cinema Universe character data."""

# Universe configuration
UNIVERSE_CONFIG = {
    "id": "telugu",
    "name": "Telugu Cinema Universe",
    "description": "Characters from popular Telugu films including Baahubali, RRR, Pushpa, Salaar, and Kalki.",
    "color": "#FF9933",
    "logo": "/static/assets/telugu-logo.png"
}

# Category definitions
CATEGORIES = {
    "baahubali": {
        "id": "baahubali",
        "name": "Baahubali",
        "description": "The legendary warrior who became the king of Mahishmati.",
        "icon": "crown"
    },
    "rrr": {
        "id": "rrr",
        "name": "RRR",
        "description": "Revolutionary warriors fighting against British colonial rule.",
        "icon": "flag"
    },
    "pushpa": {
        "id": "pushpa",
        "name": "Pushpa",
        "description": "A fearless smuggler who rises in the red sanders syndicate.",
        "icon": "flower"
    },
    "salaar": {
        "id": "salaar",
        "name": "Salaar",
        "description": "A powerful warrior with unmatched combat skills.",
        "icon": "sword"
    },
    "kalki": {
        "id": "kalki",
        "name": "Kalki",
        "description": "A bounty hunter in a post-apocalyptic world.",
        "icon": "target"
    }
}

# Character data organized by category
CHARACTERS = {
    # BAAHUBALI
    "Amarendra Baahubali": {
        "id": "amarendra-baahubali",
        "name": "Amarendra Baahubali",
        "universe": "telugu",
        "category": "baahubali",
        "real_name": "Amarendra Baahubali",
        "image": "amarendra-baahubali.jpg",
        "description": "The greatest warrior in Mahishmati history, known for his honor and unparalleled fighting skills.",
        "powers": [
            "Master Swordsman",
            "Superhuman Strength",
            "Leadership",
            "Tactical Genius",
            "Archery",
            "Horse Riding"
        ],
        "timeline": {
            "first_appearance": "Baahubali: The Beginning (2015)",
            "born": "Ancient India"
        },
        "movie_appearances": [
            "Baahubali: The Beginning (2015)",
            "Baahubali 2: The Conclusion (2017)"
        ],
        "stats": {
            "strength": 100,
            "speed": 90,
            "intelligence": 85,
            "abilities": 95,
            "combat": 100,
            "durability": 95
        }
    },
    "Mahendra Baahubali": {
        "id": "mahendra-baahubali",
        "name": "Mahendra Baahubali",
        "universe": "telugu",
        "category": "baahubali",
        "real_name": "Mahendra Baahubali (Shivudu)",
        "image": "mahendra-baahubali.jpg",
        "description": "The son of Amarendra Baahubali, who grows up to reclaim his throne and avenge his father.",
        "powers": [
            "Master Warrior",
            "Climbing Skills",
            "Strategic Thinking",
            "Sword Mastery",
            "Strength",
            "Courage"
        ],
        "timeline": {
            "first_appearance": "Baahubali: The Beginning (2015)",
            "born": "Ancient India"
        },
        "movie_appearances": [
            "Baahubali: The Beginning (2015)",
            "Baahubali 2: The Conclusion (2017)"
        ],
        "stats": {
            "strength": 95,
            "speed": 85,
            "intelligence": 80,
            "abilities": 85,
            "combat": 95,
            "durability": 90
        }
    },
    "Bhallaladeva": {
        "id": "bhallaladeva",
        "name": "Bhallaladeva",
        "universe": "telugu",
        "category": "baahubali",
        "real_name": "Bhallaladeva",
        "image": "bhallaladeva.jpg",
        "description": "The power-hungry warrior who becomes the tyrannical ruler of Mahishmati.",
        "powers": [
            "Superhuman Strength",
            "Master Combatant",
            "Weapon Mastery",
            "Political Manipulation",
            "Ruthlessness"
        ],
        "timeline": {
            "first_appearance": "Baahubali: The Beginning (2015)",
            "born": "Ancient India"
        },
        "movie_appearances": [
            "Baahubali: The Beginning (2015)",
            "Baahubali 2: The Conclusion (2017)"
        ],
        "stats": {
            "strength": 95,
            "speed": 80,
            "intelligence": 80,
            "abilities": 85,
            "combat": 90,
            "durability": 90
        }
    },
    "Sivagami": {
        "id": "sivagami",
        "name": "Sivagami",
        "universe": "telugu",
        "category": "baahubali",
        "real_name": "Sivagami",
        "image": "sivagami.jpg",
        "description": "The wise and powerful queen who plays a crucial role in Mahishmati's politics.",
        "powers": [
            "Political Acumen",
            "Strategic Planning",
            "Leadership",
            "Wisdom",
            "Combat Skills"
        ],
        "timeline": {
            "first_appearance": "Baahubali: The Beginning (2015)",
            "born": "Ancient India"
        },
        "movie_appearances": [
            "Baahubali: The Beginning (2015)",
            "Baahubali 2: The Conclusion (2017)"
        ],
        "stats": {
            "strength": 50,
            "speed": 45,
            "intelligence": 95,
            "abilities": 75,
            "combat": 60,
            "durability": 55
        }
    },
    
    # RRR
    "Alluri Sitarama Raju": {
        "id": "alluri-sitarama-raju",
        "name": "Alluri Sitarama Raju",
        "universe": "telugu",
        "category": "rrr",
        "real_name": "Alluri Sitarama Raju",
        "image": "alluri-sitarama-raju.jpg",
        "description": "A revolutionary leader fighting against British colonial rule in the early 1920s.",
        "powers": [
            "Revolutionary Leadership",
            "Martial Arts",
            "Tactical Planning",
            "Sword Combat",
            "Charisma",
            "Fearlessness"
        ],
        "timeline": {
            "first_appearance": "RRR (2022)",
            "born": "1897"
        },
        "movie_appearances": [
            "RRR (2022)"
        ],
        "stats": {
            "strength": 85,
            "speed": 80,
            "intelligence": 85,
            "abilities": 80,
            "combat": 90,
            "durability": 80
        }
    },
    "Komaram Bheem": {
        "id": "komaram-bheem",
        "name": "Komaram Bheem",
        "universe": "telugu",
        "category": "rrr",
        "real_name": "Komaram Bheem",
        "image": "komaram-bheem.jpg",
        "description": "A tribal warrior fighting for his people against the British.",
        "powers": [
            "Tribal Combat Skills",
            "Jungle Survival",
            "Strength",
            "Archery",
            "Leadership",
            "Spear Mastery"
        ],
        "timeline": {
            "first_appearance": "RRR (2022)",
            "born": "1900"
        },
        "movie_appearances": [
            "RRR (2022)"
        ],
        "stats": {
            "strength": 90,
            "speed": 85,
            "intelligence": 70,
            "abilities": 75,
            "combat": 95,
            "durability": 85
        }
    },
    
    # PUSHPA
    "Pushpa Raj": {
        "id": "pushpa-raj",
        "name": "Pushpa Raj",
        "universe": "telugu",
        "category": "pushpa",
        "real_name": "Pushpa Raj",
        "image": "pushpa-raj.jpg",
        "description": "A red sanders smuggler who rises to become a powerful figure in the syndicate.",
        "powers": [
            "Combat Skills",
            "Street Smarts",
            "Tactical Planning",
            "Negotiation",
            "Fearlessness",
            "Charisma"
        ],
        "timeline": {
            "first_appearance": "Pushpa: The Rise (2021)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Pushpa: The Rise (2021)",
            "Pushpa 2: The Rule (2024)"
        ],
        "stats": {
            "strength": 80,
            "speed": 75,
            "intelligence": 85,
            "abilities": 70,
            "combat": 85,
            "durability": 75
        }
    },
    "Bhanwar Singh Shekhawat": {
        "id": "bhanwar-singh",
        "name": "Bhanwar Singh Shekhawat",
        "universe": "telugu",
        "category": "pushpa",
        "real_name": "Bhanwar Singh Shekhawat",
        "image": "bhanwar-singh.jpg",
        "description": "A police officer who becomes an arch-nemesis to Pushpa Raj.",
        "powers": [
            "Police Training",
            "Investigation Skills",
            "Tactical Planning",
            "Combat Skills",
            "Determination"
        ],
        "timeline": {
            "first_appearance": "Pushpa: The Rise (2021)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Pushpa: The Rise (2021)",
            "Pushpa 2: The Rule (2024)"
        ],
        "stats": {
            "strength": 65,
            "speed": 70,
            "intelligence": 85,
            "abilities": 65,
            "combat": 75,
            "durability": 60
        }
    },
    
    # SALAAR
    "Deva": {
        "id": "deva",
        "name": "Deva",
        "universe": "telugu",
        "category": "salaar",
        "real_name": "Deva",
        "image": "deva.jpg",
        "description": "A powerful warrior who becomes the ruler of Khansaar with unmatched combat skills.",
        "powers": [
            "Master Combatant",
            "Superhuman Strength",
            "Leadership",
            "Sword Mastery",
            "Tactical Genius",
            "Invincibility"
        ],
        "timeline": {
            "first_appearance": "Salaar: Ceasefire (2023)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Salaar: Ceasefire (2023)",
            "Salaar 2 (2024)"
        ],
        "stats": {
            "strength": 100,
            "speed": 90,
            "intelligence": 85,
            "abilities": 90,
            "combat": 100,
            "durability": 95
        }
    },
    
    # KALKI
    "Bhairava": {
        "id": "bhairava",
        "name": "Bhairava",
        "universe": "telugu",
        "category": "kalki",
        "real_name": "Bhairava",
        "image": "bhairava.jpg",
        "description": "A skilled bounty hunter in the post-apocalyptic world of 2891 AD.",
        "powers": [
            "Combat Expertise",
            "Bounty Hunting Skills",
            "Weapon Mastery",
            "Survival Skills",
            "Tech Proficiency",
            "Agility"
        ],
        "timeline": {
            "first_appearance": "Kalki 2898 AD (2024)",
            "born": "2891 AD"
        },
        "movie_appearances": [
            "Kalki 2898 AD (2024)"
        ],
        "stats": {
            "strength": 85,
            "speed": 90,
            "intelligence": 80,
            "abilities": 80,
            "combat": 90,
            "durability": 80
        }
    },
    "Ashwatthama": {
        "id": "ashwatthama",
        "name": "Ashwatthama",
        "universe": "telugu",
        "category": "kalki",
        "real_name": "Ashwatthama",
        "image": "ashwatthama.jpg",
        "description": "An immortal warrior from ancient times who has survived to the future.",
        "powers": [
            "Immortality",
            "Superhuman Strength",
            "Ancient Combat Skills",
            "Regeneration",
            "Cursed Knowledge",
            "Durability"
        ],
        "timeline": {
            "first_appearance": "Kalki 2898 AD (2024)",
            "born": "Ancient India (Mahabharata Era)"
        },
        "movie_appearances": [
            "Kalki 2898 AD (2024)"
        ],
        "stats": {
            "strength": 100,
            "speed": 80,
            "intelligence": 90,
            "abilities": 95,
            "combat": 95,
            "durability": 100
        }
    }
}


def get_all_characters():
    """Return all Telugu characters as a list."""
    return list(CHARACTERS.values())


def get_character_by_id(character_id):
    """Get a character by their ID."""
    for character in CHARACTERS.values():
        if character['id'] == character_id:
            return character
    return None


def get_character_by_name(name):
    """Get a character by their name."""
    return CHARACTERS.get(name)


def get_characters_by_category(category):
    """Get all characters in a specific category."""
    return [char for char in CHARACTERS.values() if char['category'] == category]


def get_categories():
    """Return all categories."""
    return list(CATEGORIES.values())


def get_category_by_id(category_id):
    """Get a category by ID."""
    return CATEGORIES.get(category_id)


def get_universe_info():
    """Return universe configuration."""
    return UNIVERSE_CONFIG
