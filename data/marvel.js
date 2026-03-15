// Marvel Universe character data

const UNIVERSE_CONFIG = {
    id: "marvel",
    name: "Marvel Cinematic Universe",
    description: "The Marvel Cinematic Universe (MCU) is an American media franchise and shared universe centered on a series of superhero films produced by Marvel Studios.",
    color: "#E62429",
    logo: "/static/assets/marvel-logo.png"
};

// Category definitions
const CATEGORIES = {
    avengers: {
        id: "avengers",
        name: "The Avengers",
        description: "Earth's mightiest heroes united to protect the world.",
        icon: "shield"
    },
    guardians: {
        id: "guardians",
        name: "Guardians of the Galaxy",
        description: "A group of intergalactic criminals who become unlikely heroes.",
        icon: "star"
    },
    xmen: {
        id: "xmen",
        name: "X-Men",
        description: "Mutant heroes fighting for peace and equality.",
        icon: "x"
    },
    villains: {
        id: "villains",
        name: "Villains",
        description: "The most powerful antagonists in the MCU.",
        icon: "skull"
    }
};

// Character data organized by category
const CHARACTERS = {
    // AVENGERS
    "Iron Man": {
        id: "iron-man",
        name: "Iron Man",
        universe: "marvel",
        category: "avengers",
        real_name: "Tony Stark",
        image: "Iron-Man.jpg",
        description: "Genius, billionaire, playboy, philanthropist. The armored Avenger who started it all.",
        powers: [
            "Arc Reactor Technology",
            "Powered Armor Suit",
            "Repulsor Beams",
            "Flight",
            "Superhuman Strength",
            "Genius-Level Intellect"
        ],
        timeline: {
            first_appearance: "Iron Man (2008)",
            born: "1970"
        },
        movie_appearances: [
            "Iron Man (2008)",
            "Iron Man 2 (2010)",
            "The Avengers (2012)",
            "Iron Man 3 (2013)",
            "Avengers: Age of Ultron (2015)",
            "Captain America: Civil War (2016)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)"
        ],
        stats: {
            strength: 85,
            speed: 70,
            intelligence: 100,
            abilities: 90,
            combat: 80,
            durability: 75
        }
    },
    "Captain America": {
        id: "captain-america",
        name: "Captain America",
        universe: "marvel",
        category: "avengers",
        real_name: "Steve Rogers",
        image: "captain america.jpg",
        description: "The First Avenger with an unbreakable shield and unwavering moral compass.",
        powers: [
            "Superhuman Strength",
            "Superhuman Speed",
            "Superhuman Durability",
            "Enhanced Healing",
            "Master Martial Artist",
            "Vibranium Shield"
        ],
        timeline: {
            first_appearance: "Captain America: The First Avenger (2011)",
            born: "1918"
        },
        movie_appearances: [
            "Captain America: The First Avenger (2011)",
            "The Avengers (2012)",
            "Captain America: The Winter Soldier (2014)",
            "Avengers: Age of Ultron (2015)",
            "Captain America: Civil War (2016)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)"
        ],
        stats: {
            strength: 90,
            speed: 80,
            intelligence: 85,
            abilities: 75,
            combat: 100,
            durability: 90
        }
    },
    "Thor": {
        id: "thor",
        name: "Thor",
        universe: "marvel",
        category: "avengers",
        real_name: "Thor Odinson",
        image: "thor.jpg",
        description: "God of Thunder, wielder of Mjölnir and Stormbreaker.",
        powers: [
            "Thor Lightning",
            "Superhuman Strength",
            "Superhuman Durability",
            "Flight",
            "Weather Manipulation",
            "Regenerative Healing"
        ],
        timeline: {
            first_appearance: "Thor (2011)",
            born: "Unknown (Thousands of years)"
        },
        movie_appearances: [
            "Thor (2011)",
            "The Avengers (2012)",
            "Thor: The Dark World (2013)",
            "Avengers: Age of Ultron (2015)",
            "Thor: Ragnarok (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Thor: Love and Thunder (2022)"
        ],
        stats: {
            strength: 100,
            speed: 85,
            intelligence: 70,
            abilities: 95,
            combat: 90,
            durability: 95
        }
    },
    "Hulk": {
        id: "hulk",
        name: "Hulk",
        universe: "marvel",
        category: "avengers",
        real_name: "Bruce Banner",
        image: "hulk.jpg",
        description: "The strongest Avenger with incredible gamma-powered strength.",
        powers: [
            "Superhuman Strength",
            "Superhuman Durability",
            "Regenerative Healing",
            "Gamma Radiation Immunity",
            "Leap Ability",
            "Rage Boost"
        ],
        timeline: {
            first_appearance: "The Incredible Hulk (2008)",
            born: "1969"
        },
        movie_appearances: [
            "The Incredible Hulk (2008)",
            "The Avengers (2012)",
            "Avengers: Age of Ultron (2015)",
            "Thor: Ragnarok (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "She-Hulk (2022)"
        ],
        stats: {
            strength: 100,
            speed: 60,
            intelligence: 80,
            abilities: 50,
            combat: 70,
            durability: 100
        }
    },
    "Black Widow": {
        id: "black-widow",
        name: "Black Widow",
        universe: "marvel",
        category: "avengers",
        real_name: "Natasha Romanoff",
        image: "black widow.jpg",
        description: "Master spy and assassin, Avenger team member.",
        powers: [
            "Master Martial Artist",
            "Espionage",
            "Acrobatics",
            "Weapons Expert",
            "Hacking",
            "Seduction"
        ],
        timeline: {
            first_appearance: "Iron Man 2 (2010)",
            born: "1984"
        },
        movie_appearances: [
            "Iron Man 2 (2010)",
            "The Avengers (2012)",
            "Captain America: The Winter Soldier (2014)",
            "Captain America: Civil War (2016)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Black Widow (2021)"
        ],
        stats: {
            strength: 55,
            speed: 70,
            intelligence: 90,
            abilities: 85,
            combat: 95,
            durability: 50
        }
    },
    "Hawkeye": {
        id: "hawkeye",
        name: "Hawkeye",
        universe: "marvel",
        category: "avengers",
        real_name: "Clint Barton",
        image: "hawkeye.jpg",
        description: "Master archer and Avenger, never misses his target.",
        powers: [
            "Master Archer",
            "Expert Marksman",
            "Master Martial Artist",
            "Acrobatics",
            "Tactical Planning",
            "Throwing Weapons"
        ],
        timeline: {
            first_appearance: "Thor (2011)",
            born: "1971"
        },
        movie_appearances: [
            "Thor (2011)",
            "The Avengers (2012)",
            "Avengers: Age of Ultron (2015)",
            "Captain America: Civil War (2016)",
            "Avengers: Endgame (2019)",
            "Hawkeye (2021)"
        ],
        stats: {
            strength: 50,
            speed: 60,
            intelligence: 80,
            abilities: 90,
            combat: 85,
            durability: 45
        }
    },
    "Scarlet Witch": {
        id: "scarlet-witch",
        name: "Scarlet Witch",
        universe: "marvel",
        category: "avengers",
        real_name: "Wanda Maximoff",
        image: "scarlet witch.jpg",
        description: "Powerful mutant with reality-warping abilities.",
        powers: [
            "Telekinesis",
            "Telepathy",
            "Energy Manipulation",
            "Reality Warping",
            "Chaos Magic",
            "Probability Manipulation"
        ],
        timeline: {
            first_appearance: "Avengers: Age of Ultron (2015)",
            born: "1989"
        },
        movie_appearances: [
            "Avengers: Age of Ultron (2015)",
            "Captain America: Civil War (2016)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "WandaVision (2021)",
            "Doctor Strange in the Multiverse of Madness (2022)"
        ],
        stats: {
            strength: 70,
            speed: 65,
            intelligence: 85,
            abilities: 100,
            combat: 60,
            durability: 75
        }
    },
    "Vision": {
        id: "vision",
        name: "Vision",
        universe: "marvel",
        category: "avengers",
        real_name: "Vision (Synthezoid)",
        image: "vision.jpg",
        description: "Android Avenger with the Mind Stone.",
        powers: [
            "Density Manipulation",
            "Flight",
            "Solar Energy Absorption",
            "Superhuman Strength",
            "Mind Stone Power",
            "Intangibility"
        ],
        timeline: {
            first_appearance: "Avengers: Age of Ultron (2015)",
            born: "2015"
        },
        movie_appearances: [
            "Avengers: Age of Ultron (2015)",
            "Captain America: Civil War (2016)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "WandaVision (2021)"
        ],
        stats: {
            strength: 80,
            speed: 75,
            intelligence: 95,
            abilities: 85,
            combat: 65,
            durability: 85
        }
    },
    "Ant-Man": {
        id: "ant-man",
        name: "Ant-Man",
        universe: "marvel",
        category: "avengers",
        real_name: "Scott Lang",
        image: "ant-man.jpg",
        description: "Hero with the ability to shrink and communicate with insects.",
        powers: [
            "Size Manipulation",
            "Insect Communication",
            "Superhuman Strength (at small size)",
            "Pym Particles",
            "Agility"
        ],
        timeline: {
            first_appearance: "Ant-Man (2015)",
            born: "1969"
        },
        movie_appearances: [
            "Ant-Man (2015)",
            "Captain America: Civil War (2016)",
            "Ant-Man and the Wasp (2018)",
            "Avengers: Endgame (2019)"
        ],
        stats: {
            strength: 75,
            speed: 70,
            intelligence: 80,
            abilities: 70,
            combat: 70,
            durability: 60
        }
    },
    "Wasp": {
        id: "wasp",
        name: "Wasp",
        universe: "marvel",
        category: "avengers",
        real_name: "Hope van Dyne",
        image: "wasp.jpg",
        description: "Flying wasp-themed hero with bio-electric blasts.",
        powers: [
            "Size Manipulation",
            "Flight",
            "Bio-Electric Blasts",
            "Pym Particles",
            "Agility"
        ],
        timeline: {
            first_appearance: "Ant-Man (2015)",
            born: "Unknown"
        },
        movie_appearances: [
            "Ant-Man (2015)",
            "Captain America: Civil War (2016)",
            "Ant-Man and the Wasp (2018)",
            "Avengers: Endgame (2019)"
        ],
        stats: {
            strength: 65,
            speed: 85,
            intelligence: 75,
            abilities: 75,
            combat: 65,
            durability: 60
        }
    },
    
    // GUARDIANS OF THE GALAXY
    "Star-Lord": {
        id: "star-lord",
        name: "Star-Lord",
        universe: "marvel",
        category: "guardians",
        real_name: "Peter Quill",
        image: "star-lord.jpg",
        description: "Half-human, half-Celestial leader of the Guardians.",
        powers: [
            "Celestial Heritage",
            "Expert Pilot",
            "Master Tactician",
            "Element Gun",
            "Immunity to Energy Absorption"
        ],
        timeline: {
            first_appearance: "Guardians of the Galaxy (2014)",
            born: "1980"
        },
        movie_appearances: [
            "Guardians of the Galaxy (2014)",
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Guardians of the Galaxy Vol. 3 (2023)"
        ],
        stats: {
            strength: 60,
            speed: 70,
            intelligence: 75,
            abilities: 65,
            combat: 70,
            durability: 60
        }
    },
    "Gamora": {
        id: "gamora",
        name: "Gamora",
        universe: "marvel",
        category: "guardians",
        real_name: "Gamora Zen Whoberi",
        image: "gamora.jpg",
        description: "The deadliest woman in the galaxy, Thanos' adopted daughter.",
        powers: [
            "Superhuman Strength",
            "Superhuman Speed",
            "Superhuman Agility",
            "Master Martial Artist",
            "Assassin Training"
        ],
        timeline: {
            first_appearance: "Guardians of the Galaxy (2014)",
            born: "Unknown"
        },
        movie_appearances: [
            "Guardians of the Galaxy (2014)",
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)"
        ],
        stats: {
            strength: 75,
            speed: 80,
            intelligence: 70,
            abilities: 80,
            combat: 95,
            durability: 65
        }
    },
    "Rocket": {
        id: "rocket",
        name: "Rocket",
        universe: "marvel",
        category: "guardians",
        real_name: "Rocket (Raccoon)",
        image: "rocket.jpg",
        description: "Genius raccoon and master of weapons and tactics.",
        powers: [
            "Genius-Level Intellect",
            "Expert Marksman",
            "Weapons Expert",
            "Tactical Planning",
            "Enhanced Senses"
        ],
        timeline: {
            first_appearance: "Guardians of the Galaxy (2014)",
            born: "Unknown"
        },
        movie_appearances: [
            "Guardians of the Galaxy (2014)",
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Guardians of the Galaxy Vol. 3 (2023)"
        ],
        stats: {
            strength: 45,
            speed: 60,
            intelligence: 95,
            abilities: 70,
            combat: 75,
            durability: 50
        }
    },
    "Groot": {
        id: "groot",
        name: "Groot",
        universe: "marvel",
        category: "guardians",
        real_name: "Groot",
        image: "groot.jpg",
        description: "Sentient tree being with incredible strength and regenerative abilities.",
        powers: [
            "Superhuman Strength",
            "Regenerative Healing",
            "Wood Manipulation",
            "Durability",
            "Root Generation"
        ],
        timeline: {
            first_appearance: "Guardians of the Galaxy (2014)",
            born: "Unknown"
        },
        movie_appearances: [
            "Guardians of the Galaxy (2014)",
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Guardians of the Galaxy Vol. 3 (2023)"
        ],
        stats: {
            strength: 95,
            speed: 40,
            intelligence: 50,
            abilities: 60,
            combat: 50,
            durability: 90
        }
    },
    "Drax": {
        id: "drax",
        name: "Drax",
        universe: "marvel",
        category: "guardians",
        real_name: "Drax the Destroyer",
        image: "drax.jpg",
        description: "Powerful warrior seeking revenge against Thanos.",
        powers: [
            "Superhuman Strength",
            "Superhuman Durability",
            "Enhanced Senses",
            "Master Combatant"
        ],
        timeline: {
            first_appearance: "Guardians of the Galaxy (2014)",
            born: "Unknown"
        },
        movie_appearances: [
            "Guardians of the Galaxy (2014)",
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Guardians of the Galaxy Vol. 3 (2023)"
        ],
        stats: {
            strength: 90,
            speed: 55,
            intelligence: 45,
            abilities: 50,
            combat: 80,
            durability: 85
        }
    },
    "Mantis": {
        id: "mantis",
        name: "Mantis",
        universe: "marvel",
        category: "guardians",
        real_name: "Mantis",
        image: "mantis.jpg",
        description: "Empathic alien with powerful abilities.",
        powers: [
            "Empathy",
            "Telepathy",
            "Energy Manipulation",
            "Flight",
            "Regenerative Healing"
        ],
        timeline: {
            first_appearance: "Guardians of the Galaxy Vol. 2 (2017)",
            born: "Unknown"
        },
        movie_appearances: [
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Guardians of the Galaxy Vol. 3 (2023)"
        ],
        stats: {
            strength: 30,
            speed: 50,
            intelligence: 70,
            abilities: 90,
            combat: 20,
            durability: 40
        }
    },
    "Nebula": {
        id: "nebula",
        name: "Nebula",
        universe: "marvel",
        category: "guardians",
        real_name: "Nebula",
        image: "nebula.jpg",
        description: "Cybernetic warrior and daughter of Thanos.",
        powers: [
            "Cybernetic Enhancements",
            "Superhuman Strength",
            "Superhuman Durability",
            "Weapon Integration",
            "Space Travel"
        ],
        timeline: {
            first_appearance: "Guardians of the Galaxy (2014)",
            born: "Unknown"
        },
        movie_appearances: [
            "Guardians of the Galaxy (2014)",
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)",
            "Guardians of the Galaxy Vol. 3 (2023)"
        ],
        stats: {
            strength: 70,
            speed: 65,
            intelligence: 75,
            abilities: 60,
            combat: 80,
            durability: 80
        }
    },
    
    // X-MEN
    "Wolverine": {
        id: "wolverine",
        name: "Wolverine",
        universe: "marvel",
        category: "xmen",
        real_name: "Logan",
        image: "wolverine.jpg",
        description: "Mutant with regenerative healing and adamantium claws.",
        powers: [
            "Regenerative Healing",
            "Adamantium Claws",
            "Superhuman Strength",
            "Superhuman Senses",
            "Extended Lifespan",
            "Bone Claws"
        ],
        timeline: {
            first_appearance: "X-Men (2000)",
            born: "1832"
        },
        movie_appearances: [
            "X-Men (2000)",
            "X2: X-Men United (2003)",
            "X-Men: The Last Stand (2006)",
            "X-Men Origins: Wolverine (2009)",
            "The Wolverine (2013)",
            "X-Men: Days of Future Past (2014)",
            "Logan (2017)",
            "X-Men: Dark Phoenix (2019)"
        ],
        stats: {
            strength: 85,
            speed: 75,
            intelligence: 80,
            abilities: 70,
            combat: 100,
            durability: 95
        }
    },
    "Professor X": {
        id: "professor-x",
        name: "Professor X",
        universe: "marvel",
        category: "xmen",
        real_name: "Charles Xavier",
        image: "professor x.jpg",
        description: "Most powerful telepath and founder of the X-Men.",
        powers: [
            "Telepathy",
            "Telekinesis",
            "Mind Control",
            "Psychic Shield",
            "Astral Projection"
        ],
        timeline: {
            first_appearance: "X-Men (2000)",
            born: "1932"
        },
        movie_appearances: [
            "X-Men (2000)",
            "X2: X-Men United (2003)",
            "X-Men: The Last Stand (2006)",
            "X-Men: First Class (2011)",
            "X-Men: Days of Future Past (2014)",
            "X-Men: Apocalypse (2016)",
            "Dark Phoenix (2019)"
        ],
        stats: {
            strength: 30,
            speed: 25,
            intelligence: 100,
            abilities: 100,
            combat: 20,
            durability: 40
        }
    },
    "Magneto": {
        id: "magneto",
        name: "Magneto",
        universe: "marvel",
        category: "xmen",
        real_name: "Erik Lehnsherr",
        image: "magneto.jpg",
        description: "Master of magnetism and mutant supremacist.",
        powers: [
            "Magnetism Manipulation",
            "Metal Manipulation",
            "Electromagnetic Pulse",
            "Flight",
            "Force Fields"
        ],
        timeline: {
            first_appearance: "X-Men (2000)",
            born: "1930"
        },
        movie_appearances: [
            "X-Men (2000)",
            "X2: X-Men United (2003)",
            "X-Men: The Last Stand (2006)",
            "X-Men: First Class (2011)",
            "X-Men: Days of Future Past (2014)",
            "X-Men: Apocalypse (2016)",
            "Dark Phoenix (2019)"
        ],
        stats: {
            strength: 75,
            speed: 60,
            intelligence: 95,
            abilities: 95,
            combat: 70,
            durability: 70
        }
    },
    "Deadpool": {
        id: "deadpool",
        name: "Deadpool",
        universe: "marvel",
        category: "xmen",
        real_name: "Wade Wilson",
        image: "deapool.jpg",
        description: "Merc with a mouth and regenerative healing factor.",
        powers: [
            "Regenerative Healing",
            "Superhuman Agility",
            "Master Martial Artist",
            "Expert Marksman",
            "Immortality"
        ],
        timeline: {
            first_appearance: "Deadpool (2016)",
            born: "Unknown"
        },
        movie_appearances: [
            "Deadpool (2016)",
            "Deadpool 2 (2018)",
            "Deadpool & Wolverine (2024)"
        ],
        stats: {
            strength: 70,
            speed: 80,
            intelligence: 85,
            abilities: 75,
            combat: 95,
            durability: 85
        }
    },
    
    // VILLAINS
    "Thanos": {
        id: "thanos",
        name: "Thanos",
        universe: "marvel",
        category: "villains",
        real_name: "Thanos",
        image: "thanos.jpg",
        description: "The Mad Titan who sought the Infinity Stones.",
        powers: [
            "Superhuman Strength",
            "Superhuman Durability",
            "Energy Manipulation",
            "Telepathy",
            "Immortality",
            "Cosmic Awareness"
        ],
        timeline: {
            first_appearance: "The Avengers (2012)",
            born: "Unknown (Billions of years)"
        },
        movie_appearances: [
            "The Avengers (2012)",
            "Guardians of the Galaxy (2014)",
            "Avengers: Infinity War (2018)",
            "Avengers: Endgame (2019)"
        ],
        stats: {
            strength: 100,
            speed: 75,
            intelligence: 95,
            abilities: 90,
            combat: 95,
            durability: 100
        }
    },
    "Loki": {
        id: "loki",
        name: "Loki",
        universe: "marvel",
        category: "villains",
        real_name: "Loki Laufeyson",
        image: "loki.jpg",
        description: "God of Mischief and Thor's adoptive brother.",
        powers: [
            "Magic Manipulation",
            "Illusion Casting",
            "Shape-Shifting",
            "Superhuman Strength",
            "Telekinesis",
            "Durability"
        ],
        timeline: {
            first_appearance: "Thor (2011)",
            born: "Unknown (Thousands of years)"
        },
        movie_appearances: [
            "Thor (2011)",
            "The Avengers (2012)",
            "Thor: The Dark World (2013)",
            "Thor: Ragnarok (2017)",
            "Avengers: Infinity War (2018)",
            "Loki (2021)",
            "Thor: Love and Thunder (2022)"
        ],
        stats: {
            strength: 80,
            speed: 70,
            intelligence: 90,
            abilities: 95,
            combat: 80,
            durability: 75
        }
    },
    "Ultron": {
        id: "ultron",
        name: "Ultron",
        universe: "marvel",
        category: "villains",
        real_name: "Ultron Prime",
        image: "ultron.jpg",
        description: "AI villain created by Tony Stark with a vision of extinction.",
        powers: [
            "Artificial Intelligence",
            "Superhuman Strength",
            "Flight",
            "Energy Projection",
            "Hacking",
            "Body Hopping"
        ],
        timeline: {
            first_appearance: "Avengers: Age of Ultron (2015)",
            born: "2015"
        },
        movie_appearances: [
            "Avengers: Age of Ultron (2015)",
            "Avengers: Age of Ultron (2015)",
            "What If...? (2021)"
        ],
        stats: {
            strength: 85,
            speed: 80,
            intelligence: 100,
            abilities: 85,
            combat: 70,
            durability: 90
        }
    },
    "Green Goblin": {
        id: "green-goblin",
        name: "Green Goblin",
        universe: "marvel",
        category: "villains",
        real_name: "Norman Osborn",
        image: "green goblin.jpg",
        description: "Psychotic villain with enhanced strength and glider.",
        powers: [
            "Superhuman Strength",
            "Enhanced Durability",
            "Glider Flight",
            "Pumpkin Bomb",
            "Genius-Level Intellect"
        ],
        timeline: {
            first_appearance: "Spider-Man (2002)",
            born: "Unknown"
        },
        movie_appearances: [
            "Spider-Man (2002)",
            "Spider-Man 2 (2004)",
            "Spider-Man 3 (2007)",
            "The Amazing Spider-Man 2 (2014)",
            "Spider-Man: No Way Home (2021)"
        ],
        stats: {
            strength: 70,
            speed: 75,
            intelligence: 90,
            abilities: 75,
            combat: 80,
            durability: 65
        }
    }
};

function getAllCharacters() {
    return Object.values(CHARACTERS);
}

function getCharacterById(characterId) {
    for (const char of Object.values(CHARACTERS)) {
        if (char.id === characterId) {
            return char;
        }
    }
    return null;
}

function getCharacterByName(name) {
    return CHARACTERS[name] || null;
}

function getCharactersByCategory(category) {
    return getAllCharacters().filter(char => char.category === category);
}

function getCategories() {
    return Object.values(CATEGORIES);
}

function getCategoryById(categoryId) {
    return CATEGORIES[categoryId] || null;
}

function getUniverseInfo() {
    return UNIVERSE_CONFIG;
}

module.exports = {
    UNIVERSE_CONFIG,
    CATEGORIES,
    CHARACTERS,
    getAllCharacters,
    getCharacterById,
    getCharacterByName,
    getCharactersByCategory,
    getCategories,
    getCategoryById,
    getUniverseInfo
};
