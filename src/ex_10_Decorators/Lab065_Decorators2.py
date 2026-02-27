def add_sprinkles(func):
    def wrapper(*args, **kwargs):   # *args will add n number of arguments and **kwargs will add
                                    # keyword arguments
        print("**Add sprinkles**")
        func(*args, **kwargs)
    return wrapper

def add_chocolate(func):
    def wrapper(*args, **kwargs):
        print("**Add chocolate**")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_chocolate
def get_ice_cream(flavour):
    print(f"Here is your {flavour} Ice cream")

get_ice_cream("butterscotch")

