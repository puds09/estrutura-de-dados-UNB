def inverte(word):
    if word != "": 
        print(word[-1], end="")
        inverte(word[:-1])
    return ""

