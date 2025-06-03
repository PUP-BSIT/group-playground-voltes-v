def gulles_menu():
    choice = 0
    while choice != 7:
        print("Hello, I'm Althea Shane Salazar Gulles")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment From Caculitan")
        print("4. Comment From Corpus")
        print("5. Comment From Morales")
        print("6. Comment From Pineda")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        print("-----------------------------------------------------")
           
        match choice:
            case 1:
                print("Sex: Female")
                print("Age: 20 years old")
                print("Birthday: October 20, 2004")
                print("-----------------------------------------------------")
            case 2:
                print("Goals:")
                print("To pass IPT SUBJECT")
                print("To graduate in the year 2027")
                print("To have a stable job after graduation")
                print("-----------------------------------------------------")
            case 3:
                print("Comment From Caculitan")
                print("-----------------------------------------------------")
            case 4:
                print("Comment From Corpus")
                print("-----------------------------------------------------")
            case 5:
                print("Comment From Morales")
                print("MAKAKAPASA KA SA IPT SUBJECT<333")
                print("-----------------------------------------------------")
            case 6:
                print("Comment From Pineda")
                print("-----------------------------------------------------")
            case 7:
                print("Exiting Gulles Menu")
                print("-----------------------------------------------------")
            case _:
                print("Invalid choice. Please select a number from 1 to 7.")