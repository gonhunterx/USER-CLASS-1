from app.sql_db import conn, c
from app.home_page import home_page
from app.users import User


def main_menu():
    print(
        """
1. Login
2. Register
3. Exit
          """
    )
    choice = input("Input: ")
    return choice


def login():
    print("Please enter your username and password.")
    username = input("Username: ")
    password = input("Password: ")

    # Check if the user exists
    c.execute(
        "SELECT user, password FROM users WHERE user = ? AND password = ?",
        (username, password),
    )
    result = c.fetchone()

    if result:
        print("Login successful!")
        # Create a User instance for the logged-in user
        user = User(username, password)
        home_page(user)  # Pass the User instance to the home_page
    else:
        print("Login failed. Please try again or register.")


def register():
    print("=========================")
    print("Please Create an account")
    username = input("Username: ")
    password = input("Password: ")

    # Check if the username already exists in the database
    c.execute("SELECT user FROM users WHERE user = ?", (username,))
    existing_user = c.fetchone()

    if existing_user:
        print("Username already exists. Please choose another.")
    else:
        # Insert the data into the database for account creation in the users table
        c.execute(
            "INSERT INTO users (user, password) VALUES (?, ?)", (username, password)
        )
        conn.commit()
        print("Registration successful!")


def main():
    print("Welcome to the LamaForge Password Manager")
    while True:
        main_menu_choice = main_menu()
        if main_menu_choice == "1":
            login()
        elif main_menu_choice == "2":
            register()
        elif main_menu_choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid input. Please select a valid option.")


if __name__ == "__main__":
    main()
