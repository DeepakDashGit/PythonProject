import time

def print_log(func):
    def wrapper(*args, **kwargs):
        print("Start of the log")
        func(*args, **kwargs)
    return wrapper

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Start of the time")
        func(*args, **kwargs)
        end_time = time.time()
        print("Total time taken by this function : ", end_time - start_time)
    return wrapper
@time_decorator
@print_log
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)
test_ui_1()

@time_decorator
@print_log
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)
test_ui_2()