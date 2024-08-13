
def calculateupper(somevalue):

    count = 0
    for letter in somevalue:
        if letter.isupper():
            count += 1
    return f"No. of Upper case character : {count}"

def calculatelower(somevalue):

    count = 0
    for letter in somevalue:
        if letter.islower():
            count += 1
    return f"No. of Lower case character : {count}"


def allin():
    print("Sample String: hello Mr. Rogers, how are you this fine Tuesday?")
    print(calculateupper(mystring))
    print(calculatelower(mystring))

    return

mystring = 'Hello Mr. Rogers, how are you this fine Tuesday?'

allin()