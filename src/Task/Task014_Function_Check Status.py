# Write a Function to Check Test Case Status
# Write a function check_status(status_code) that returns:
#
# "PASS" if status_code = 200
# "FAIL" if status_code = 400 or 500
# "UNKNOWN" otherwise


def check_status(status_code):
    if status_code == 200:
        return "Pass"
    elif status_code in(400, 500):
        return "Fail"
    else:
        return "Unknow"

print(check_status(200))   # PASS
print(check_status(500))   # FAIL
print(check_status(302))   # UNKNOWN