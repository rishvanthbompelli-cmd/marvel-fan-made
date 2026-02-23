from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import mysql.connector
import os
import re
import json
import random

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='/static')
CORS(app)

app.secret_key = 'marvel_secret_key_12345'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sura123",
    database="otp_login"
)
cursor = db.cursor()

# Regex patterns
email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
phone_regex = r'^\+?[\d\s-]{10,15}$'

# Hero name to image mapping (handles special cases)
HERO_IMAGE_MAP = {
    "iron man": "Iron-Man.jpg",
    "captain america": "captain america.jpg",
    "thor": "thor.jpg",
    "hulk": "hulk.jpg",
    "black widow": "black widow.jpg",
    "hawkeye": "hawkeye.jpg",
    "scarlet witch": "scarlet witch.jpg",
    "vision": "vision.jpg",
    "spider-man": "spider-man.jpg",
    "doctor strange": "doctor strange.jpg",
    "black panther": "black panther.jpg",
    "thanos": "thanos.jpg",
    "loki": "loki.jpg",
    "deadpool": "deapool.jpg",
    "wolverine": "wolverine.jpg",
    "star-lord": "star-lord.jpg",
    "gamora": "gamora.jpg",
    "rocket": "rocket.jpg",
    "groot": "groot.jpg",
    "falcon": "falcon.jpg",
    "winter soldier": "winter soldier.jpg",
    "war machine": "war machine.jpg",
    "ant-man": "ant-man.jpg",
    "wasp": "wasp.jpg",
    "mantis": "mantis.jpg",
    "nebula": "nebula.jpg",
    "drax": "drax.jpg",
    "venom": "venom.jpg",
    "quicksilver": "quicksilver.jpg",
    "storm": "storm.jpg",
    "magneto": "magneto.jpg",
    "ultron": "ultron.jpg",
    "green goblin": "green goblin.jpg",
    "doctor octopus": "doctor octopus.jpg",
    "professor x": "professor x.jpg",
    "captain marvel": "captain marvel.jpg",
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
}

HEROES_DATA = {
    "Iron Man": {
        "category": "Avengers",
        "description": "Genius, billionaire, playboy, philanthropist. The armored Avenger.",
        "movies": ["Iron Man (2008)", "Iron Man 2 (2010)", "Iron Man 3 (2013)", "The Avengers (2012)", "Avengers: Age of Ultron (2015)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)"]
    },
    "Captain America": {
        "category": "Avengers",
        "description": "The First Avenger with an unbreakable shield.",
        "movies": ["Captain America: The First Avenger (2011)", "The Avengers (2012)", "Captain America: The Winter Soldier (2014)", "Avengers: Age of Ultron (2015)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)"]
    },
    "Thor": {
        "category": "Avengers",
        "description": "God of Thunder, wielder of Mjölnir and Stormbreaker.",
        "movies": ["Thor (2011)", "The Avengers (2012)", "Thor: The Dark World (2013)", "Avengers: Age of Ultron (2015)", "Thor: Ragnarok (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Thor: Love and Thunder (2022)"]
    },
    "Hulk": {
        "category": "Avengers",
        "description": "The strongest Avenger with incredible gamma-powered strength.",
        "movies": ["The Incredible Hulk (2008)", "The Avengers (2012)", "Avengers: Age of Ultron (2015)", "Thor: Ragnarok (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "She-Hulk (2022)"]
    },
    "Black Widow": {
        "category": "Avengers",
        "description": "Master spy and assassin, Avenger team member.",
        "movies": ["Iron Man 2 (2010)", "The Avengers (2012)", "Captain America: The Winter Soldier (2014)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Black Widow (2021)"]
    },
    "Hawkeye": {
        "category": "Avengers",
        "description": "Master archer and Avenger, never misses his target.",
        "movies": ["Thor (2011)", "The Avengers (2012)", "Avengers: Age of Ultron (2015)", "Captain America: Civil War (2016)", "Avengers: Endgame (2019)", "Hawkeye (2021)"]
    },
    "Scarlet Witch": {
        "category": "Avengers",
        "description": "Powerful mutant with reality-warping abilities.",
        "movies": ["Captain America: The Winter Soldier (2015)", "Avengers: Age of Ultron (2015)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "WandaVision (2021)", "Doctor Strange in the Multiverse of Madness (2022)"]
    },
    "Vision": {
        "category": "Avengers",
        "description": "Android Avenger with the Mind Stone.",
        "movies": ["Avengers: Age of Ultron (2015)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "WandaVision (2021)"]
    },
    "Spider-Man": {
        "category": "Spider-Man",
        "description": "Friendly neighborhood superhero with spider-powers.",
        "movies": ["Spider-Man (2002)", "Spider-Man 2 (2004)", "Spider-Man 3 (2007)", "The Amazing Spider-Man (2012)", "The Amazing Spider-Man 2 (2014)", "Spider-Man: Homecoming (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Spider-Man: Far From Home (2019)", "Spider-Man: No Way Home (2021)"]
    },
    "Doctor Strange": {
        "category": "Mystic",
        "description": "Master of the Mystic Arts.",
        "movies": ["Doctor Strange (2016)", "Thor: Ragnarok (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Doctor Strange in the Multiverse of Madness (2022)"]
    },
    "Black Panther": {
        "category": "Wakanda",
        "description": "King of Wakanda, protector of the vibranium nation.",
        "movies": ["Captain America: Civil War (2016)", "Black Panther (2018)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Black Panther: Wakanda Forever (2022)"]
    },
    "Thanos": {
        "category": "Villains",
        "description": "Titan seeking the Infinity Stones for universal balance.",
        "movies": ["The Avengers (2012)", "Guardians of the Galaxy (2014)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)"]
    },
    "Loki": {
        "category": "Villains",
        "description": "God of mischief and trickster.",
        "movies": ["Thor (2011)", "The Avengers (2012)", "Thor: The Dark World (2013)", "Thor: Ragnarok (2017)", "Avengers: Endgame (2019)", "Loki (2021)"]
    },
    "Deadpool": {
        "category": "X-Men",
        "description": "Merc with a mouth, expert swordsman and marksman.",
        "movies": ["Deadpool (2016)", "Deadpool 2 (2018)", "Deadpool 3 (2024)"]
    },
    "Wolverine": {
        "category": "X-Men",
        "description": "Mutant with accelerated healing factor and adamantium claws.",
        "movies": ["X-Men (2000)", "X2: X-Men United (2003)", "X-Men: The Last Stand (2006)", "X-Men Origins: Wolverine (2009)", "The Wolverine (2013)", "X-Men: Days of Future Past (2014)", "Deadpool (2016)", "Logan (2017)"]
    },
    "Star-Lord": {
        "category": "Guardians",
        "description": "Half-human, half-celestial leader of the Guardians.",
        "movies": ["Guardians of the Galaxy (2014)", "Guardians of the Galaxy Vol. 2 (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Guardians of the Galaxy Vol. 3 (2023)"]
    },
    "Gamora": {
        "category": "Guardians",
        "description": "Adopted daughter of Thanos, deadliest woman in the galaxy.",
        "movies": ["Guardians of the Galaxy (2014)", "Guardians of the Galaxy Vol. 2 (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)"]
    },
    "Rocket": {
        "category": "Guardians",
        "description": "Genetically enhanced raccoon, master of weapons.",
        "movies": ["Guardians of the Galaxy (2014)", "Guardians of the Galaxy Vol. 2 (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Guardians of the Galaxy Vol. 3 (2023)"]
    },
    "Groot": {
        "category": "Guardians",
        "description": "Sentient tree being from the Guardians of the Galaxy.",
        "movies": ["Guardians of the Galaxy (2014)", "Guardians of the Galaxy Vol. 2 (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Guardians of the Galaxy Vol. 3 (2023)"]
    },
    "Falcon": {
        "category": "Avengers",
        "description": "Winged Avenger with exceptional aerial combat skills.",
        "movies": ["Captain America: The Winter Soldier (2014)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "The Falcon and The Winter Soldier (2021)"]
    },
    "Winter Soldier": {
        "category": "Avengers",
        "description": "Former assassin with a mechanical arm and super-soldier abilities.",
        "movies": ["Captain America: The Winter Soldier (2014)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "The Falcon and The Winter Soldier (2021)"]
    },
    "War Machine": {
        "category": "Avengers",
        "description": "U.S. Air Force colonel with advanced powered armor.",
        "movies": ["Iron Man 2 (2010)", "The Avengers (2012)", "Captain America: Civil War (2016)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)"]
    },
    "Ant-Man": {
        "category": "Avengers",
        "description": "Hero with suit that allows size manipulation.",
        "movies": ["Ant-Man (2015)", "Ant-Man and the Wasp (2018)", "Avengers: Endgame (2019)", "Ant-Man and the Wasp: Quantumania (2023)"]
    },
    "Wasp": {
        "category": "Avengers",
        "description": "Hero with similar abilities to Ant-Man plus flying capabilities.",
        "movies": ["Ant-Man (2015)", "Ant-Man and the Wasp (2018)", "Ant-Man and the Wasp: Quantumania (2023)"]
    },
    "Mantis": {
        "category": "Guardians",
        "description": "Empathic alien with plant-like abilities.",
        "movies": ["Guardians of the Galaxy Vol. 2 (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Guardians of the Galaxy Vol. 3 (2023)"]
    },
    "Nebula": {
        "category": "Guardians",
        "description": "Cybernetic alien, daughter of Thanos.",
        "movies": ["Guardians of the Galaxy (2014)", "Guardians of the Galaxy Vol. 2 (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)"]
    },
    "Drax": {
        "category": "Guardians",
        "description": "Powerful warrior seeking revenge on Thanos.",
        "movies": ["Guardians of the Galaxy (2014)", "Guardians of the Galaxy Vol. 2 (2017)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Guardians of the Galaxy Vol. 3 (2023)"]
    },
    "Captain Marvel": {
        "category": "Cosmic",
        "description": "Powerful Avenger with energy absorption abilities.",
        "movies": ["Captain Marvel (2019)", "Avengers: Endgame (2019)", "The Marvels (2023)"]
    },
}

HEROES = [
    {"id": 1, "name": "Iron Man", "category": "Avengers"},
    {"id": 2, "name": "Captain America", "category": "Avengers"},
    {"id": 3, "name": "Thor", "category": "Avengers"},
    {"id": 4, "name": "Hulk", "category": "Avengers"},
    {"id": 5, "name": "Black Widow", "category": "Avengers"},
    {"id": 6, "name": "Hawkeye", "category": "Avengers"},
    {"id": 7, "name": "Scarlet Witch", "category": "Avengers"},
    {"id": 8, "name": "Vision", "category": "Avengers"},
    {"id": 9, "name": "Spider-Man", "category": "Spider-Man"},
    {"id": 10, "name": "Doctor Strange", "category": "Mystic"},
    {"id": 11, "name": "Black Panther", "category": "Wakanda"},
    {"id": 12, "name": "Thanos", "category": "Villains"},
    {"id": 13, "name": "Loki", "category": "Villains"},
    {"id": 14, "name": "Deadpool", "category": "X-Men"},
    {"id": 15, "name": "Wolverine", "category": "X-Men"},
    {"id": 16, "name": "Star-Lord", "category": "Guardians"},
    {"id": 17, "name": "Gamora", "category": "Guardians"},
    {"id": 18, "name": "Rocket", "category": "Guardians"},
    {"id": 19, "name": "Groot", "category": "Guardians"},
    {"id": 20, "name": "Falcon", "category": "Avengers"},
    {"id": 21, "name": "Winter Soldier", "category": "Avengers"},
    {"id": 22, "name": "War Machine", "category": "Avengers"},
    {"id": 23, "name": "Ant-Man", "category": "Avengers"},
    {"id": 24, "name": "Wasp", "category": "Avengers"},
    {"id": 25, "name": "Mantis", "category": "Guardians"},
    {"id": 26, "name": "Nebula", "category": "Guardians"},
    {"id": 27, "name": "Drax", "category": "Guardians"},
    {"id": 28, "name": "Venom", "category": "Villains"},
    {"id": 29, "name": "Quicksilver", "category": "X-Men"},
    {"id": 30, "name": "Storm", "category": "X-Men"},
    {"id": 31, "name": "Magneto", "category": "Villains"},
    {"id": 32, "name": "Ultron", "category": "Villains"},
    {"id": 33, "name": "Green Goblin", "category": "Villains"},
    {"id": 34, "name": "Doctor Octopus", "category": "Villains"},
    {"id": 35, "name": "Professor X", "category": "X-Men"},
    {"id": 36, "name": "Captain Marvel", "category": "Cosmic"},
]


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/hero")
def hero():
    return render_template("hero.html")


@app.route("/hero/<hero_name>")
def hero_detail(hero_name):
    """Dynamic route for individual hero pages"""
    # Try to find hero by slug mapping first
    display_name = HERO_SLUG_MAP.get(hero_name.lower())
    
    if display_name:
        hero_data = HEROES_DATA.get(display_name)
    else:
        # Try direct match
        hero_data = HEROES_DATA.get(hero_name)
        display_name = hero_name
    
    if not hero_data:
        # Try case-insensitive search
        for name, data in HEROES_DATA.items():
            if name.lower() == hero_name.lower():
                hero_data = data
                display_name = name
                break
    
    if not hero_data:
        return "Hero not found", 404
    
    # Get image path for the hero using the mapping
    hero_key = display_name.lower()
    image_filename = HERO_IMAGE_MAP.get(hero_key, f"{hero_key}.jpg")
    hero_image = f"/static/assets/{image_filename}"
    
    return render_template("hero_detail.html", 
                         hero_name=display_name, 
                         hero_data=hero_data,
                         hero_image=hero_image)


@app.route("/timeline")
def timeline():
    """MCU Timeline page"""
    return render_template("timeline.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    full_name = data.get("fullName", "").strip()
    email_phone = data.get("emailPhone", "").strip()
    
    login_type = ""
    
    if re.match(email_regex, email_phone):
        login_type = "email"
        domain = email_phone.split("@")[1].lower()
        if domain != "gmail.com":
            return jsonify({
                "success": False,
                "message": "Please use a valid Gmail address (@gmail.com)"
            })
    elif re.match(phone_regex, email_phone):
        login_type = "phone"
    else:
        return jsonify({
            "success": False,
            "message": "Please enter a valid email or phone number"
        })
    
    try:
        if login_type == "email":
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name = VALUES(name)",
                (full_name, email_phone)
            )
        else:
            cursor.execute(
                "INSERT INTO users (name, phone) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name = VALUES(name)",
                (full_name, email_phone)
            )
        db.commit()
    except Exception as e:
        print(f"Database error: {e}")
    
    session['user'] = {
        'fullName': full_name,
        'email': email_phone if login_type == "email" else None,
        'phone': email_phone if login_type == "phone" else None
    }
    
    return jsonify({
        "success": True
    })


@app.route("/logout", methods=["POST"])
def logout():
    session.pop('user', None)
    return jsonify({"success": True, "message": "Logged out successfully"})


@app.route("/check-session")
def check_session():
    if 'user' in session:
        return jsonify({"authenticated": True, "user": session['user']})
    return jsonify({"authenticated": False})


@app.route("/search-heroes")
def search_heroes():
    query = request.args.get('q', '').lower()
    if query:
        results = [h for h in HEROES if query in h['name'].lower()]
        return jsonify(results)
    return jsonify(HEROES)


@app.route("/hero-movies/<hero_name>")
def get_hero_movies(hero_name):
    # Try slug mapping first
    display_name = HERO_SLUG_MAP.get(hero_name.lower())
    if display_name:
        hero_data = HEROES_DATA.get(display_name)
    else:
        hero_data = HEROES_DATA.get(hero_name)
    
    if not hero_data:
        # Try case-insensitive
        for name, data in HEROES_DATA.items():
            if name.lower() == hero_name.lower():
                hero_data = data
                break
    
    if hero_data:
        return jsonify(hero_data)
    return jsonify({"error": "Hero not found"})


@app.route("/favorites", methods=["GET"])
def get_favorites():
    if 'user' not in session:
        return jsonify({"success": False, "message": "Not logged in"})
    
    user = session.get('user', {})
    email = user.get('email')
    phone = user.get('phone')
    
    if email:
        cursor.execute("SELECT favorites FROM users WHERE email=%s", (email,))
    elif phone:
        cursor.execute("SELECT favorites FROM users WHERE phone=%s", (phone,))
    else:
        return jsonify({"success": False, "message": "No user found"})
    
    result = cursor.fetchone()
    favorites = []
    if result and result[0]:
        try:
            favorites = json.loads(result[0])
        except:
            favorites = []
    
    return jsonify({"success": True, "favorites": favorites})


@app.route("/favorites", methods=["POST"])
def add_favorite():
    if 'user' not in session:
        return jsonify({"success": False, "message": "Not logged in. Please login first."})
    
    data = request.json
    hero_name = data.get("heroName")
    
    if not hero_name:
        return jsonify({"success": False, "message": "Hero name required"})
    
    user = session.get('user', {})
    email = user.get('email')
    phone = user.get('phone')
    
    if not email and not phone:
        return jsonify({"success": False, "message": "No user found in session"})
    
    # Get current favorites
    if email:
        cursor.execute("SELECT favorites FROM users WHERE email=%s", (email,))
    elif phone:
        cursor.execute("SELECT favorites FROM users WHERE phone=%s", (phone,))
    
    result = cursor.fetchone()
    favorites = []
    if result and result[0]:
        try:
            favorites = json.loads(result[0])
        except:
            favorites = []
    
    # Add hero if not already in favorites
    if hero_name not in favorites:
        favorites.append(hero_name)
    
    favorites_json = json.dumps(favorites)
    
    if email:
        cursor.execute("UPDATE users SET favorites=%s WHERE email=%s", (favorites_json, email))
    elif phone:
        cursor.execute("UPDATE users SET favorites=%s WHERE phone=%s", (favorites_json, phone))
    
    db.commit()
    
    return jsonify({"success": True, "message": f"{hero_name} added to favorites!", "favorites": favorites})


@app.route("/favorites/remove", methods=["POST"])
def remove_favorite():
    if 'user' not in session:
        return jsonify({"success": False, "message": "Not logged in. Please login first."})
    
    data = request.json
    hero_name = data.get("heroName")
    
    if not hero_name:
        return jsonify({"success": False, "message": "Hero name required"})
    
    user = session.get('user', {})
    email = user.get('email')
    phone = user.get('phone')
    
    if not email and not phone:
        return jsonify({"success": False, "message": "No user found in session"})
    
    # Get current favorites
    if email:
        cursor.execute("SELECT favorites FROM users WHERE email=%s", (email,))
    elif phone:
        cursor.execute("SELECT favorites FROM users WHERE phone=%s", (phone,))
    
    result = cursor.fetchone()
    favorites = []
    if result and result[0]:
        try:
            favorites = json.loads(result[0])
        except:
            favorites = []
    
    # Remove hero from favorites
    if hero_name in favorites:
        favorites.remove(hero_name)
    
    favorites_json = json.dumps(favorites)
    
    if email:
        cursor.execute("UPDATE users SET favorites=%s WHERE email=%s", (favorites_json, email))
    elif phone:
        cursor.execute("UPDATE users SET favorites=%s WHERE phone=%s", (favorites_json, phone))
    
    db.commit()
    
    return jsonify({"success": True, "message": f"{hero_name} removed from favorites!", "favorites": favorites})


@app.route("/send-otp", methods=["POST"])
def send_otp():
    phone = request.json.get("phone")
    otp = str(random.randint(100000, 999999))

    cursor.execute(
        "INSERT INTO users (phone, otp) VALUES (%s, %s)",
        (phone, otp)
    )
    db.commit()

    print("OTP:", otp)
    return jsonify({"message": "OTP sent"})


@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    phone = request.json.get("phone")
    otp = request.json.get("otp")

    cursor.execute(
        "SELECT * FROM users WHERE phone=%s AND otp=%s",
        (phone, otp)
    )

    if cursor.fetchone():
        return jsonify({"success": True, "message": "OTP Verified! Redirecting..."})
    else:
        return jsonify({"success": False, "message": "Invalid OTP!"})


if __name__ == "__main__":
    app.run(debug=True)
