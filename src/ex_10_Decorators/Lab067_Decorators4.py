def before_and_after(func):
    def wrap():
        print("Before function")
        func()
        print("After function")
    return wrap

@before_and_after
def test_ui():
    print("Test ui")
test_ui()