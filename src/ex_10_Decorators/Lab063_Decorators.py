# Decorators: It is a function that extends the behavior of another function without
# modifying the base function.
# Pass the base function as an argument to the decorator.

def select_ride(func):
    def wrapper():
        print("**ride selected**")
        func()
    return wrapper

@select_ride
def uber_ride():
    print("you booked a auto")
uber_ride()