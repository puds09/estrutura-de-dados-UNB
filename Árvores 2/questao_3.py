import re

lastKey = ""
added = []

def getElementsByClassName(root, id):

    id = id.split()
    temp = []
    global lastKey
    global added

    for key in root:
        for element in id:
            if root[key] == element.lower() or root[key] == element.upper() :
                temp.append(lastKey)
 

            if type(root[key]) is not str: 
                lastKey = key
                temp += getElementsByClassName(root[key], element)

    return temp
