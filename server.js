// Main Express server for Marvel Fan Made application

const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const path = require('path');
const data = require('./data');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'static')));
app.use(express.static(path.join(__dirname, 'templates')));

// Session configuration
app.use(session({
    secret: 'marvel-fan-secret-key',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }
}));

// Set view engine to serve HTML files directly
app.set('view engine', 'html');
app.set('views', path.join(__dirname, 'templates'));
app.engine('html', require('ejs').renderFile);

// Helper function to get hero image
const HERO_IMAGE_MAP = {
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
};

function getImageForHero(heroName) {
    const heroKey = heroName.toLowerCase();
    if (HERO_IMAGE_MAP[heroKey]) {
        return `/static/assets/${HERO_IMAGE_MAP[heroKey]}`;
    }
    const imageName = `${heroKey.replace(/ /g, '-')}.jpg`;
    return `/static/assets/${imageName}`;
}

// ==================== ROUTES ====================

// Home page
app.get('/', (req, res) => {
    const universes = data.getAllUniverses();
    res.render('landing.html', { universes });
});

// World page
app.get('/world', (req, res) => {
    const universes = data.getAllUniverses();
    res.render('world.html', { universes });
});

// Universe page - handles both /universe and /universe/:id
app.get('/universe', (req, res) => {
    const universes = data.getAllUniverses();
    res.render('universe.html', { 
        category: 'marvel',
        universes 
    });
});

app.get('/universe/:universeId', (req, res) => {
    const { universeId } = req.params;
    const universe = data.getUniverseById(universeId);
    
    if (!universe) {
        return res.status(404).send('Universe not found');
    }
    
    const categories = data.getCategoriesByUniverse(universeId);
    const characters = data.getCharactersByUniverse(universeId);
    
    res.render('universe.html', {
        category: universeId,
        universe,
        categories,
        characters,
        universes: data.getAllUniverses()
    });
});

// Hero detail page
app.get('/hero/:heroIdentifier', (req, res) => {
    const { heroIdentifier } = req.params;
    let character = data.getCharacterByIdAnyUniverse(heroIdentifier);
    
    if (!character) {
        // Try with hyphen/space variations
        character = data.getCharacterByIdAnyUniverse(heroIdentifier.replace(/-/g, ' ').toLowerCase());
    }
    
    if (!character) {
        return res.status(404).send('Character not found');
    }
    
    const image = getImageForHero(character.name);
    const universe = data.getUniverseById(character.universe);
    const categories = data.getCategoriesByUniverse(character.universe);
    
    // Check if favorite
    const favorites = req.session.favorites || [];
    const isFavorite = favorites.includes(character.id);
    
    res.render('hero_detail.html', {
        character,
        universe,
        categories,
        image,
        hero_image: image,
        is_favorite: isFavorite,
        universes: data.getAllUniverses()
    });
});

// Timeline page
app.get('/timeline', (req, res) => {
    res.render('timeline.html', { universes: data.getAllUniverses() });
});

// Achievements page
app.get('/achievements', (req, res) => {
    res.render('achievements.html', { universes: data.getAllUniverses() });
});

// Compare page
app.get('/compare', (req, res) => {
    res.render('compare.html', { universes: data.getAllUniverses() });
});

// Login page
app.get('/login', (req, res) => {
    res.render('login.html');
});

// ==================== API ROUTES ====================

// Get heroes by category
app.get('/category-heroes/:universe/:category', (req, res) => {
    const { universe, category } = req.params;
    
    let characters;
    if (category === 'all') {
        characters = data.getCharactersByUniverse(universe);
    } else {
        characters = data.getCategoryCharacters(universe, category);
    }
    
    const formatted = characters.map(char => ({
        id: char.id,
        name: char.name,
        category: char.category,
        image: getImageForHero(char.name),
        description: char.description || ''
    }));
    
    res.json(formatted);
});

// Search heroes
app.get('/search-heroes', (req, res) => {
    const query = req.query.q || '';
    
    if (!query) {
        return res.json([]);
    }
    
    const results = data.searchCharacters(query);
    const formatted = results.slice(0, 20).map(char => ({
        id: char.id,
        name: char.name,
        universe: char.universe,
        category: char.category,
        image: getImageForHero(char.name),
        description: (char.description || '').substring(0, 100)
    }));
    
    res.json(formatted);
});

// Get all characters API
app.get('/api/characters', (req, res) => {
    const universeId = req.query.universe;
    
    let characters;
    if (universeId) {
        characters = data.getCharactersByUniverse(universeId);
    } else {
        characters = data.getAllCharacters();
    }
    
    const formatted = characters.map(char => ({
        id: char.id,
        name: char.name,
        universe: char.universe,
        category: char.category,
        image: getImageForHero(char.name),
        description: char.description || ''
    }));
    
    res.json(formatted);
});

// Get single character API
app.get('/api/character/:characterId', (req, res) => {
    const character = data.getCharacterByIdAnyUniverse(req.params.characterId);
    
    if (!character) {
        return res.status(404).json({ error: 'Character not found' });
    }
    
    res.json(character);
});

// Get universes API
app.get('/api/universes', (req, res) => {
    res.json(data.getAllUniverses());
});

// Get universe API
app.get('/api/universe/:universeId', (req, res) => {
    const universe = data.getUniverseById(req.params.universeId);
    
    if (!universe) {
        return res.status(404).json({ error: 'Universe not found' });
    }
    
    const categories = data.getCategoriesByUniverse(req.params.universeId);
    const characters = data.getCharactersByUniverse(req.params.universeId);
    
    res.json({
        universe,
        categories,
        character_count: characters.length
    });
});

// ==================== FAVORITES ROUTES ====================

// Toggle favorite
app.post('/toggle-favorite', (req, res) => {
    const { heroName, action } = req.body;
    
    if (!req.session.favorites) {
        req.session.favorites = [];
    }
    
    const favorites = req.session.favorites;
    const index = favorites.indexOf(heroName);
    
    if (action === 'add' && index === -1) {
        favorites.push(heroName);
    } else if (action === 'remove' && index > -1) {
        favorites.splice(index, 1);
    }
    
    req.session.favorites = favorites;
    res.json({ success: true, favorites });
});

// Logout
app.get('/logout', (req, res) => {
    req.session.destroy();
    res.redirect('/');
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

module.exports = app;
