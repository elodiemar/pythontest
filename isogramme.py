def is_isogram(string):
    #your code here
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
