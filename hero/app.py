from flask import Flask, request, jsonify, render_template, session, redirect
from flask_cors import CORS
import mysql.connector
import os
import re
import json
import random

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='/static')
CORS(app, supports_credentials=True)

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
    # New heroes (Post-Endgame & Multiverse Saga)
    "shang-chi": "shang-chi.jpg",
    "kate bishop": "kate-bishop.jpg",
    "yelena belova": "yelena-belova.jpg",
    "moon knight": "moon-knight.jpg",
    "ms. marvel": "ms-marvel.jpg",
    "she-hulk": "she-hulk.jpg",
    "america chavez": "america-chavez.jpg",
    "namor": "namor.jpg",
    "shuri": "shuri.jpg",
    "gorr the god butcher": "gorr.jpg",
    "kang the conqueror": "kang.jpg",
    "sylvie": "sylvie.jpg",
    "red guardian": "red-guardian.jpg",
    "taskmaster": "taskmaster.jpg",
    "sersi": "sersi.jpg",
    "ikaris": "ikaris.jpg",
    "druig": "druig.jpg",
    "king valkyrie": "valkyrie.jpg",
    "hercules": "hercules.jpg",
    "adam warlock": "adam-warlock.jpg",
    "high evolutionary": "high-evolutionary.jpg",
    "clea": "clea.jpg",
    "blade": "blade.jpg",
    "daredevil": "daredevil.jpg",
    "echo": "echo.jpg",
    "agatha harkness": "agatha-harkness.jpg",
    "ironheart": "ironheart.jpg",
    "nova": "nova.jpg",
    "silver surfer": "silver-surfer.jpg",
    "mr. fantastic": "mr-fantastic.jpg",
    "invisible woman": "invisible-woman.jpg",
    "human torch": "human-torch.jpg",
    "the thing": "the-thing.jpg",
    # Anime characters
    "gojo satoru": "gojo-satoru.jpg",
    "yuji itadori": "yuji-itadori.jpg",
    "sung jin-woo": "sung-jin-woo.jpg",
    "tanjiro kamado": "tanjiro-kamado.jpg",
    "eren yeager": "eren-yeager.jpg",
    # Telugu heroes
    "prabhas": "prabhas.jpg",
    "allu arjun": "allu-arjun.jpg",
    "ram charan": "ram-charan.jpg",
    "ntr jr": "ntr-jr.jpg",
    "mahesh babu": "mahesh-babu.jpg",
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
    # New heroes (Post-Endgame & Multiverse Saga)
    "shang-chi": "Shang-Chi",
    "kate-bishop": "Kate Bishop",
    "yelena-belova": "Yelena Belova",
    "moon-knight": "Moon Knight",
    "ms-marvel": "Ms. Marvel",
    "she-hulk": "She-Hulk",
    "america-chavez": "America Chavez",
    "namor": "Namor",
    "shuri": "Shuri",
    "gorr": "Gorr the God Butcher",
    "kang": "Kang the Conqueror",
    "sylvie": "Sylvie",
    "red-guardian": "Red Guardian",
    "taskmaster": "Taskmaster",
    "sersi": "Sersi",
    "ikaris": "Ikaris",
    "druig": "Druig",
    "king-valkyrie": "King Valkyrie",
    "hercules": "Hercules",
    "adam-warlock": "Adam Warlock",
    "high-evolutionary": "High Evolutionary",
    "clea": "Clea",
    "blade": "Blade",
    "daredevil": "Daredevil",
    "echo": "Echo",
    "agatha-harkness": "Agatha Harkness",
    "ironheart": "Ironheart",
    "nova": "Nova",
    "silver-surfer": "Silver Surfer",
    "mr-fantastic": "Mr. Fantastic",
    "invisible-woman": "Invisible Woman",
    "human-torch": "Human Torch",
    "the-thing": "The Thing",
    # Anime characters
    "gojo-satoru": "Gojo Satoru",
    "yuji-itadori": "Yuji Itadori",
    "sung-jin-woo": "Sung Jin-Woo",
    "tanjiro-kamado": "Tanjiro Kamado",
    "eren-yeager": "Eren Yeager",
    # Telugu heroes
    "prabhas": "Prabhas",
    "allu-arjun": "Allu Arjun",
    "ram-charan": "Ram Charan",
    "ntr-jr": "NTR Jr",
    "mahesh-babu": "Mahesh Babu",
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
    # New heroes (Post-Endgame & Multiverse Saga)
    "Shang-Chi": {
        "category": "Mystic",
        "description": "Martial arts master with the Ten Rings.",
        "movies": ["Shang-Chi and the Legend of the Ten Rings (2021)"]
    },
    "Kate Bishop": {
        "category": "Avengers",
        "description": "Young archer and Hawkeye's protégé.",
        "movies": ["Hawkeye (2021)"]
    },
    "Yelena Belova": {
        "category": "Avengers",
        "description": "Red Guardian's daughter, skilled assassin.",
        "movies": ["Black Widow (2021)", "Hawkeye (2021)"]
    },
    "Moon Knight": {
        "category": "Mystic",
        "description": "Avenger with multiple identities, granted powers by Khonshu.",
        "movies": ["Moon Knight (2022)"]
    },
    "Ms. Marvel": {
        "category": "Cosmic",
        "description": "Inhuman with cosmic embers powers.",
        "movies": ["Ms. Marvel (2022)", "The Marvels (2023)"]
    },
    "She-Hulk": {
        "category": "Avengers",
        "description": "Lawyer and Hulk cousin with gamma powers.",
        "movies": ["She-Hulk (2022)"]
    },
    "America Chavez": {
        "category": "Mystic",
        "description": "Teenager with power to travel the multiverse.",
        "movies": ["Doctor Strange in the Multiverse of Madness (2022)"]
    },
    "Namor": {
        "category": "Wakanda",
        "description": "King of Atlantis, mutant with underwater abilities.",
        "movies": ["Black Panther: Wakanda Forever (2022)"]
    },
    "Shuri": {
        "category": "Wakanda",
        "description": "Genius inventor, Black Panther of Wakanda.",
        "movies": ["Black Panther (2018)", "Avengers: Infinity War (2018)", "Avengers: Endgame (2019)", "Black Panther: Wakanda Forever (2022)"]
    },
    "Gorr the God Butcher": {
        "category": "Villains",
        "description": "Serial killer of gods wielding All-Black the Necrosword.",
        "movies": ["Thor: Love and Thunder (2022)"]
    },
    "Kang the Conqueror": {
        "category": "Villains",
        "description": "Multiversal conqueror from the 31st century.",
        "movies": ["Ant-Man and the Wasp: Quantumania (2023)", "Avengers: The Kang Dynasty (2025)"]
    },
    "Sylvie": {
        "category": "Mystic",
        "description": "Variant of Loki, skilled at enchantment magic.",
        "movies": ["Loki (2021)"]
    },
    "Red Guardian": {
        "category": "Avengers",
        "description": "Russia's super-soldier, father of Yelena Belova.",
        "movies": ["Black Widow (2021)"]
    },
    "Taskmaster": {
        "category": "Villains",
        "description": "Mercenary with photographic reflexes.",
        "movies": ["Black Widow (2021)"]
    },
    "Sersi": {
        "category": "Cosmic",
        "description": "Eternal with matter manipulation powers.",
        "movies": ["Eternals (2021)"]
    },
    "Ikaris": {
        "category": "Cosmic",
        "description": "Eternal with solar energy manipulation.",
        "movies": ["Eternals (2021)"]
    },
    "Druig": {
        "category": "Cosmic",
        "description": "Eternal with telepathic and telekinetic abilities.",
        "movies": ["Eternals (2021)"]
    },
    "King Valkyrie": {
        "category": "Asgard",
        "description": "Warrior queen of New Asgard, successor to Thor.",
        "movies": ["Thor: Ragnarok (2017)", "Avengers: Endgame (2019)", "Thor: Love and Thunder (2022)"]
    },
    "Hercules": {
        "category": "Cosmic",
        "description": "Olympian god, son of Zeus.",
        "movies": ["Thor: Love and Thunder (2022)"]
    },
    "Adam Warlock": {
        "category": "Guardians",
        "description": "Artificial being known as Him, powerful cosmic entity.",
        "movies": ["Guardians of the Galaxy Vol. 3 (2023)"]
    },
    "High Evolutionary": {
        "category": "Villains",
        "description": "Mad scientist who created Adam Warlock.",
        "movies": ["Guardians of the Galaxy Vol. 3 (2023)"]
    },
    "Clea": {
        "category": "Mystic",
        "description": "Dormammu's daughter, master of the dark dimension.",
        "movies": ["Doctor Strange in the Multiverse of Madness (2022)"]
    },
    "Blade": {
        "category": "Mystic",
        "description": "Daywalker, half-vampire vampire hunter.",
        "movies": ["Blade (2025)"]
    },
    "Daredevil": {
        "category": "Street",
        "description": "Blind lawyer by day, vigilante by night.",
        "movies": ["Daredevil (2024)"]
    },
    "Echo": {
        "category": "Street",
        "description": "Native American assassin with photographic reflexes.",
        "movies": ["Echo (2023)"]
    },
    "Agatha Harkness": {
        "category": "Mystic",
        "description": " centuries-old witch, mentor to Scarlet Witch.",
        "movies": ["WandaVision (2021)", "Agatha: Darkhold Diaries (2023)"]
    },
    "Ironheart": {
        "category": "Avengers",
        "description": "Genius inventor with advanced armor technology.",
        "movies": ["Ironheart (2024)"]
    },
    "Nova": {
        "category": "Cosmic",
        "description": "Human-Rhodey hybrid with Nova Force powers.",
        "movies": ["Nova (2026)"]
    },
    "Silver Surfer": {
        "category": "Cosmic",
        "description": " Herald of Galactus, powered by the Power Cosmic.",
        "movies": ["Fantastic Four (2025)", "Silver Surfer (2026)"]
    },
    "Mr. Fantastic": {
        "category": "Fantastic Four",
        "description": "Leader of the Fantastic Four, genius inventor with elastic body.",
        "movies": ["Fantastic Four (2025)"]
    },
    "Invisible Woman": {
        "category": "Fantastic Four",
        "description": "Fantastic Four member with invisibility and force field powers.",
        "movies": ["Fantastic Four (2025)"]
    },
    "Human Torch": {
        "category": "Fantastic Four",
        "description": "Fantastic Four member with flame powers.",
        "movies": ["Fantastic Four (2025)"]
    },
    "The Thing": {
        "category": "Fantastic Four",
        "description": "Fantastic Four member with super strength and durability.",
        "movies": ["Fantastic Four (2025)"]
    },
    # Anime characters
    "Gojo Satoru": {
        "category": "Anime",
        "description": "Strongest sorcerer from Jujutsu Kaisen.",
        "movies": ["Jujutsu Kaisen 0"]
    },
    "Yuji Itadori": {
        "category": "Anime",
        "description": "Jujutsu sorcerer and vessel of Sukuna.",
        "movies": ["Jujutsu Kaisen 0"]
    },
    "Sung Jin-Woo": {
        "category": "Anime",
        "description": "Shadow Monarch from Solo Leveling.",
        "movies": ["Solo Leveling Season 1"]
    },
    "Tanjiro Kamado": {
        "category": "Anime",
        "description": "Demon Slayer fighting to save his sister.",
        "movies": ["Demon Slayer: Mugen Train"]
    },
    "Eren Yeager": {
        "category": "Anime",
        "description": "Main protagonist of Attack on Titan.",
        "movies": ["Attack on Titan Final Season"]
    },
    # Telugu heroes
    "Prabhas": {
        "category": "Telugu",
        "description": "Pan-India superstar.",
        "movies": ["Baahubali", "Salaar", "Kalki 2898 AD"]
    },
    "Allu Arjun": {
        "category": "Telugu",
        "description": "Stylish star of Telugu cinema.",
        "movies": ["Pushpa", "Ala Vaikunthapurramuloo"]
    },
    "Ram Charan": {
        "category": "Telugu",
        "description": "RRR global star.",
        "movies": ["RRR", "Magadheera"]
    },
    "NTR Jr": {
        "category": "Telugu",
        "description": "Powerful performer from RRR.",
        "movies": ["RRR", "Temper"]
    },
    "Mahesh Babu": {
        "category": "Telugu",
        "description": "Superstar of Telugu industry.",
        "movies": ["Pokiri", "Srimanthudu"]
    },
}

HEROES = [
    # AVENGERS
    {"id": 1, "name": "Iron Man", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 2, "name": "Captain America", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/captain america.jpg"},
    {"id": 3, "name": "Thor", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/thor.jpg"},
    {"id": 4, "name": "Hulk", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/hulk.jpg"},
    {"id": 5, "name": "Black Widow", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/black widow.jpg"},
    {"id": 6, "name": "Hawkeye", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/hawkeye.jpg"},
    {"id": 7, "name": "Scarlet Witch", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/scarlet witch.jpg"},
    {"id": 8, "name": "Vision", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/vision.jpg"},
    {"id": 9, "name": "Falcon", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/falcon.jpg"},
    {"id": 10, "name": "War Machine", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/war machine.jpg"},
    {"id": 11, "name": "Ant-Man", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/ant-man.jpg"},
    {"id": 12, "name": "Wasp", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/wasp.jpg"},
    {"id": 13, "name": "Doctor Strange", "category": "Mystic", "team": "mystic", "role": "Hero", "image": "/static/assets/doctor strange.jpg"},
    {"id": 14, "name": "Black Panther", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/black panther.jpg"},
    {"id": 15, "name": "Captain Marvel", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/captain marvel.jpg"},
    {"id": 16, "name": "Spider-Man", "category": "Spider-Verse", "team": "spiderverse", "role": "Hero", "image": "/static/assets/spider-man.jpg"},
    {"id": 17, "name": "She-Hulk", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/she-hulk.jpg"},
    {"id": 18, "name": "Shang-Chi", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/shang-chi.jpg"},
    {"id": 19, "name": "Moon Knight", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/moon knight.jpg"},
    {"id": 20, "name": "Winter Soldier", "category": "Avengers", "team": "avengers", "role": "Anti-Hero", "image": "/static/assets/winter soldier.jpg"},
    
    # X-MEN
    {"id": 21, "name": "Professor X", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/professor x.jpg"},
    {"id": 22, "name": "Wolverine", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/wolverine.jpg"},
    {"id": 23, "name": "Cyclops", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/cyclops.jpg"},
    {"id": 24, "name": "Jean Grey", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/jean grey.jpg"},
    {"id": 25, "name": "Storm", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/storm.jpg"},
    {"id": 26, "name": "Beast", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/beast.jpg"},
    {"id": 27, "name": "Rogue", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/rogue.jpg"},
    {"id": 28, "name": "Gambit", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/gambit.jpg"},
    {"id": 29, "name": "Nightcrawler", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/nightcrawler.jpg"},
    {"id": 30, "name": "Iceman", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/iceman.jpg"},
    {"id": 31, "name": "Colossus", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/colossus.jpg"},
    {"id": 32, "name": "Kitty Pryde", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/kitty pryde.jpg"},
    {"id": 33, "name": "Psylocke", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/psylocke.jpg"},
    {"id": 34, "name": "Magneto", "category": "X-Men", "team": "xmen", "role": "Villain", "image": "/static/assets/magneto.jpg"},
    {"id": 35, "name": "Mystique", "category": "X-Men", "team": "xmen", "role": "Villain", "image": "/static/assets/mystique.jpg"},
    {"id": 36, "name": "Sabretooth", "category": "X-Men", "team": "xmen", "role": "Villain", "image": "/static/assets/sabretooth.jpg"},
    {"id": 37, "name": "Apocalypse", "category": "X-Men", "team": "xmen", "role": "Villain", "image": "/static/assets/apocalypse.jpg"},
    {"id": 38, "name": "Mr. Sinister", "category": "X-Men", "team": "xmen", "role": "Villain", "image": "/static/assets/mr sinister.jpg"},
    {"id": 39, "name": "Quicksilver", "category": "X-Men", "team": "xmen", "role": "Hero", "image": "/static/assets/quicksilver.jpg"},
    
    # GUARDIANS OF THE GALAXY
    {"id": 40, "name": "Star-Lord", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/star-lord.jpg"},
    {"id": 41, "name": "Gamora", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/gamora.jpg"},
    {"id": 42, "name": "Drax", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/drax.jpg"},
    {"id": 43, "name": "Rocket Raccoon", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/rocket.jpg"},
    {"id": 44, "name": "Groot", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/groot.jpg"},
    {"id": 45, "name": "Mantis", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/mantis.jpg"},
    {"id": 46, "name": "Nebula", "category": "Guardians", "team": "guardians", "role": "Anti-Hero", "image": "/static/assets/nebula.jpg"},
    {"id": 47, "name": "Adam Warlock", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/adam warlock.jpg"},
    {"id": 48, "name": "Nova", "category": "Guardians", "team": "guardians", "role": "Hero", "image": "/static/assets/nova.jpg"},
    
    # COSMIC ENTITIES
    {"id": 49, "name": "Silver Surfer", "category": "Cosmic", "team": "cosmic", "role": "Hero", "image": "/static/assets/silver surfer.jpg"},
    {"id": 50, "name": "Galactus", "category": "Cosmic", "team": "cosmic", "role": "Cosmic Entity", "image": "/static/assets/galactus.jpg"},
    {"id": 51, "name": "Thanos", "category": "Cosmic", "team": "cosmic", "role": "Villain", "image": "/static/assets/thanos.jpg"},
    {"id": 52, "name": "The Watcher", "category": "Cosmic", "team": "cosmic", "role": "Cosmic Entity", "image": "/static/assets/watcher.jpg"},
    {"id": 53, "name": "Eternity", "category": "Cosmic", "team": "cosmic", "role": "Cosmic Entity", "image": "/static/assets/eternity.jpg"},
    {"id": 54, "name": "Living Tribunal", "category": "Cosmic", "team": "cosmic", "role": "Cosmic Entity", "image": "/static/assets/living tribunal.jpg"},
    {"id": 55, "name": "Celestials", "category": "Cosmic", "team": "cosmic", "role": "Cosmic Entity", "image": "/static/assets/celestials.jpg"},
    {"id": 56, "name": "Kang the Conqueror", "category": "Cosmic", "team": "cosmic", "role": "Villain", "image": "/static/assets/kang.jpg"},
    
    # SPIDER-VERSE
    {"id": 57, "name": "Miles Morales", "category": "Spider-Verse", "team": "spiderverse", "role": "Hero", "image": "/static/assets/miles morales.jpg"},
    {"id": 58, "name": "Spider-Gwen", "category": "Spider-Verse", "team": "spiderverse", "role": "Hero", "image": "/static/assets/spider-gwen.jpg"},
    {"id": 59, "name": "Venom", "category": "Spider-Verse", "team": "spiderverse", "role": "Anti-Hero", "image": "/static/assets/venom.jpg"},
    {"id": 60, "name": "Carnage", "category": "Spider-Verse", "team": "spiderverse", "role": "Villain", "image": "/static/assets/carnage.jpg"},
    {"id": 61, "name": "Green Goblin", "category": "Spider-Verse", "team": "spiderverse", "role": "Villain", "image": "/static/assets/green goblin.jpg"},
    {"id": 62, "name": "Doctor Octopus", "category": "Spider-Verse", "team": "spiderverse", "role": "Villain", "image": "/static/assets/doctor octopus.jpg"},
    {"id": 63, "name": "Sandman", "category": "Spider-Verse", "team": "spiderverse", "role": "Anti-Hero", "image": "/static/assets/sandman.jpg"},
    {"id": 64, "name": "Lizard", "category": "Spider-Verse", "team": "spiderverse", "role": "Villain", "image": "/static/assets/lizard.jpg"},
    
    # MYSTIC / MAGIC
    {"id": 65, "name": "Loki", "category": "Mystic", "team": "mystic", "role": "Anti-Hero", "image": "/static/assets/loki.jpg"},
    {"id": 66, "name": "Wong", "category": "Mystic", "team": "mystic", "role": "Hero", "image": "/static/assets/wong.jpg"},
    {"id": 67, "name": "Agatha Harkness", "category": "Mystic", "team": "mystic", "role": "Anti-Hero", "image": "/static/assets/agatha harkness.jpg"},
    {"id": 68, "name": "Ghost Rider", "category": "Mystic", "team": "mystic", "role": "Hero", "image": "/static/assets/ghost rider.jpg"},
    {"id": 69, "name": "Blade", "category": "Mystic", "team": "mystic", "role": "Hero", "image": "/static/assets/blade.jpg"},
    
    # STREET LEVEL
    {"id": 70, "name": "Daredevil", "category": "Street", "team": "street", "role": "Hero", "image": "/static/assets/daredevil.jpg"},
    {"id": 71, "name": "Luke Cage", "category": "Street", "team": "street", "role": "Hero", "image": "/static/assets/luke cage.jpg"},
    {"id": 72, "name": "Iron Fist", "category": "Street", "team": "street", "role": "Hero", "image": "/static/assets/iron fist.jpg"},
    {"id": 73, "name": "Jessica Jones", "category": "Street", "team": "street", "role": "Hero", "image": "/static/assets/jessica jones.jpg"},
    {"id": 74, "name": "Punisher", "category": "Street", "team": "street", "role": "Anti-Hero", "image": "/static/assets/punisher.jpg"},
    {"id": 75, "name": "Echo", "category": "Street", "team": "street", "role": "Hero", "image": "/static/assets/echo.jpg"},
    
    # VILLAINS
    {"id": 76, "name": "Ultron", "category": "Villains", "team": "cosmic", "role": "Villain", "image": "/static/assets/ultron.jpg"},
    {"id": 77, "name": "Deadpool", "category": "Villains", "team": "avengers", "role": "Anti-Hero", "image": "/static/assets/deapool.jpg"},
    
    # Additional heroes (using fallback images)
    {"id": 78, "name": "Kate Bishop", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 79, "name": "Yelena Belova", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/black widow.jpg"},
    {"id": 80, "name": "Ironheart", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 81, "name": "Ms. Marvel", "category": "Avengers", "team": "avengers", "role": "Hero", "image": "/static/assets/captain marvel.jpg"},
    
    # Anime characters - NOT Marvel
    {"id": 90, "name": "Gojo Satoru", "category": "Anime", "team": "anime", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 91, "name": "Yuji Itadori", "category": "Anime", "team": "anime", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 92, "name": "Sung Jin-Woo", "category": "Anime", "team": "anime", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 93, "name": "Tanjiro Kamado", "category": "Anime", "team": "anime", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 94, "name": "Eren Yeager", "category": "Anime", "team": "anime", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    
    # Telugu heroes - NOT Marvel
    {"id": 95, "name": "Prabhas", "category": "Telugu", "team": "telugu", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 96, "name": "Allu Arjun", "category": "Telugu", "team": "telugu", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 97, "name": "Ram Charan", "category": "Telugu", "team": "telugu", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 98, "name": "NTR Jr", "category": "Telugu", "team": "telugu", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
    {"id": 99, "name": "Mahesh Babu", "category": "Telugu", "team": "telugu", "role": "Hero", "image": "/static/assets/Iron-Man.jpg"},
]


@app.route("/")
def home():
    """Landing page - Multiverse Hub with cinematic intro"""
    return render_template("landing.html")


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


@app.route("/universe/<category>")
def universe(category):
    """Universe page with category-specific theme"""
    valid_categories = ['marvel', 'anime', 'telugu']
    if category not in valid_categories:
        return redirect("/")
    return render_template("universe.html", category=category)


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


@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop('user', None)
    if request.method == "GET":
        return redirect("/")
    return jsonify({"success": True, "message": "Logged out successfully"})


@app.route("/check-session")
def check_session():
    if 'user' in session:
        return jsonify({"authenticated": True, "user": session['user']})
    return jsonify({"authenticated": False})


@app.route("/search-heroes")
def search_heroes():
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '').lower()
    
    results = HEROES
    
    # Filter by category if provided
    if category:
        if category == 'marvel':
            results = [h for h in results if h.get('category', '') in ['Avengers', 'Guardians', 'Street', 'Cosmic', 'Mystic', 'Villains', 'X-Men', 'Spider-Verse', 'Fantastic Four']]
        elif category == 'anime':
            results = [h for h in results if h.get('category', '') == 'Anime']
        elif category == 'telugu':
            results = [h for h in results if h.get('category', '') == 'Telugu']
    
    # Filter by search query if provided
    if query:
        results = [h for h in results if query in h['name'].lower()]
    
    return jsonify(results)


@app.route("/category-heroes/<universe>/<category>")
def get_category_heroes(universe, category):
    """Get heroes by category: marvel, anime, or telugu with enhanced data"""
    uni = universe.lower()
    cat = category.lower()
    
    # Filter by universe
    if uni == 'marvel':
        # Return Marvel heroes
        results = [h for h in HEROES if h.get('team', '') not in ['anime', 'telugu']]
    elif uni == 'anime':
        results = [h for h in HEROES if h.get('team', '') == 'anime']
    elif uni == 'telugu':
        results = [h for h in HEROES if h.get('team', '') == 'telugu']
    else:
        results = []
    
    # Filter by category if not 'all'
    if cat != 'all':
        results = [h for h in results if h.get('category', '').lower() == cat]
    
    # Add image and stats to each hero
    enhanced_results = []
    for h in results:
        hero_key = h['name'].lower()
        image_filename = HERO_IMAGE_MAP.get(hero_key, f"{hero_key}.jpg")
        enhanced_results.append({
            **h,
            "image": f"/static/assets/{image_filename}",
            "slug": h['name'].lower().replace(' ', '-')
        })
    
    # Apply team sorting for Marvel category only
    if uni == 'marvel':
        team_order = {
            "avengers": 1,
            "guardians": 2,
            "spiderverse": 3,
            "xmen": 4,
            "mystic": 5,
            "street": 6,
            "cosmic": 7
        }
        enhanced_results = sorted(
            enhanced_results,
            key=lambda hero: team_order.get(hero.get("team", "cosmic"), 99)
        )
    
    return jsonify(enhanced_results)


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


# ========================================
# NEW ROUTES FOR CINEMATIC FEATURES
# ========================================

@app.route("/compare")
def compare():
    """Hero Power Comparison Tool"""
    # Get all heroes for dropdown
    heroes_list = [
        {"id": h['id'], "name": h['name'], "category": h.get('category', '')}
        for h in HEROES
    ]
    return render_template("compare.html", heroes=heroes_list)


@app.route("/world")
def world():
    """Interactive World Map"""
    return render_template("world.html")



@app.route("/achievements")
def achievements():
    """User Achievements & Badges - Coming Soon"""
    return jsonify({
        "message": "Achievements feature coming soon!",
        "available": False
    })


@app.route("/recommendations")
def recommendations():
    """Personalized Hero Recommendations - Coming Soon"""
    return jsonify({
        "message": "Recommendations feature coming soon!",
        "available": False,
        "suggestions": []
    })


@app.route("/trending")
def trending():
    """Trending Heroes API - Returns popular heroes"""
    # Get heroes sorted by popularity (based on favorites count)
    trending_heroes = []
    
    # For now, return some popular Marvel heroes as trending
    popular_heroes = ['Iron Man', 'Spider-Man', 'Thor', 'Captain America', 'Black Panther']
    for hero_name in popular_heroes:
        if hero_name in HEROES_DATA:
            hero_data = HEROES_DATA[hero_name]
            hero_key = hero_name.lower()
            image_filename = HERO_IMAGE_MAP.get(hero_key, f"{hero_key}.jpg")
            trending_heroes.append({
                "name": hero_name,
                "category": hero_data.get("category", ""),
                "image": f"/static/assets/{image_filename}",
                "slug": hero_key.replace(' ', '-')
            })
    
    return jsonify(trending_heroes)


# ========================================
# ENHANCED ROUTES WITH NEW FEATURES
# ========================================




if __name__ == "__main__":
    app.run(debug=True)
