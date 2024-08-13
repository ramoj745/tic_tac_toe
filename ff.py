def myfunc(*args):
    empty_list = []
    for even in args:
        if even %2==0:
            empty_list.append(even)
            return empty_list

print(myfunc(1,2,3,4))

