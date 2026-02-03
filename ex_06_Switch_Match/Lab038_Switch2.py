print("Which test type you want to run")

test_type= input("Enter the test type: API, UI, Performance, Security")
match test_type:
    case "API":
        print("We are running a Postman testcase")
    case "UI":
        print("We are running a Selenium testcase ")
    case "Performance":
        print("We are running a Performance testcase")
    case "Security":
        print("We are running a Security testcase")
    case _:
        print("Invalid testcase")

