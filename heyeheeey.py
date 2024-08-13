def evennames(name):

    if len(name) %2==0:
        return print('even')
    else:
        return print('odd')

names = ['andy', 'yowi', 'jab']
list(map(evennames, names))






