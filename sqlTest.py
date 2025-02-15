import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

# Execute SQL commands
cursor.execute('''
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,  -- Store hashed passwords
    nightscout_url BYTEA NOT NULL,         -- Encrypted
    api_secret BYTEA NOT NULL,             -- Encrypted
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()