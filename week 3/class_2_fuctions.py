def outer():
    print("A")
    def inner():
        print("B")
    inner()
outer()