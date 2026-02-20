def outer_func():
    vr1 = 4

    def inner_func():
        vr2 = 5
        print(vr1)

    def inner_func2():
        print(vr1)
    inner_func()
    inner_func2()

outer_func()