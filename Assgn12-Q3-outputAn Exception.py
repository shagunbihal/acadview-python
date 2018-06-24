try:
    raise NameError("Hi there")
except NameError:
    print("An Exception")


#output is "An Exception"