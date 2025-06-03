def caculitan_menu():
    choice = 0
    while choice != 7:
        print("\n=== CACULITAN' MENU ===")
        print("Hello! I am John Cris!\n")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment From Corpus")
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
                print("Name: John Cris C. Caculitan")
                print("Age: 20")
                print("Birthday: September 01, 2004")
                print("-----------------------------------------------------")
            case 2:
                print("\n ---- MY GOALS ----\n")
                print("• Goal 1: To pass INTE 202")
                print("• Goal 2: To graduate on year 2027")
                print("• Goal 3: To live a Christ-like life.")
                print("• Goal 4: To lift my family out of poverty")
                print("• Goal 5: To be a successful in life")
                print("-----------------------------------------------------")
            case 3:
                print("Comment From Caculitan")
                print("-----------------------------------------------------")
            case 4:
                print("Comment From Corpus")
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