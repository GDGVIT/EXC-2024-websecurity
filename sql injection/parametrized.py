import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table if it does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

# Insert data using safer parameterized SQL
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Carol', 'carol@example.com'))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Dave', 'dave@example.com'))

# Save (commit) the changes
conn.commit()

# Query using parameterized SQL
user_id = "2"  # This is still a hardcoded value but safe for demonstration
query = "SELECT * FROM users WHERE id = ?;"
cursor.execute(query, (user_id,))

# Display the results
print(cursor.fetchall())

# Close the connection
conn.close()
