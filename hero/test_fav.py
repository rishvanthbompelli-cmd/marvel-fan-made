import mysql.connector
import json

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sura123",
    database="otp_login"
)
cursor = db.cursor()

# Test adding a favorite manually
print("Testing favorite add...")
cursor.execute("SELECT phone, favorites FROM users ORDER BY id DESC LIMIT 5")
users = cursor.fetchall()

for user in users:
    print(f"Phone: {user[0]}, Favorites: {user[1]}")

# Update one user with test favorites
test_favorites = json.dumps(["Iron Man", "Thor", "Hulk"])
cursor.execute("UPDATE users SET favorites=%s WHERE id=1", (test_favorites,))
db.commit()
print(f"\nUpdated user 1 with favorites: {test_favorites}")

# Show updated data
cursor.execute("SELECT id, phone, favorites FROM users WHERE id=1")
print("\nUser 1 after update:")
print(cursor.fetchone())

cursor.close()
db.close()
