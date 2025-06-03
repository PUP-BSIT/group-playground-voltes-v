def corpus_menu():
    choice = 0
    while choice != 7:
        print("\n=== CORPUS' MENU ===")
        print("Hello! I am Precious Hannah!\n")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment From Caculitan")
        print("4. Comment From Gulles")
        print("5. Comment From Morales")
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
                print("Name: Precious Hannah A. Corpus")
                print("Age: 19")
                print("Birthday: October 25, 2005")
                print("-----------------------------------------------------")
            case 2:
                print("\n ---- MY GOALS ----\n")
                print("• Goal 1: To pass INTE 202")
                print("• Goal 2: To graduate with latin honors")
                print("• Goal 3: To be a successful Cybercrime Investigator")
                print("• Goal 4: To travel the world with my family")
                print("• Goal 5: To migrate to USA")
                print("• Goal 6: To be happy")
                print("-----------------------------------------------------")
            case 3:
                print("Comment From Caculitan")
                print("-----------------------------------------------------")
            case 4:
                print("Comment From Gulles")
                print("-----------------------------------------------------")
            case 5:
                print("Comment From Morales")
                print("-----------------------------------------------------")
            case 6:
                print("Comment From Pineda")
                print("-----------------------------------------------------")
            case 7:
                print("Exiting Corpus' Menu")
                print("-----------------------------------------------------")
                break
            case _:
                print("Invalid choice. Please select a number from 1 to 7.")