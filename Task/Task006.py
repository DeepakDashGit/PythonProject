#expected_reult = "Dashboard"
#actual_result = "Dashboard "    use strip()
#print(test passed -title matches)
#print(test failed - title mismatch)

expected_result = "Dashboard"
actual_result = "Dashboard "
#actual_result = "dashboard"
#actual_result = "DASHBOARD"
if expected_result.strip().lower().upper() == actual_result.strip().lower().upper():
    print("Test passed - title matches")
else:
    print("Test failed - title mismatch")


