def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
#AbyB(2,1)

#if we are call the function and put the argument value like "AbyB(2,1)" so output of this code is 3 and without calling function code output is none and 0