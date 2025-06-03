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
            import voltes.caculitan
            voltes.caculitan.caculitan_menu()
        case 2:
           import voltes.corpus
           voltes.corpus.corpus_menu()
        case 3:
            import voltes.gulles
            voltes.gulles.gulles_menu()
        case 4:
           import voltes.morales
           voltes.morales.morales_menu()
        case 5:
            import voltes.pineda
            voltes.pineda.pineda_menu()
        case 6:
            print("Exiting Voltes V Modules")
            print("-----------------------------------------------------")
        case _:
            print("Invalid choice. Please select a number from 1 to 6.")