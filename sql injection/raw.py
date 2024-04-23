import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")

# Save (commit) the changes
conn.commit()

# Query using raw SQL
user_id = "1"  # Normally this would be unsafe if it came from user input!
query = f"SELECT * FROM users WHERE id = {user_id};"
cursor.execute(query)

# Display the results
print(cursor.fetchall())

# Close the connection
conn.close()
