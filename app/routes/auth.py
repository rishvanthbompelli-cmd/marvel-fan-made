"""Authentication and favorites routes."""

from flask import Blueprint, render_template, jsonify, request, session, redirect
from app.data import get_all_characters, get_character_by_id_any_universe
import re
import random

# Create Blueprint
auth_bp = Blueprint('auth', __name__)


# Database connection (will be set by app factory)
db = None
cursor = None


def init_db(db_connection, db_cursor):
    """Initialize database connection for this blueprint."""
    global db, cursor
    db = db_connection
    cursor = db_cursor


# Regex patterns
email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
phone_regex = r'^\+?[\d\s-]{10,15}$'


@auth_bp.route("/login")
def login_page():
    """Login page."""
    return render_template('login.html')


@auth_bp.route("/login", methods=["POST"])
def login():
    """Login handler - supports email, phone, or username."""
    global cursor, db
    
    data = request.get_json()
    identifier = data.get('identifier', '').strip()
    password = data.get('password', '')
    
    if not identifier or not password:
        return jsonify({'success': False, 'message': 'Please provide identifier and password'}), 400
    
    # Determine if identifier is email or phone
    is_email = re.match(email_regex, identifier)
    is_phone = re.match(phone_regex, identifier)
    
    try:
        if is_email:
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (identifier, password))
        elif is_phone:
            cursor.execute("SELECT * FROM users WHERE phone = %s AND password = %s", (identifier, password))
        else:
            # Try username
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (identifier, password))
        
        user = cursor.fetchone()
        
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['email'] = user[2]
            session['phone'] = user[3]
            
            # Initialize favorites if not present
            if 'favorites' not in session:
                session['favorites'] = []
            
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2]
                }
            })
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
            
    except Exception as e:
        # If database error, fall back to session-based auth
        if identifier == 'admin' and password == 'admin':
            session['user_id'] = 1
            session['username'] = 'admin'
            session['email'] = 'admin@marvel.com'
            if 'favorites' not in session:
                session['favorites'] = []
            return jsonify({'success': True, 'message': 'Login successful (demo mode)'})
        
        return jsonify({'success': False, 'message': f'Login failed: {str(e)}'}), 500


@auth_bp.route("/logout", methods=["POST", "GET"])
def logout():
    """Logout handler."""
    session.clear()
    return redirect('/')


@auth_bp.route("/check-session")
def check_session():
    """Check if user is logged in."""
    if 'user_id' in session:
        return jsonify({
            'logged_in': True,
            'user': {
                'username': session.get('username'),
                'email': session.get('email')
            }
        })
    else:
        return jsonify({'logged_in': False})


@auth_bp.route("/send-otp", methods=["POST"])
def send_otp():
    """Send OTP for verification."""
    data = request.get_json()
    phone = data.get('phone', '').strip()
    
    if not phone:
        return jsonify({'success': False, 'message': 'Phone number required'}), 400
    
    # Generate random OTP
    otp = str(random.randint(100000, 999999))
    
    # Store OTP in session (in real app, send via SMS)
    session['otp'] = otp
    session['otp_phone'] = phone
    
    # In production, integrate with SMS service
    # For demo, return OTP
    return jsonify({
        'success': True,
        'message': 'OTP sent successfully',
        'demo_otp': otp  # Remove in production
    })


@auth_bp.route("/verify-otp", methods=["POST"])
def verify_otp():
    """Verify OTP and complete login."""
    data = request.get_json()
    otp = data.get('otp', '').strip()
    phone = data.get('phone', '').strip()
    
    stored_otp = session.get('otp')
    stored_phone = session.get('otp_phone')
    
    if otp == stored_otp and phone == stored_phone:
        # Create or get user
        global cursor, db
        
        try:
            cursor.execute("SELECT * FROM users WHERE phone = %s", (phone,))
            user = cursor.fetchone()
            
            if not user:
                # Create new user
                username = f"user_{phone[-4:]}"
                cursor.execute(
                    "INSERT INTO users (username, email, phone, password) VALUES (%s, %s, %s, %s)",
                    (username, f"{username}@example.com", phone, "otp_auth")
                )
                db.commit()
                cursor.execute("SELECT * FROM users WHERE phone = %s", (phone,))
                user = cursor.fetchone()
            
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['email'] = user[2]
            session['phone'] = user[3]
            
            if 'favorites' not in session:
                session['favorites'] = []
            
            # Clear OTP
            session.pop('otp', None)
            session.pop('otp_phone', None)
            
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'id': user[0],
                    'username': user[1]
                }
            })
            
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 500
    else:
        return jsonify({'success': False, 'message': 'Invalid OTP'}), 401


# Favorites Routes
@auth_bp.route("/favorites", methods=["GET"])
def get_favorites():
    """Get user's favorite characters."""
    if 'user_id' not in session:
        return jsonify({'favorites': []})
    
    favorites = session.get('favorites', [])
    
    # Get full character data for each favorite
    favorite_characters = []
    for char_id in favorites:
        character = get_character_by_id_any_universe(char_id)
        if character:
            favorite_characters.append({
                'id': character['id'],
                'name': character['name'],
                'universe': character['universe'],
                'category': character['category'],
                'image': character.get('image', '')
            })
    
    return jsonify({'favorites': favorite_characters})


@auth_bp.route("/favorites", methods=["POST"])
def add_favorite():
    """Add a character to favorites."""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Please login first'}), 401
    
    data = request.get_json()
    character_id = data.get('character_id')
    
    if not character_id:
        return jsonify({'success': False, 'message': 'Character ID required'}), 400
    
    # Check if character exists
    character = get_character_by_id_any_universe(character_id)
    if not character:
        return jsonify({'success': False, 'message': 'Character not found'}), 404
    
    # Add to favorites
    favorites = session.get('favorites', [])
    if character_id not in favorites:
        favorites.append(character_id)
        session['favorites'] = favorites
        
        # Also save to database if available
        global cursor, db
        try:
            if 'user_id' in session:
                cursor.execute(
                    "INSERT INTO favorites (user_id, character_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE character_id=character_id",
                    (session['user_id'], character_id)
                )
                db.commit()
        except:
            pass  # Ignore database errors
    
    return jsonify({
        'success': True,
        'message': f'{character["name"]} added to favorites',
        'favorites_count': len(favorites)
    })


@auth_bp.route("/favorites/remove", methods=["POST"])
def remove_favorite():
    """Remove a character from favorites."""
    data = request.get_json()
    character_id = data.get('character_id')
    
    if not character_id:
        return jsonify({'success': False, 'message': 'Character ID required'}), 400
    
    # Remove from favorites
    favorites = session.get('favorites', [])
    if character_id in favorites:
        favorites.remove(character_id)
        session['favorites'] = favorites
        
        # Also remove from database if available
        global cursor, db
        try:
            if 'user_id' in session:
                cursor.execute(
                    "DELETE FROM favorites WHERE user_id = %s AND character_id = %s",
                    (session['user_id'], character_id)
                )
                db.commit()
        except:
            pass  # Ignore database errors
    
    return jsonify({
        'success': True,
        'message': 'Removed from favorites',
        'favorites_count': len(favorites)
    })


@auth_bp.route("/favorites/check/<character_id>")
def check_favorite(character_id):
    """Check if a character is in favorites."""
    favorites = session.get('favorites', [])
    is_favorite = character_id in favorites
    
    return jsonify({
        'character_id': character_id,
        'is_favorite': is_favorite
    })
