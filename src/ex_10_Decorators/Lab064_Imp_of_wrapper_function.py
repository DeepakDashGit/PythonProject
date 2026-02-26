# def select_room(func):
#     print("**Select room**")
#     func()
#
# @select_room
# def book_hotel():
#     print("you booked a room")

#   In the above code, we didn't call the base function, but it will still return the result as
# **Select room**
#you booked a room

# Correct code using wrapper function
def select_room(func):
    def wrapper():
     print("**Select room**")
     func()
    return wrapper

@select_room
def book_hotel():
    print("you booked a room")
book_hotel()  #if we exclude the calling of this function here it will not give any results.

