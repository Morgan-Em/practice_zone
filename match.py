name = input("What's your name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")

    case "Draco" | "Pansy" | "Crabbe" | "Goyle":
        print("Slytherin")
    
    case _: 
        print("Who are you?")