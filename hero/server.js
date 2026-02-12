const express = require('express');
const mysql = require('mysql2/promise');
const app = express();
const PORT = 3000;

// Database connection
const db = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'sura123',
  database: 'otp_login',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

app.use(express.json());
app.use(express.static('static'));
app.use(express.static('templates'));

// Session store (in production, use Redis or similar)
const sessions = new Map();

// Login endpoint with email validation
app.post('/login', async (req, res) => {
  try {
    const { fullName, emailPhone, favoriteHero } = req.body;

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^\+?[\d\s-]{10,}$/;

    let loginType = '';
    let identifier = emailPhone;

    if (emailRegex.test(emailPhone)) {
      loginType = 'email';
      // Validate email domain
      const domain = emailPhone.split('@')[1].toLowerCase();
      if (domain !== 'gmail.com') {
        return res.json({ 
          success: false, 
          message: 'Please use a valid Gmail address (@gmail.com)' 
        });
      }
    } else if (phoneRegex.test(emailPhone)) {
      loginType = 'phone';
    } else {
      return res.json({ 
        success: false, 
        message: 'Please enter a valid email or phone number' 
      });
    }

    // Save user to database
    const [result] = await db.execute(
      'INSERT INTO users (name, email, phone, favorite_hero) VALUES (?, ?, ?, ?) ON DUPLICATE KEY UPDATE name = VALUES(name), favorite_hero = VALUES(favorite_hero)',
      [fullName, loginType === 'email' ? emailPhone : null, loginType === 'phone' ? emailPhone : null, favoriteHero]
    );

    // Create session
    const sessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    sessions.set(sessionId, {
      fullName,
      email: loginType === 'email' ? emailPhone : null,
      phone: loginType === 'phone' ? emailPhone : null,
      favoriteHero,
      loginTime: new Date()
    });

    res.json({ 
      success: true, 
      message: `Welcome to the Marvel Universe, ${fullName}!`,
      sessionId
    });

  } catch (error) {
    console.error('Login error:', error);
    res.json({ success: false, message: 'Login failed. Please try again.' });
  }
});

// Logout endpoint
app.post('/logout', (req, res) => {
  const { sessionId } = req.body;
  if (sessionId && sessions.has(sessionId)) {
    sessions.delete(sessionId);
  }
  res.json({ success: true, message: 'Logged out successfully' });
});

// Check session
app.get('/check-session', (req, res) => {
  const sessionId = req.headers['session-id'];
  if (sessionId && sessions.has(sessionId)) {
    res.json({ authenticated: true, user: sessions.get(sessionId) });
  } else {
    res.json({ authenticated: false });
  }
});

// Hero search endpoint
app.get('/search-heroes', (req, res) => {
  const { q } = req.query;
  const heroes = [
    { id: 1, name: 'Iron Man', category: 'Avengers' },
    { id: 2, name: 'Captain America', category: 'Avengers' },
    { id: 3, name: 'Thor', category: 'Avengers' },
    { id: 4, name: 'Hulk', category: 'Avengers' },
    { id: 5, name: 'Black Widow', category: 'Avengers' },
    { id: 6, name: 'Hawkeye', category: 'Avengers' },
    { id: 7, name: 'Scarlet Witch', category: 'Avengers' },
    { id: 8, name: 'Vision', category: 'Avengers' },
    { id: 9, name: 'Spider-Man', category: 'Spider-Man' },
    { id: 10, name: 'Doctor Strange', category: 'Mystic' },
    { id: 11, name: 'Black Panther', category: 'Wakanda' },
    { id: 12, name: 'Captain Marvel', category: 'Cosmic' },
    { id: 13, name: 'Thanos', category: 'Villains' },
    { id: 14, name: 'Loki', category: 'Villains' },
    { id: 15, name: 'Deadpool', category: 'X-Men' },
    { id: 16, name: 'Wolverine', category: 'X-Men' },
    { id: 17, name: 'Star-Lord', category: 'Guardians' },
    { id: 18, name: 'Gamora', category: 'Guardians' },
    { id: 19, name: 'Rocket', category: 'Guardians' },
    { id: 20, name: 'Groot', category: 'Guardians' }
  ];

  if (q) {
    const filtered = heroes.filter(h => 
      h.name.toLowerCase().includes(q.toLowerCase())
    );
    return res.json(filtered);
  }
  res.json(heroes);
});

// Serve main pages
app.get('/', (req, res) => {
  res.sendFile('templates/login.html');
});

app.get('/hero', (req, res) => {
  res.sendFile('templates/hero.html');
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
