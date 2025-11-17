import sqlite3
import os

# Railway uses /data/neurobud.db
db_path = '/data/neurobud.db' if os.path.exists('/data/neurobud.db') else 'neurobud.db'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    if not cursor.fetchone():
        print("Users table doesn't exist yet!")
        conn.close()
        exit()

    # Get all users
    cursor.execute('SELECT id, email, name, is_admin FROM users')
    users = cursor.fetchall()

    print(f'Database: {db_path}')
    print('=' * 80)

    if users:
        print(f'Found {len(users)} user(s):')
        print('-' * 80)
        for user in users:
            admin_status = 'ADMIN' if user[3] else 'Not Admin'
            print(f'ID: {user[0]} | {user[1]} | {user[2]} | {admin_status}')
    else:
        print('No users found!')
        print('You need to sign in to the frontend first to create your user account.')

    conn.close()

except Exception as e:
    print(f'Error: {e}')
