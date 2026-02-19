def validate_status_code(response_code):
    if response_code == 200:
        print("Request is successful")
        return True
    else:
        print("Request is not successful")
        return False
print(validate_status_code(200))
validate_status_code(400)
validate_status_code(response_code=200)
print(validate_status_code(response_code=400))

