Browser_Name = input("Enter Browser Name: ")
match Browser_Name:
    case "Firefox":
        print("supported")
    case "Edge":
        print("Supported")
    case "Chrome":
        print("Supported")
    case _:
        print("Not Supported")