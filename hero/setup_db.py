import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sura123",
    database="otp_login"
)
cursor = db.cursor()

# Create users table with all required columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    favorite_hero VARCHAR(100),
    favorites TEXT,
    otp VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
db.commit()

# Check if columns exist and add them if needed
cursor.execute("SHOW COLUMNS FROM users LIKE 'favorites'")
if cursor.fetchone() is None:
    cursor.execute("ALTER TABLE users ADD COLUMN favorites TEXT")
    db.commit()

cursor.execute("SHOW COLUMNS FROM users LIKE 'favorite_hero'")
if cursor.fetchone() is None:
    cursor.execute("ALTER TABLE users ADD COLUMN favorite_hero VARCHAR(100)")
    db.commit()

cursor.execute("SHOW COLUMNS FROM users LIKE 'name'")
if cursor.fetchone() is None:
    cursor.execute("ALTER TABLE users ADD COLUMN name VARCHAR(255)")
    db.commit()

print("Database setup complete!")
cursor.close()
db.close()
