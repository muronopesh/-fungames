## FUN GAMES
print("FASCINATING PLACES YOU SHOULD VISIT IN AFRICA: ")
print("DEPENDING ON WHAT YOU LIKE — WILD ANIMAL or DESERT:")

choice1 = input("Type WILD ANIMAL or DESERT: ").lower()

if choice1 == "wild animal":
    print("\nWelcome to Kenya!")
    print("Would you like to visit MAASAI MARA or NAIROBI?")
    choice2 = input("Type MAASAI MARA or NAIROBI: ").lower()

    if choice2 == "maasai mara":
        print("\nMaasai Mara park is located in Kajiado. Do you want to see LION or RHINO?")
        choice3 = input("Type LION or RHINO: ").lower()
        if choice3 == "lion":
            print("\n3,000 dollars for the trip. No discount available.")
        elif choice3 == "rhino":
            print("6,000 dollars for the trip. You won a 0.6 discount!")
        else:
            print("\nINVALID ANIMAL CHOICE! Try again next time.")

    elif choice2 == "nairobi":
        print("Nairobi park is in the city. Do you want to see LION or RHINO?")
        choice3 = input("Type LION or RHINO: ").lower()
        if choice3 == "lion":
            print("\n3,000 dollars for the trip. No discount available.")
        elif choice3 == "rhino":
            print("6,000 dollars for the trip. You won a 0.6 discount!")
        else:
            print("INVALID ANIMAL CHOICE! Try again next time.")

elif choice1 == "desert":
    print("\nDeserts are beautiful!")
    print("Would you like to visit NAMIBIA or MOROCCO?")
    choice2 = input("Type NAMIBIA or MOROCCO: ").lower()

    if choice2 == "namibia":
        print("Namib desert in Namibia is where the desert meets the Atlantic ocean! Do you like NORTH or SOUTH?")
        choice3 = input("Type NORTH or SOUTH: ").lower()
        if choice3 == "north":
            print("Welcome to NORTH AFRICA!")
        elif choice3 == "south":
            print("Welcome to SOUTH AFRICA!")
        else:
            print("INVALID DIRECTION! Try again next time.")

    elif choice2 == "morocco":
        print("Moroccan deserts are very huge with lots of sand dunes and hot temperatures! Do you like NORTH or SOUTH?")
        choice3 = input("Type NORTH or SOUTH: ").lower()
        if choice3 == "north":
            print("Welcome to NORTH AFRICA!")
        elif choice3 == "south":
            print("Welcome to SOUTH AFRICA!")
        else:
            print("TRY AGAIN NEXT TIME!")
    else:
        print("INVALID COUNTRY CHOICE! Try again next time.")

else:
    print("\nINVALID CHOICE! Please type WILD ANIMAL or DESERT.")