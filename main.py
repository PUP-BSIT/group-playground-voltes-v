choice = 0
while choice !=6:
    print("-------------------------------------------")
    print("            Voltes V Modules               ")
    print("-------------------------------------------")
    print("1. Caculitan Module")
    print("2. Corpus Module")
    print("3. Gulles Module")
    print("4. Morales Module")
    print("5. Pineda Module")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    print("-------------------------------------------")
    
    match choice:
        case 1:
            print("Input Caculitan Module")
        case 2:
           print("Input Corpus Module")
        case 3:
            import voltes.gulles
            voltes.gulles.gullesmenu()
        case 4:
           print("Input Morales Module")
        case 5:
           print("Input Pineda Module")
        case 6:
            print("Exiting Voltes V Modules")
            print("-----------------------------------------------------")
        case _:
            print("Invalid choice. Please select a number from 1 to 6.")