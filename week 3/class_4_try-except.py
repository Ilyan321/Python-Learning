try:
    print(x)
except NameError:
    print("variable not defined")
except:
    print("something else went wrong")
