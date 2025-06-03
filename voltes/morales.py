def morales_menu():
    choice = 0
    while choice != 7:
        print("\n=== MORALES'S MENU ===")
        print("Hello! I am Woman Daphne Morales!\n")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment From Caculitan")
        print("4. Comment From Corpus")
        print("5. Comment From Gulles")
        print("6. Comment From Pineda")
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
                print("Name: Woman Daphne Morales")
                print("Age: 22")
                print("Birthday: March 9, 2003")
                print("-----------------------------------------------------")
            case 2:
                print("\n ---- MY GOALS ----\n")
                print("• Goal 1: To pass INTE 202")
                print("• Goal 2: Finish my studies")
                print("• Goal 3: Travel the world")
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
                print("Comment From Pineda")
                print("-----------------------------------------------------")
            case 7:
                print("Exiting Morales Menu")
                print("-----------------------------------------------------")
            case _:
                print("Invalid choice. Please select a number from 1 to 7.")