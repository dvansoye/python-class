def chop(x) :
    if len(x) > 0 :
        del x[len(x) - 1]
        if len(x) > 0 :
            del x[0]

x = [1,2,3,4]
chop(x)
print x