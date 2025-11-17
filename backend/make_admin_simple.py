#!/usr/bin/env python3
"""
Simple script to make a user admin in the database.
Uses only stdlib - no external dependencies.
"""
import sqlite3
import os
import sys

# Email to make admin
ADMIN_EMAIL = "nishanth4011@gmail.com"

# Get database path from environment or use default
database_url = os.getenv('DATABASE_URL', 'sqlite:///./neurobud.db')

# Extract SQLite file path from DATABASE_URL
# Format: sqlite:///path/to/file.db or sqlite:////absolute/path/to/file.db
if database_url.startswith('sqlite:///'):
    db_path = database_url.replace('sqlite:///', '')
    # Handle absolute paths (sqlite:////data/neurobud.db -> /data/neurobud.db)
    if db_path.startswith('/'):
        db_path = '/' + db_path.lstrip('/')
elif database_url.startswith('postgresql://'):
    print("Error: This script only works with SQLite databases")
    print(f"Current DATABASE_URL: {database_url}")
    sys.exit(1)
else:
    db_path = './neurobud.db'

print(f"Database path: {db_path}")
print(f"Looking for user: {ADMIN_EMAIL}")
print("-" * 60)

try:
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    if not cursor.fetchone():
        print("ERROR: Users table doesn't exist!")
        print("The database hasn't been initialized yet.")
        conn.close()
        sys.exit(1)

    # Find user
    cursor.execute('SELECT id, email, is_admin FROM users WHERE email = ?', (ADMIN_EMAIL,))
    user = cursor.fetchone()

    if not user:
        print(f"ERROR: User {ADMIN_EMAIL} not found!")
        print("\nAvailable users:")
        cursor.execute('SELECT id, email, name FROM users')
        all_users = cursor.fetchall()
        if all_users:
            for u in all_users:
                print(f"  - ID {u[0]}: {u[1]} ({u[2]})")
        else:
            print("  (no users in database)")
        print("\nPlease sign in to the frontend first to create your user account.")
        conn.close()
        sys.exit(1)

    user_id, email, is_admin = user

    if is_admin:
        print(f"User {email} is ALREADY an admin!")
    else:
        # Make user admin
        cursor.execute('UPDATE users SET is_admin = 1 WHERE id = ?', (user_id,))
        conn.commit()
        print(f"SUCCESS: {email} is now an admin!")

    conn.close()

except sqlite3.Error as e:
    print(f"Database error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
