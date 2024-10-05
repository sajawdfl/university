def getInput(string):
    result = input(string)
    if result == 'q':
        raise ValueError
    return result 