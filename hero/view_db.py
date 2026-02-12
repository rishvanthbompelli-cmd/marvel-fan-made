import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sura123",
    database="otp_login"
)
cursor = db.cursor()

print("=" * 70)
print(" MARVEL DATABASE - ALL USERS WITH FAVORITES")
print("=" * 70)

cursor.execute("SELECT id, phone, name, favorite_hero, favorites FROM users ORDER BY id DESC")
users = cursor.fetchall()

for user in users:
    print(f"\n[{user[0]}] Phone: {user[1]}")
    print(f"    Name: {user[2] or 'N/A'}")
    print(f"    Login Favorite: {user[3] or 'N/A'}")
    
    if user[4]:
        import json
        try:
            favs = json.loads(user[4])
            if favs:
                print(f"    SAVED FAVORITES: {', '.join(favs)}")
            else:
                print(f"    Saved Favorites: []")
        except:
            print(f"    Saved Favorites: {user[4]}")
    else:
        print(f"    Saved Favorites: (empty)")

print("\n" + "=" * 70)
cursor.close()
db.close()
