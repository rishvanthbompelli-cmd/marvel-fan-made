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
    # New heroes (Post-Endgame & Multiverse Saga) - IDs 37+
    {"id": 37, "name": "Shang-Chi", "category": "Mystic"},
    {"id": 38, "name": "Kate Bishop", "category": "Avengers"},
    {"id": 39, "name": "Yelena Belova", "category": "Avengers"},
    {"id": 40, "name": "Moon Knight", "category": "Mystic"},
    {"id": 41, "name": "Ms. Marvel", "category": "Cosmic"},
    {"id": 42, "name": "She-Hulk", "category": "Avengers"},
    {"id": 43, "name": "America Chavez", "category": "Mystic"},
    {"id": 44, "name": "Namor", "category": "Wakanda"},
    {"id": 45, "name": "Shuri", "category": "Wakanda"},
    {"id": 46, "name": "Gorr the God Butcher", "category": "Villains"},
    {"id": 47, "name": "Kang the Conqueror", "category": "Villains"},
    {"id": 48, "name": "Sylvie", "category": "Mystic"},
    {"id": 49, "name": "Red Guardian", "category": "Avengers"},
    {"id": 50, "name": "Taskmaster", "category": "Villains"},
    {"id": 51, "name": "Sersi", "category": "Cosmic"},
    {"id": 52, "name": "Ikaris", "category": "Cosmic"},
    {"id": 53, "name": "Druig", "category": "Cosmic"},
    {"id": 54, "name": "King Valkyrie", "category": "Asgard"},
    {"id": 55, "name": "Hercules", "category": "Cosmic"},
    {"id": 56, "name": "Adam Warlock", "category": "Guardians"},
    {"id": 57, "name": "High Evolutionary", "category": "Villains"},
    {"id": 58, "name": "Clea", "category": "Mystic"},
    {"id": 59, "name": "Blade", "category": "Mystic"},
    {"id": 60, "name": "Daredevil", "category": "Street"},
    {"id": 61, "name": "Echo", "category": "Street"},
    {"id": 62, "name": "Agatha Harkness", "category": "Mystic"},
    {"id": 63, "name": "Ironheart", "category": "Avengers"},
    {"id": 64, "name": "Nova", "category": "Cosmic"},
    {"id": 65, "name": "Silver Surfer", "category": "Cosmic"},
    {"id": 66, "name": "Mr. Fantastic", "category": "Fantastic Four"},
    {"id": 67, "name": "Invisible Woman", "category": "Fantastic Four"},
    {"id": 68, "name": "Human Torch", "category": "Fantastic Four"},
    {"id": 69, "name": "The Thing", "category": "Fantastic Four"},
    # Anime characters - IDs 70-74
    {"id": 70, "name": "Gojo Satoru", "category": "Anime"},
    {"id": 71, "name": "Yuji Itadori", "category": "Anime"},
    {"id": 72, "name": "Sung Jin-Woo", "category": "Anime"},
    {"id": 73, "name": "Tanjiro Kamado", "category": "Anime"},
    {"id": 74, "name": "Eren Yeager", "category": "Anime"},
    # Telugu heroes - IDs 75-79
    {"id": 75, "name": "Prabhas", "category": "Telugu"},
    {"id": 76, "name": "Allu Arjun", "category": "Telugu"},
    {"id": 77, "name": "Ram Charan", "category": "Telugu"},
    {"id": 78, "name": "NTR Jr", "category": "Telugu"},
    {"id": 79, "name": "Mahesh Babu", "category": "Telugu"},
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


@app.route("/category-heroes/<category>")
def get_category_heroes(category):
    """Get heroes by category: marvel, anime, or telugu"""
    cat = category.lower()
    
    if cat == 'marvel':
        results = [h for h in HEROES if h.get('category', '') in ['Avengers', 'Guardians', 'Street', 'Cosmic', 'Mystic', 'Villains', 'X-Men', 'Spider-Verse', 'Fantastic Four']]
    elif cat == 'anime':
        results = [h for h in HEROES if h.get('category', '') == 'Anime']
    elif cat == 'telugu':
        results = [h for h in HEROES if h.get('category', '') == 'Telugu']
    else:
        results = []
    
    return jsonify(results)


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


@app.route("/world-map")
def world_map():
    """Interactive World Map - Full Screen"""
    return render_template("world_map.html")


@app.route("/achievements")
def achievements():
    """User Achievements & Badges"""
    return render_template("achievements.html")


@app.route("/recommendations")
def recommendations():
    """Personalized Hero Recommendations"""
    return render_template("recommendations.html")


@app.route("/trending")
def trending():
    """Trending Heroes API"""
    # Get heroes sorted by popularity (mock data based on favorites count)
    trending_heroes = []
    return jsonify(trending_heroes)


# ========================================
# ENHANCED ROUTES WITH NEW FEATURES
# ========================================

@app.route("/category-heroes/<category>")
def enhanced_category_heroes(category):
    """Get heroes by category: marvel, anime, or telugu with enhanced data"""
    cat = category.lower()
    
    if cat == 'marvel':
        results = [h for h in HEROES if h.get('category', '') in ['Avengers', 'Guardians', 'Street', 'Cosmic', 'Mystic', 'Villains', 'X-Men', 'Spider-Verse', 'Fantastic Four', 'Wakanda', 'Asgard']]
    elif cat == 'anime':
        results = [h for h in HEROES if h.get('category', '') == 'Anime']
    elif cat == 'telugu':
        results = [h for h in HEROES if h.get('category', '') == 'Telugu']
    else:
        results = []
    
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
    
    return jsonify(enhanced_results)


if __name__ == "__main__":
    app.run(debug=True)
