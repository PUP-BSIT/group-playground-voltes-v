def pineda_menu():
    choice = 0
    while choice != 7:
        print("\n=== PINEDA'S MENU ===")
        print("Hello! I am Dyanna May!\n")
        print("1. Basic Information")
        print("2. Hobbies")
        print("3. Comment From Caculitan")
        print("4. Comment From Corpus")
        print("5. Comment From Gulles")
        print("6. Comment From Morales")
        print("7. Go Back to  Voltes V Modules")
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        print("-----------------------------------------------------")

        match choice:
            case 1:
                print("\n ---- MY BASIC INFO ----\n")
                print("Name: Dyanna May D. Pineda")
                print("Age: 19")
                print("Birthday: October 10, 2005")
                print("Pet: My Catto ' Harith '")
                print("-----------------------------------------------------")
            case 2:
                print("\n ---- MY HOBBIES ----\n")
                print("• Hobby 1: Watch Horror Movies")
                print("• Hobby 2: Cook")
                print("• Hobby 3: Play Computer Games")
                print("-----------------------------------------------------")
            case 3:
                print("Comment From Caculitan")
                print("-----------------------------------------------------")
            case 4:
                print("Comment From Corpus")
                print("-----------------------------------------------------")
            case 5:
                print("Comment From Gulles")
                print("-----------------------------------------------------")
            case 6:
                print("Comment From Morales")
                print("-----------------------------------------------------")
            case 7:
                print("Exiting Pineda Menu")
                print("-----------------------------------------------------")
            case _:
                print("Invalid choice. Please select a number from 1 to 7.")