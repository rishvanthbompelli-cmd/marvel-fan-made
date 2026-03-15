// Data package for character information across all universes
const marvel = require('./marvel');

// Placeholder data for anime and telugu (can be expanded later)
const anime = {
    UNIVERSE_CONFIG: {
        id: "anime",
        name: "Anime Universe",
        description: "Characters from popular anime series.",
        color: "#FF6B6B",
        logo: "/static/assets/anime-logo.png"
    },
    getAllCharacters: () => [],
    getCharacterById: (id) => null,
    getCharactersByCategory: (category) => [],
    getCategories: () => [],
    getUniverseInfo: () => this.UNIVERSE_CONFIG
};

const telugu = {
    UNIVERSE_CONFIG: {
        id: "telugu",
        name: "Telugu Cinema",
        description: "Characters from popular Telugu movies.",
        color: "#D4AF37",
        logo: "/static/assets/telugu-logo.png"
    },
    getAllCharacters: () => [],
    getCharacterById: (id) => null,
    getCharactersByCategory: (category) => [],
    getCategories: () => [],
    getUniverseInfo: () => this.UNIVERSE_CONFIG
};

function getAllUniverses() {
    return [
        marvel.UNIVERSE_CONFIG,
        anime.UNIVERSE_CONFIG,
        telugu.UNIVERSE_CONFIG
    ];
}

function getUniverseById(universeId) {
    const universes = {
        "marvel": marvel.UNIVERSE_CONFIG,
        "anime": anime.UNIVERSE_CONFIG,
        "telugu": telugu.UNIVERSE_CONFIG
    };
    return universes[universeId] || null;
}

function getAllCharacters() {
    return marvel.getAllCharacters();
}

function getCharacterByIdAnyUniverse(characterId) {
    // Check Marvel
    let character = marvel.getCharacterById(characterId);
    if (character) return character;
    
    return null;
}

function searchCharacters(query) {
    const q = query.toLowerCase();
    const results = [];
    
    const characters = marvel.getAllCharacters();
    for (const character of characters) {
        if (character.name.toLowerCase().includes(q) || 
            (character.description && character.description.toLowerCase().includes(q))) {
            results.push(character);
        }
    }
    
    return results;
}

function getCharactersByUniverse(universeId) {
    if (universeId === "marvel") {
        return marvel.getAllCharacters();
    }
    return [];
}

function getCategoriesByUniverse(universeId) {
    if (universeId === "marvel") {
        return marvel.getCategories();
    }
    return [];
}

function getCategoryCharacters(universeId, categoryId) {
    if (universeId === "marvel") {
        return marvel.getCharactersByCategory(categoryId);
    }
    return [];
}

module.exports = {
    getAllUniverses,
    getUniverseById,
    getAllCharacters,
    getCharacterByIdAnyUniverse,
    searchCharacters,
    getCharactersByUniverse,
    getCategoriesByUniverse,
    getCategoryCharacters
};
