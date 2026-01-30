# All errors
# ZeroDivisionError
# NameError
# IndexError
# KeyError
# TypeError
# ValueError
# FileNotFoundError
# ImportError
# AttributeError
# IndentationError
# SyntaxError


# try:
#     print(x)
# except NameError:
#     print("variable not defined")
# except :
#     print("indentation error occurred")
# finally:
#     print("the 'try except' is finished")

def name(name):
    if type(name) != str:
        raise TypeError ("Only strings are allowed")
    
try: 
    name(123)
except TypeError as e:
    print(e)
