def login():
    # Predefined username and password
    correct_username = "user123"
    correct_password = "securepass"

    # Getting input from user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Checking credentials
    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password")

# Call the login function
login()
