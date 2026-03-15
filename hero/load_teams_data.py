#!/usr/bin/env python3
"""
Marvel Teams Data Loader
Loads team and character data from JSON into MySQL database
Run: python hero/load_teams_data.py
"""

import json
import mysql.connector
import os

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sura123',
    'database': 'otp_login'
}

def load_json_data():
    """Load data from JSON file"""
    json_path = os.path.join(os.path.dirname(__file__), 'marvel_teams_data.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_tables(cursor):
    """Create database tables if they don't exist"""
    
    # Teams table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id VARCHAR(50) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            color VARCHAR(20),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """)
    
    # Heroes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS heroes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            team_id VARCHAR(50) NOT NULL,
            role ENUM('Hero', 'Villain', 'Anti-Hero', 'Cosmic Entity') NOT NULL DEFAULT 'Hero',
            description TEXT,
            image VARCHAR(255),
            category VARCHAR(50) DEFAULT 'marvel',
            power_level INT DEFAULT 50,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE,
            INDEX idx_team (team_id),
            INDEX idx_role (role),
            INDEX idx_name (name)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """)
    
    print("✓ Tables created successfully")

def insert_teams(cursor, teams):
    """Insert team data"""
    for team in teams:
        cursor.execute("""
            INSERT IGNORE INTO teams (id, name, description, color)
            VALUES (%s, %s, %s, %s)
        """, (team['id'], team['name'], team['description'], team['color']))
    print(f"✓ Inserted {len(teams)} teams")

def insert_heroes(cursor, characters):
    """Insert character data"""
    for char in characters:
        cursor.execute("""
            INSERT IGNORE INTO heroes (name, team_id, role, description, image, category)
            VALUES (%s, %s, %s, %s, %s, 'marvel')
        """, (
            char['name'],
            char['team'],
            char['role'],
            char['description'],
            char['image']
        ))
    print(f"✓ Inserted {len(characters)} characters")

def get_teams_for_ui(cursor):
    """Get teams formatted for UI filter tabs"""
    cursor.execute("""
        SELECT id, name, color FROM teams ORDER BY 
        CASE id 
            WHEN 'avengers' THEN 1 
            WHEN 'xmen' THEN 2 
            WHEN 'guardians' THEN 3 
            WHEN 'cosmic' THEN 4 
            WHEN 'spiderverse' THEN 5 
            WHEN 'mystic' THEN 6 
            WHEN 'street' THEN 7 
        END
    """)
    teams = cursor.fetchall()
    
    # Generate filter tabs HTML
    filter_html = '<div class="team-filters">\n'
    filter_html += '  <button class="filter-tab active" data-team="all">All Teams</button>\n'
    
    for team in teams:
        filter_html += f'  <button class="filter-tab" data-team="{team[0]}" style="--team-color: {team[2]}">{team[1]}</button>\n'
    
    filter_html += '</div>'
    return filter_html

def main():
    """Main function to load all data"""
    print("🚀 Loading Marvel Teams Data...\n")
    
    try:
        # Connect to database
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Load JSON data
        print("📂 Loading JSON data...")
        data = load_json_data()
        
        # Create tables
        print("🔧 Creating tables...")
        create_tables(cursor)
        
        # Insert data
        print("📥 Inserting teams...")
        insert_teams(cursor, data['teams'])
        
        print("📥 Inserting characters...")
        insert_heroes(cursor, data['characters'])
        
        # Commit changes
        conn.commit()
        
        # Generate UI filter tabs
        print("\n🎨 Generating UI filter tabs...")
        filter_html = get_teams_for_ui(cursor)
        print(filter_html)
        
        print("\n✅ Data loaded successfully!")
        print(f"   - Teams: {len(data['teams'])}")
        print(f"   - Characters: {len(data['characters'])}")
        
    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")
    except FileNotFoundError:
        print("❌ Error: marvel_teams_data.json not found")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
