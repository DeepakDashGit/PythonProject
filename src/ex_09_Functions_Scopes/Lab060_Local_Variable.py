pb_global = 25

def my_func():
    pb_local = 10
    print(pb_global)
    print(pb_local)   #here we can call the local variable inside

#my_func(pb_local)     can't call the local variable outside

my_func()
