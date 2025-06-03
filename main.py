choice =0

while choice != 6:
    print("\nVoltes Module")
    print("1. Caculitan Module")
    print("2. Corpus Module")
    print("3. Gulles Module")
    print("4. Morales Module")
    print("5. Pineda Module")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    print("-----------------------------------------------------------------")
    match choice:
        case 1:
            print("Caculitan Module is not yet implemented.")
        case 2:
            print("Corpus Module is not yet implemented.")
        case 3:
            import voltes.gulles
            voltes.gulles.gulles_menu()
        case 4:
            print("Morales Module is not yet implemented.")
        case 5:
            print("Pineda Module is not yet implemented.")
        case 6:
            print("Exiting Voltes Module")
            exit()
        case _:
            print("Invalid choice, please try again.")