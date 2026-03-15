/**
 * 🌌 MULTIVERSE HUB - CINEMATIC JAVASCRIPT
 * Handles all frontend interactions, animations, and features
 */

// ========== GLOBAL STATE ==========
const AppState = {
  theme: localStorage.getItem('theme') || 'dark',
  universe: 'marvel',
  userInteractions: {
    clicks: {},
    categories: {},
    comparisons: 0,
    favorites: 0
  },
  achievements: JSON.parse(localStorage.getItem('achievements')) || {
    explorer: false,
    ultimateFan: false,
    multiverseMaster: false
  },
  universesVisited: JSON.parse(localStorage.getItem('universesVisited')) || [],
  logoClicks: 0,
  scrollSpeed: 0,
  lastScrollTime: 0,
  introShown: sessionStorage.getItem('introShown') === 'true'
};

// ========== INITIALIZATION ==========
document.addEventListener('DOMContentLoaded', () => {
  initializeApp();
});

function initializeApp() {
  // Apply saved theme
  applyTheme(AppState.theme);
  
  // Show intro if not shown yet
  if (!AppState.introShown) {
    showCinematicIntro();
  } else {
    // Initialize particles
    createParticles();
  }
  
  // Setup event listeners
  setupEventListeners();
  
  // Initialize achievements display
  updateAchievementsDisplay();
}

// ========== CINEMATIC INTRO ==========
function showCinematicIntro() {
  const introOverlay = document.getElementById('introOverlay');
  if (!introOverlay) return;
  
  // Create intro particles
  createIntroParticles();
  
  // Show intro
  introOverlay.classList.remove('hidden');
  
  // Mark as shown
  sessionStorage.setItem('introShown', 'true');
  AppState.introShown = true;
  
  // Hide intro after animation completes
  setTimeout(() => {
    introOverlay.classList.add('hidden');
    createParticles(); // Start main particles
  }, 5000);
}

function createIntroParticles() {
  const container = document.getElementById('introParticles');
  if (!container) return;
  
  const particleCount = 50;
  
  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.className = 'intro-particle';
    
    // Random position
    const x = Math.random() * 100;
    const y = Math.random() * 100;
    
    // Random direction
    const tx = (Math.random() - 0.5) * 500;
    const ty = (Math.random() - 0.5) * 500;
    
    particle.style.left = `${x}%`;
    particle.style.top = `${y}%`;
    particle.style.setProperty('--tx', `${tx}px`);
    particle.style.setProperty('--ty', `${ty}px`);
    particle.style.animationDelay = `${Math.random() * 0.5}s`;
    
    container.appendChild(particle);
  }
}

// ========== PARTICLES BACKGROUND ==========
function createParticles() {
  const container = document.querySelector('.particles');
  if (!container) return;
  
  // Clear existing
  container.innerHTML = '';
  
  const particleCount = 50;
  
  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.left = `${Math.random() * 100}%`;
    particle.style.animationDelay = `${Math.random() * 15}s`;
    particle.style.animationDuration = `${10 + Math.random() * 10}s`;
    
    container.appendChild(particle);
  }
}

// ========== REALITY SHIFT ANIMATION ==========
function triggerRealityShift(universe) {
  const shift = document.getElementById('realityShift');
  if (!shift) return;
  
  // Set universe color
  const colors = {
    marvel: 'rgba(230, 36, 41, 0.8)',
    anime: 'rgba(30, 144, 255, 0.8)',
    telugu: 'rgba(212, 175, 55, 0.8)'
  };
  
  shift.style.background = colors[universe] || colors.marvel;
  shift.classList.add('active');
  
  // Track universe visit for achievement
  if (!AppState.universesVisited.includes(universe)) {
    AppState.universesVisited.push(universe);
    localStorage.setItem('universesVisited', JSON.stringify(AppState.universesVisited));
    checkExplorerAchievement();
  }
  
  // Set current universe
  AppState.universe = universe;
  document.body.setAttribute('data-universe', universe);
  
  // Remove active class after animation
  setTimeout(() => {
    shift.classList.remove('active');
  }, 1000);
}

// ========== THEME TOGGLE ==========
function toggleTheme() {
  AppState.theme = AppState.theme === 'dark' ? 'light' : 'dark';
  localStorage.setItem('theme', AppState.theme);
  applyTheme(AppState.theme);
}

function applyTheme(theme) {
  document.body.setAttribute('data-theme', theme);
  
  const toggle = document.getElementById('themeToggle');
  if (toggle) {
    toggle.classList.toggle('dark', theme === 'light');
  }
}

// ========== EVENT LISTENERS ==========
function setupEventListeners() {
  // Theme toggle
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
  
  // Logo click for chaos mode
  const logo = document.getElementById('navBrand') || document.querySelector('.title');
  if (logo) {
    logo.addEventListener('click', handleLogoClick);
  }
  
  // Search input for easter eggs
  const searchInput = document.getElementById('heroSearch');
  if (searchInput) {
    searchInput.addEventListener('input', handleSearchInput);
  }
  
  // Fast scroll detection
  window.addEventListener('scroll', handleScroll);
  
  // Scroll reveal animations
  setupScrollReveal();
}

// ========== LOGO CLICK - CHAOS MODE ==========
function handleLogoClick() {
  AppState.logoClicks++;
  
  if (AppState.logoClicks >= 5) {
    activateChaosMode();
    AppState.logoClicks = 0;
  }
}

function activateChaosMode() {
  document.body.classList.add('chaos-mode');
  
  // Show notification
  showNotification('🌈 MULTIVERSE CHAOS MODE ACTIVATED!', 'warning');
  
  // Deactivate after 10 seconds
  setTimeout(() => {
    document.body.classList.remove('chaos-mode');
    showNotification('Chaos Mode Deactivated', 'info');
  }, 10000);
}

// ========== SEARCH EASTER EGGS ==========
function handleSearchInput(e) {
  const query = e.target.value.toLowerCase();
  
  // Thanos snap easter egg
  if (query === 'thanos') {
    triggerThanosSnap();
  }
}

function triggerThanosSnap() {
  // Create snap overlay
  const overlay = document.createElement('div');
  overlay.className = 'snap-effect';
  overlay.innerHTML = '<div class="snap-text">💫 PERFECTLY BALANCED</div>';
  document.body.appendChild(overlay);
  
  // Fade out half the cards
  const cards = document.querySelectorAll('.hero-card');
  const halfLength = Math.floor(cards.length / 2);
  
  // Randomly select half
  const indices = Array.from({ length: cards.length }, (_, i) => i);
  const selectedIndices = [];
  
  for (let i = 0; i < halfLength; i++) {
    const randomIndex = Math.floor(Math.random() * indices.length);
    selectedIndices.push(indices.splice(randomIndex, 1)[0]);
  }
  
  setTimeout(() => {
    cards.forEach((card, index) => {
      if (selectedIndices.includes(index)) {
        card.classList.add('half-fade');
      }
    });
  }, 500);
  
  // Remove overlay
  setTimeout(() => {
    overlay.remove();
  }, 2000);
  
  // Restore cards after 5 seconds
  setTimeout(() => {
    cards.forEach(card => {
      card.classList.remove('half-fade');
    });
  }, 5000);
}

// ========== FAST SCROLL - LIGHTNING EFFECT ==========
let scrollTimeout;
function handleScroll() {
  const now = Date.now();
  const timeDiff = now - AppState.lastScrollTime;
  
  if (timeDiff < 100) {
    AppState.scrollSpeed++;
    
    if (AppState.scrollSpeed > 5 && !document.querySelector('.lightning-flash')) {
      triggerLightningFlash();
    }
  } else {
    AppState.scrollSpeed = 0;
  }
  
  AppState.lastScrollTime = now;
  
  clearTimeout(scrollTimeout);
  scrollTimeout = setTimeout(() => {
    AppState.scrollSpeed = 0;
  }, 200);
}

function triggerLightningFlash() {
  const flash = document.createElement('div');
  flash.className = 'lightning-flash';
  document.body.appendChild(flash);
  
  setTimeout(() => {
    flash.remove();
  }, 200);
}

// ========== SCROLL REVEAL ANIMATIONS ==========
function setupScrollReveal() {
  const reveals = document.querySelectorAll('.reveal');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { threshold: 0.1 });
  
  reveals.forEach(el => observer.observe(el));
}

// ========== AI-LIKE RECOMMENDATIONS ==========
function trackHeroClick(heroName, category) {
  // Track clicks per category
  AppState.userInteractions.categories[category] = 
    (AppState.userInteractions.categories[category] || 0) + 1;
  
  // Store recent clicks
  const recentClicks = JSON.parse(localStorage.getItem('recentClicks')) || [];
  recentClicks.push({ hero: heroName, category, timestamp: Date.now() });
  
  // Keep only last 20
  if (recentClicks.length > 20) {
    recentClicks.shift();
  }
  
  localStorage.setItem('recentClicks', JSON.stringify(recentClicks));
}

function getRecommendations() {
  const recentClicks = JSON.parse(localStorage.getItem('recentClicks')) || [];
  
  if (recentClicks.length < 3) {
    return getDefaultRecommendations();
  }
  
  // Count category preferences
  const categoryCount = {};
  recentClicks.forEach(click => {
    categoryCount[click.category] = (categoryCount[click.category] || 0) + 1;
  });
  
  // Get dominant category
  const dominantCategory = Object.keys(categoryCount).reduce((a, b) => 
    categoryCount[a] > categoryCount[b] ? a : b
  );
  
  // Generate reason text
  const reasons = {
    Avengers: "Because you love the heroes",
    Villains: "Because you explored the dark side",
    Anime: "Because you're into anime",
    Telugu: "Because you love Telugu cinema",
    default: "Because you might like this"
  };
  
  return {
    category: dominantCategory,
    reason: reasons[dominantCategory] || reasons.default
  };
}

function getDefaultRecommendations() {
  const categories = ['Avengers', 'Villains', 'Anime', 'Telugu'];
  const randomCategory = categories[Math.floor(Math.random() * categories.length)];
  
  return {
    category: randomCategory,
    reason: "Trending now"
  };
}

function displayRecommendations() {
  const recommendations = getRecommendations();
  const container = document.getElementById('recommendationsContainer');
  const reasonText = document.getElementById('recommendationReason');
  
  if (reasonText) {
    reasonText.textContent = recommendations.reason;
  }
  
  // Fetch and display recommended heroes
  // Map category names to universe/category pairs
  let universe = 'marvel';
  let category = recommendations.category.toLowerCase();
  
  // For universe-level categories, use 'all' to get all heroes
  if (category === 'anime' || category === 'telugu') {
    universe = category;
    category = 'all';
  }
  
  fetch(`/category-heroes/${universe}/${category}`)
    .then(res => res.json())
    .then(heroes => {
      const shuffled = heroes.sort(() => 0.5 - Math.random()).slice(0, 6);
      renderRecommendationCards(shuffled);
    });
}

function renderRecommendationCards(heroes) {
  const container = document.getElementById('recommendationsScroll');
  if (!container) return;
  
  container.innerHTML = heroes.map(hero => `
    <div class="recommendation-card" onclick="navigateToHero('${hero.name}')">
      <img src="/static/assets/${getHeroImage(hero.name)}" alt="${hero.name}">
      <div class="hero-card-overlay">
        <div class="hero-card-name">${hero.name}</div>
      </div>
    </div>
  `).join('');
}

// ========== ACHIEVEMENTS SYSTEM ==========
function checkExplorerAchievement() {
  if (AppState.achievements.explorer) return;
  
  if (AppState.universesVisited.length >= 3) {
    unlockAchievement('explorer', '🏅 Explorer Badge');
  }
}

function checkUltimateFanAchievement() {
  if (AppState.achievements.ultimateFan) return;
  
  if (AppState.userInteractions.favorites >= 20) {
    unlockAchievement('ultimateFan', '🔥 Ultimate Fan');
  }
}

function checkMultiverseMasterAchievement() {
  if (AppState.achievements.multiverseMaster) return;
  
  if (AppState.userInteractions.comparisons >= 10) {
    unlockAchievement('multiverseMaster', '💎 Multiverse Master');
  }
}

function unlockAchievement(id, name) {
  AppState.achievements[id] = true;
  localStorage.setItem('achievements', JSON.stringify(AppState.achievements));
  
  showNotification(`🎉 Achievement Unlocked: ${name}!`, 'success');
  updateAchievementsDisplay();
}

function updateAchievementsDisplay() {
  const badges = document.querySelectorAll('.achievement-badge');
  
  badges.forEach(badge => {
    const badgeId = badge.dataset.badge;
    if (AppState.achievements[badgeId]) {
      badge.classList.remove('locked');
      badge.classList.add('unlocked');
    } else {
      badge.classList.add('locked');
      badge.classList.remove('unlocked');
    }
  });
}

// ========== COMPARISON TOOL ==========
function compareHeroes() {
  const hero1 = document.getElementById('compareHero1').value;
  const hero2 = document.getElementById('compareHero2').value;
  
  if (!hero1 || !hero2) {
    showNotification('Please select two heroes to compare', 'warning');
    return;
  }
  
  // Track comparison for achievement
  AppState.userInteractions.comparisons++;
  checkMultiverseMasterAchievement();
  
  // Fetch hero data
  Promise.all([
    fetch(`/hero-movies/${hero1}`).then(r => r.json()),
    fetch(`/hero-movies/${hero2}`).then(r => r.json())
  ]).then(([data1, data2]) => {
    displayComparison(data1, data2);
  });
}

function displayComparison(hero1, hero2) {
  const container = document.getElementById('comparisonResults');
  if (!container) return;
  
  const stats = ['Power', 'Intelligence', 'Speed', 'Strength', 'Popularity'];
  
  container.innerHTML = `
    <div class="compare-hero">
      <h3>${hero1.name || 'Hero 1'}</h3>
      ${stats.map(stat => createCompareBar(stat, getRandomStat(), getThemeColor())).join('')}
    </div>
    <div class="compare-hero">
      <h3>${hero2.name || 'Hero 2'}</h3>
      ${stats.map(stat => createCompareBar(stat, getRandomStat(), getThemeColor())).join('')}
    </div>
  `;
  
  container.classList.add('active');
}

function createCompareBar(stat, value, color) {
  return `
    <div class="compare-stat">
      <div class="compare-stat-label">${stat}</div>
      <div class="compare-bar-container">
        <div class="compare-bar" style="width: ${value}%; background: ${color};"></div>
      </div>
      <div class="compare-stat-value">${value}</div>
    </div>
  `;
}

function getRandomStat() {
  return Math.floor(Math.random() * 100) + 20;
}

// ========== TRENDING HEROES ==========
function loadTrendingHeroes() {
  const favorites = JSON.parse(localStorage.getItem('favorites')) || [];
  
  // Combine with click data to determine trending
  const trending = calculateTrending(favorites);
  
  displayTrendingHeroes(trending);
}

function calculateTrending(favorites) {
  // Simple trending algorithm based on favorites count
  // In real app, would track views/clicks server-side
  const heroCounts = {};
  
  favorites.forEach(hero => {
    heroCounts[hero] = (heroCounts[hero] || 0) + 1;
  });
  
  return Object.entries(heroCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([hero, count], index) => ({
      rank: index + 1,
      name: hero,
      count
    }));
}

function displayTrendingHeroes(trending) {
  const container = document.getElementById('trendingList');
  if (!container) return;
  
  if (trending.length === 0) {
    container.innerHTML = '<p class="text-center">No trending heroes yet. Add favorites!</p>';
    return;
  }
  
  container.innerHTML = trending.map(hero => `
    <div class="trending-item" onclick="navigateToHero('${hero.name}')">
      <div class="trending-rank trending-rank-${hero.rank}">
        ${hero.rank === 1 ? '👑' : hero.rank}
      </div>
      <img src="/static/assets/${getHeroImage(hero.name)}" alt="${hero.name}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 10px;">
      <div>
        <div class="hero-card-name">${hero.name}</div>
        <div class="hero-card-category">${hero.count} favorites</div>
      </div>
    </div>
  `).join('');
}

// ========== WORLD MAP ==========
function setupWorldMap() {
  const locations = document.querySelectorAll('.map-location');
  
  locations.forEach(location => {
    location.addEventListener('click', () => {
      const locationName = location.dataset.location;
      showLocationHeroes(locationName);
    });
  });
}

function showLocationHeroes(location) {
  const locationHeroes = {
    'wakanda': ['Black Panther', 'Shuri', 'Namor'],
    'new-york': ['Iron Man', 'Spider-Man', 'Doctor Strange'],
    'tokyo': ['Gojo Satoru', 'Yuji Itadori', 'Tanjiro Kamado'],
    'hyderabad': ['Prabhas', 'Allu Arjun', 'Ram Charan']
  };
  
  const heroes = locationHeroes[location] || [];
  const modal = document.getElementById('worldMapModal');
  const content = document.getElementById('worldMapContent');
  
  if (content) {
    content.innerHTML = `
      <h2>${formatLocationName(location)} Heroes</h2>
      <div class="hero-grid">
        ${heroes.map(hero => `
          <div class="hero-card" onclick="navigateToHero('${hero}')">
            <img src="/static/assets/${getHeroImage(hero)}" alt="${hero}">
            <div class="hero-card-overlay">
              <div class="hero-card-name">${hero}</div>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  }
  
  if (modal) {
    modal.classList.add('active');
  }
}

function formatLocationName(name) {
  return name.split('-').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ');
}

// ========== FAVORITES ==========
function addToFavorites(heroName) {
  fetch('/favorites', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ heroName })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      // Update local state
      AppState.userInteractions.favorites++;
      localStorage.setItem('favorites', JSON.stringify(data.favorites));
      
      // Check achievement
      checkUltimateFanAchievement();
      
      // Show notification
      showNotification(`${heroName} added to favorites! ❤️`, 'success');
      
      // Update button
      updateFavoriteButton(heroName, true);
    } else {
      showNotification(data.message || 'Please login first', 'error');
    }
  })
  .catch(err => console.error('Error:', err));
}

function removeFromFavorites(heroName) {
  fetch('/favorites/remove', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ heroName })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      localStorage.setItem('favorites', JSON.stringify(data.favorites));
      showNotification(`${heroName} removed from favorites`, 'info');
      updateFavoriteButton(heroName, false);
    }
  });
}

function updateFavoriteButton(heroName, isFavorite) {
  const btn = document.querySelector(`[data-hero="${heroName}"] .favorite-btn`);
  if (btn) {
    btn.classList.toggle('active', isFavorite);
    btn.innerHTML = isFavorite ? '❤️' : '🤍';
  }
}

// ========== NOTIFICATIONS ==========
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.innerHTML = message;
  
  document.body.appendChild(notification);
  
  // Animate in
  setTimeout(() => {
    notification.classList.add('show');
  }, 10);
  
  // Remove after delay
  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

// ========== UTILITY FUNCTIONS ==========
function getHeroImage(heroName) {
  const map = {
    'ant-man': 'ant-man.jpg',
    'Ant-Man': 'ant-man.jpg',
    'black panther': 'black panther.jpg',
    'Black Panther': 'black panther.jpg',
    'black widow': 'black widow.jpg',
    'Black Widow': 'black widow.jpg',
    'captain america': 'captain america.jpg',
    'Captain America': 'captain america.jpg',
    'captain marvel': 'captain marvel.jpg',
    'Captain Marvel': 'captain marvel.jpg',
    'deadpool': 'deapool.jpg',
    'Deadpool': 'deapool.jpg',
    'doctor octopus': 'doctor octopus.jpg',
    'Doctor Octopus': 'doctor octopus.jpg',
    'doctor strange': 'doctor strange.jpg',
    'Doctor Strange': 'doctor strange.jpg',
    'drax': 'drax.jpg',
    'Drax': 'drax.jpg',
    'falcon': 'falcon.jpg',
    'Falcon': 'falcon.jpg',
    'gamora': 'gamora.jpg',
    'Gamora': 'gamora.jpg',
    'green goblin': 'green goblin.jpg',
    'Green Goblin': 'green goblin.jpg',
    'groot': 'groot.jpg',
    'Groot': 'groot.jpg',
    'hawkeye': 'hawkeye.jpg',
    'Hawkeye': 'hawkeye.jpg',
    'hulk': 'hulk.jpg',
    'Hulk': 'hulk.jpg',
    'iron man': 'Iron-Man.jpg',
    'Iron Man': 'Iron-Man.jpg',
    'Iron-Man': 'Iron-Man.jpg',
    'loki': 'loki.jpg',
    'Loki': 'loki.jpg',
    'magneto': 'magneto.jpg',
    'Magneto': 'magneto.jpg',
    'mantis': 'mantis.jpg',
    'Mantis': 'mantis.jpg',
    'nebula': 'nebula.jpg',
    'Nebula': 'nebula.jpg',
    'professor x': 'professor x.jpg',
    'Professor X': 'professor x.jpg',
    'quicksilver': 'quicksilver.jpg',
    'Quicksilver': 'quicksilver.jpg',
    'rocket': 'rocket.jpg',
    'Rocket': 'rocket.jpg',
    'scarlet witch': 'scarlet witch.jpg',
    'Scarlet Witch': 'scarlet witch.jpg',
    'spider-man': 'spider-man.jpg',
    'Spider-Man': 'spider-man.jpg',
    'star-lord': 'star-lord.jpg',
    'Star-Lord': 'star-lord.jpg',
    'star lord': 'star-lord.jpg',
    'Star Lord': 'star-lord.jpg',
    'storm': 'storm.jpg',
    'Storm': 'storm.jpg',
    'thanos': 'thanos.jpg',
    'Thanos': 'thanos.jpg',
    'thor': 'thor.jpg',
    'Thor': 'thor.jpg',
    'ultron': 'ultron.jpg',
    'Ultron': 'ultron.jpg',
    'venom': 'venom.jpg',
    'Venom': 'venom.jpg',
    'vision': 'vision.jpg',
    'Vision': 'vision.jpg',
    'war machine': 'war machine.jpg',
    'War Machine': 'war machine.jpg',
    'wasp': 'wasp.jpg',
    'Wasp': 'wasp.jpg',
    'winter soldier': 'winter soldier.jpg',
    'Winter Soldier': 'winter soldier.jpg',
    'wolverine': 'wolverine.jpg',
    'Wolverine': 'wolverine.jpg',
  };
  
  // First try: direct match
  if (map[heroName]) {
    return map[heroName];
  }
  
  // Second try: lowercase with spaces
  const lowerSpace = heroName.toLowerCase();
  if (map[lowerSpace]) {
    return map[lowerSpace];
  }
  
  // Third try: lowercase with hyphens (spaces replaced with -)
  const lowerHyphen = lowerSpace.replace(/ /g, '-');
  if (map[lowerHyphen]) {
    return map[lowerHyphen];
  }
  
  // Fourth try: original with hyphens (for Iron-Man edge case)
  const originalHyphen = heroName.replace(/ /g, '-');
  if (map[originalHyphen]) {
    return map[originalHyphen];
  }
  
  // Fallback: use lowercase with hyphens
  return `${lowerHyphen}.jpg`;
}

function getThemeColor() {
  const colors = {
    marvel: '#e62429',
    anime: '#1e90ff',
    telugu: '#d4af37'
  };
  
  return colors[AppState.universe] || colors.marvel;
}

function navigateToHero(heroName) {
  const slug = heroName.toLowerCase().replace(/ /g, '-');
  window.location.href = `/hero/${slug}`;
}

function navigateToUniverse(universe) {
  triggerRealityShift(universe);
  setTimeout(() => {
    window.location.href = `/universe/${universe}`;
  }, 800);
}

// ========== MODAL HELPERS ==========
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
  }
}

// Close modal on outside click
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal')) {
    e.target.classList.remove('active');
  }
});

// ========== HERO CLICK TRACKING ==========
function onHeroCardClick(heroName, category) {
  trackHeroClick(heroName, category);
}

// Export functions for use in templates
window.AppState = AppState;
window.toggleTheme = toggleTheme;
window.triggerRealityShift = triggerRealityShift;
window.navigateToHero = navigateToHero;
window.navigateToUniverse = navigateToUniverse;
window.addToFavorites = addToFavorites;
window.removeFromFavorites = removeFromFavorites;
window.compareHeroes = compareHeroes;
window.showLocationHeroes = showLocationHeroes;
window.openModal = openModal;
window.closeModal = closeModal;
window.onHeroCardClick = onHeroCardClick;
window.displayRecommendations = displayRecommendations;
window.loadTrendingHeroes = loadTrendingHeroes;
window.setupWorldMap = setupWorldMap;
