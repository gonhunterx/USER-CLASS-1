def home_page(user):
    while True:
        print("==================")
        print(f"Welcome {user.username}")
        print(
            """
1. Add passwords to storage
2. View stored passwords
3. Delete passwords from storage
4. Logout
            """
        )
        home_choice = input("Input: ")
        if home_choice == "1":
            data = input("Type a password to store: ")
            user.insert_data(data)
            print("Password stored successfully.")
        elif home_choice == "2":
            stored_data = user.view_saved_data()
            print("Stored passwords:")
            if stored_data:
                print(stored_data)
            else:
                print("No data stored.")
        elif home_choice == "3":
            print("Which password would you like to delete?")
        elif home_choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid input. Please select 1, 2, 3, or 4.")
