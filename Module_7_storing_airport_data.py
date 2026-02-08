airports = {}
while True:
    print("\nChoose an option:")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")
    choice = input("Your choice: ")
    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved.")
    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
