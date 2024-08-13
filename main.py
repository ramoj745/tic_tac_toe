
def old_macdonaland(name):

    listed = list(name)
    listed[0] = listed[0].upper()
    listed[3] = listed[3].upper()

    return ''.join(listed)

print(old_macdonaland('macdonalds'))