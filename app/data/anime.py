"""Anime Universe character data."""

# Universe configuration
UNIVERSE_CONFIG = {
    "id": "anime",
    "name": "Anime Universe",
    "description": "Characters from popular anime series including Solo Leveling, Demon Slayer, and Jujutsu Kaisen.",
    "color": "#FF6B6B",
    "logo": "/static/assets/anime-logo.png"
}

# Category definitions
CATEGORIES = {
    "solo_leveling": {
        "id": "solo_leveling",
        "name": "Solo Leveling",
        "description": "The world where hunters with supernatural powers fight monsters in dungeons.",
        "icon": "sword"
    },
    "demon_slayer": {
        "id": "demon_slayer",
        "name": "Demon Slayer",
        "description": "Demon slayers fight to protect humanity from man-eating demons.",
        "icon": "flame"
    },
    "jujutsu_kaisen": {
        "id": "jujutsu_kaisen",
        "name": "Jujutsu Kaisen",
        "description": "Sorcerers fight against cursed spirits to protect the living.",
        "icon": "cursed"
    }
}

# Character data organized by category
CHARACTERS = {
    # SOLO LEVELING
    "Sung Jin-Woo": {
        "id": "sung-jin-woo",
        "name": "Sung Jin-Woo",
        "universe": "anime",
        "category": "solo_leveling",
        "real_name": "Sung Jin-Woo",
        "image": "sung-jin-woo.jpg",
        "description": "The only E-Rank Hunter who continues to level up beyond limits. Known as the Shadow Monarch.",
        "powers": [
            "Shadow Monarch Authority",
            "Infinite Leveling",
            "Shadow Army Summoning",
            "Spatial Manipulation",
            "Immense Strength",
            "Sword Mastery"
        ],
        "timeline": {
            "first_appearance": "Solo Leveling (Web Novel 2018)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Solo Leveling (Anime 2024)"
        ],
        "stats": {
            "strength": 100,
            "speed": 95,
            "intelligence": 90,
            "abilities": 100,
            "combat": 100,
            "durability": 95
        }
    },
    "Cha Hae-In": {
        "id": "cha-hae-in",
        "name": "Cha Hae-In",
        "universe": "anime",
        "category": "solo_leveling",
        "real_name": "Cha Hae-In",
        "image": "cha-hae-in.jpg",
        "description": "The strongest female hunter in Korea with exceptional swordsmanship.",
        "powers": [
            "Sword Mastery",
            "Superhuman Strength",
            "Superhuman Speed",
            "Battle Instinct",
            "Sensing Ability"
        ],
        "timeline": {
            "first_appearance": "Solo Leveling (Web Novel 2018)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Solo Leveling (Anime 2024)"
        ],
        "stats": {
            "strength": 85,
            "speed": 90,
            "intelligence": 80,
            "abilities": 85,
            "combat": 90,
            "durability": 75
        }
    },
    "Beru": {
        "id": "beru",
        "name": "Beru",
        "universe": "anime",
        "category": "solo_leveling",
        "real_name": "Beru (Shadow Monarch)",
        "image": "beru.jpg",
        "description": "The former Shadow Monarch who serves as Jinwoo's most powerful shadow.",
        "powers": [
            "Shadow Manipulation",
            "Spear Mastery",
            "Immense Strength",
            "Speed",
            "Shadow Transformation"
        ],
        "timeline": {
            "first_appearance": "Solo Leveling (Web Novel 2018)",
            "born": "Ancient Times"
        },
        "movie_appearances": [
            "Solo Leveling (Anime 2024)"
        ],
        "stats": {
            "strength": 95,
            "speed": 90,
            "intelligence": 70,
            "abilities": 85,
            "combat": 95,
            "durability": 90
        }
    },
    "Igris": {
        "id": "igris",
        "name": "Igris",
        "universe": "anime",
        "category": "solo_leveling",
        "real_name": "Igris (Ice Archer)",
        "image": "igris.jpg",
        "description": "A powerful shadow soldier with ice abilities, formerly an S-Rank hunter.",
        "powers": [
            "Ice Manipulation",
            "Archery",
            "Superhuman Strength",
            "Superhuman Speed",
            "Shadow Loyalty"
        ],
        "timeline": {
            "first_appearance": "Solo Leveling (Web Novel 2018)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Solo Leveling (Anime 2024)"
        ],
        "stats": {
            "strength": 80,
            "speed": 85,
            "intelligence": 65,
            "abilities": 80,
            "combat": 85,
            "durability": 75
        }
    },
    
    # DEMON SLAYER
    "Tanjiro Kamado": {
        "id": "tanjiro-kamado",
        "name": "Tanjiro Kamado",
        "universe": "anime",
        "category": "demon_slayer",
        "real_name": "Tanjiro Kamado",
        "image": "tanjiro-kamado.jpg",
        "description": "A kind-hearted boy who becomes a demon slayer after his family is slaughtered and his sister turns into a demon.",
        "powers": [
            "Water Breathing",
            "Total Concentration Breathing",
            "Sun Breathing (Hidden)",
            "Enhanced Senses",
            "Swordsmanship",
            "Demon Blood Symbol"
        ],
        "timeline": {
            "first_appearance": "Demon Slayer: Kimetsu no Yaiba (2016)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Demon Slayer: Mugen Train (2020)",
            "Demon Slayer: Entertainment District (2021)",
            "Demon Slayer: Swordsmith Village (2023)"
        ],
        "stats": {
            "strength": 90,
            "speed": 95,
            "intelligence": 80,
            "abilities": 90,
            "combat": 95,
            "durability": 85
        }
    },
    "Nezuko Kamado": {
        "id": "nezuko-kamado",
        "name": "Nezuko Kamado",
        "universe": "anime",
        "category": "demon_slayer",
        "real_name": "Nezuko Kamado",
        "image": "nezuko-kamado.jpg",
        "description": "Tanjiro's sister who was turned into a demon but retains her humanity.",
        "powers": [
            "Demon Transformation",
            "Bloxod Manipulation",
            "Superhuman Strength",
            "Blood Demon Art",
            "Immense Durability",
            "Self-Healing"
        ],
        "timeline": {
            "first_appearance": "Demon Slayer: Kimetsu no Yaiba (2016)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Demon Slayer: Mugen Train (2020)",
            "Demon Slayer: Entertainment District (2021)",
            "Demon Slayer: Swordsmith Village (2023)"
        ],
        "stats": {
            "strength": 85,
            "speed": 80,
            "intelligence": 50,
            "abilities": 75,
            "combat": 70,
            "durability": 95
        }
    },
    "Zenitsu Agatsuma": {
        "id": "zenitsu",
        "name": "Zenitsu Agatsuma",
        "universe": "anime",
        "category": "demon_slayer",
        "real_name": "Zenitsu Agatsuma",
        "image": "zenitsu.jpg",
        "description": "A fearful demon slayer who only appears strong when asleep, using Thunder Breathing.",
        "powers": [
            "Thunder Breathing",
            "Lightning Speed",
            "One Strike Combat",
            "Enhanced Hearing",
            "Sleep Combat"
        ],
        "timeline": {
            "first_appearance": "Demon Slayer: Kimetsu no Yaiba (2016)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Demon Slayer: Mugen Train (2020)",
            "Demon Slayer: Entertainment District (2021)",
            "Demon Slayer: Swordsmith Village (2023)"
        ],
        "stats": {
            "strength": 70,
            "speed": 100,
            "intelligence": 60,
            "abilities": 85,
            "combat": 85,
            "durability": 60
        }
    },
    "Inosuke Hashibira": {
        "id": "inosuke",
        "name": "Inosuke Hashibira",
        "universe": "anime",
        "category": "demon_slayer",
        "real_name": "Inosuke Hashibira",
        "image": "inosuke.jpg",
        "description": "A wild boy who was raised by boars and fights with dual serrated blades.",
        "powers": [
            "Beast Breathing",
            "Superhuman Strength",
            "Enhanced Senses",
            "Fierce Combat Style",
            "High Pain Tolerance"
        ],
        "timeline": {
            "first_appearance": "Demon Slayer: Kimetsu no Yaiba (2016)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Demon Slayer: Mugen Train (2020)",
            "Demon Slayer: Entertainment District (2021)",
            "Demon Slayer: Swordsmith Village (2023)"
        ],
        "stats": {
            "strength": 90,
            "speed": 85,
            "intelligence": 45,
            "abilities": 70,
            "combat": 90,
            "durability": 80
        }
    },
    "Muzan Kibutsuji": {
        "id": "muzan",
        "name": "Muzan Kibutsuji",
        "universe": "anime",
        "category": "demon_slayer",
        "real_name": "Muzan Kibutsuji",
        "image": "muzan.jpg",
        "description": "The first demon and main antagonist who turned Nezuko into a demon.",
        "powers": [
            "Demon Regeneration",
            "Blood Demon Art",
            "Shape-Shifting",
            "Immense Strength",
            "Immortality",
            "Cellular Manipulation"
        ],
        "timeline": {
            "first_appearance": "Demon Slayer: Kimetsu no Yaiba (2016)",
            "born": "Unknown (1000+ years)"
        },
        "movie_appearances": [
            "Demon Slayer: Entertainment District (2021)",
            "Demon Slayer: Swordsmith Village (2023)"
        ],
        "stats": {
            "strength": 100,
            "speed": 95,
            "intelligence": 95,
            "abilities": 100,
            "combat": 95,
            "durability": 100
        }
    },
    
    # JUJUTSU KAISEN
    "Yuji Itadori": {
        "id": "yuji-itadori",
        "name": "Yuji Itadori",
        "universe": "anime",
        "category": "jujutsu_kaisen",
        "real_name": "Yuji Itadori",
        "image": "yuji-itadori.jpg",
        "description": "A physically gifted student who becomes the vessel for Sukuna, the King of Curses.",
        "powers": [
            "Sukuna's Vessel",
            "Cursed Energy Manipulation",
            "Divergent Fist",
            "Black Flash",
            "Enhanced Physical Abilities",
            "King of Curses Connection"
        ],
        "timeline": {
            "first_appearance": "Jujutsu Kaisen (Manga 2018)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Jujutsu Kaisen 0 (2021)"
        ],
        "stats": {
            "strength": 90,
            "speed": 85,
            "intelligence": 75,
            "abilities": 80,
            "combat": 90,
            "durability": 85
        }
    },
    "Satoru Gojo": {
        "id": "satoru-gojo",
        "name": "Satoru Gojo",
        "universe": "anime",
        "category": "jujutsu_kaisen",
        "real_name": "Satoru Gojo",
        "image": "gojo-satoru.jpg",
        "description": "The strongest jujutsu sorcerer in the world, teacher at Tokyo Metropolitan Curse Technical College.",
        "powers": [
            "Six Eyes",
            "Infinity (Domain Expansion)",
            "Cursed Energy Manipulation",
            "Teleportation",
            "Domain Expansion: Unlimited Void",
            "Reverse Cursed Technique"
        ],
        "timeline": {
            "first_appearance": "Jujutsu Kaisen (Manga 2018)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Jujutsu Kaisen 0 (2021)"
        ],
        "stats": {
            "strength": 95,
            "speed": 100,
            "intelligence": 100,
            "abilities": 100,
            "combat": 100,
            "durability": 95
        }
    },
    "Megumi Fushiguro": {
        "id": "megumi-fushiguro",
        "name": "Megumi Fushiguro",
        "universe": "anime",
        "category": "jujutsu_kaisen",
        "real_name": "Megumi Fushiguro",
        "image": "megumi-fushiguro.jpg",
        "description": "A talented jujutsu sorcerer with the ability to summon shikigami using shadows.",
        "powers": [
            "Ten Shadows Technique",
            "Shadow Summoning",
            "Chimera Shadow Garden",
            "Divine Dogs",
            "Cursed Energy Manipulation"
        ],
        "timeline": {
            "first_appearance": "Jujutsu Kaisen (Manga 2018)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Jujutsu Kaisen 0 (2021)"
        ],
        "stats": {
            "strength": 75,
            "speed": 80,
            "intelligence": 85,
            "abilities": 85,
            "combat": 80,
            "durability": 70
        }
    },
    "Nobara Kugisaki": {
        "id": "nobara-kugisaki",
        "name": "Nobara Kugisaki",
        "universe": "anime",
        "category": "jujutsu_kaisen",
        "real_name": "Nobara Kugisaki",
        "image": "nobara-kugisaki.jpg",
        "description": "A confident jujutsu sorcerer with a unique technique involving cursed dolls and nails.",
        "powers": [
            "Straw Doll Technique",
            "Cursed Energy Manipulation",
            "Hammer Combat",
            "Hair Manipulation",
            "Resonance"
        ],
        "timeline": {
            "first_appearance": "Jujutsu Kaisen (Manga 2018)",
            "born": "Unknown"
        },
        "movie_appearances": [
            "Jujutsu Kaisen 0 (2021)"
        ],
        "stats": {
            "strength": 70,
            "speed": 75,
            "intelligence": 75,
            "abilities": 80,
            "combat": 85,
            "durability": 65
        }
    },
    "Sukuna": {
        "id": "sukuna",
        "name": "Sukuna",
        "universe": "anime",
        "category": "jujutsu_kaisen",
        "real_name": "Ryomen Sukuna",
        "image": "sukuna.jpg",
        "description": "The King of Curses, a legendary ancient sorcerer with immense power.",
        "powers": [
            "King of Curses Authority",
            "Domain Expansion: Malevolent Shrine",
            "Cursed Energy Manipulation",
            "Fire Arrow",
            "Cleave",
            "Immense Strength"
        ],
        "timeline": {
            "first_appearance": "Jujutsu Kaisen (Manga 2018)",
            "born": "Ancient Times (1000+ years)"
        },
        "movie_appearances": [
            "Jujutsu Kaisen 0 (2021)"
        ],
        "stats": {
            "strength": 100,
            "speed": 95,
            "intelligence": 100,
            "abilities": 100,
            "combat": 100,
            "durability": 100
        }
    }
}


def get_all_characters():
    """Return all Anime characters as a list."""
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
