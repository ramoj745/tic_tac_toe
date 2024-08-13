
def is_even(num):
    noteven = num % 2 != 0
    return noteven

list1 = [1,2,3,4,5,6,9]

print(list(map(lambda x: x **2, filter(is_even, list1))))