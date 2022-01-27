#interchange the elements in the list

def swaplist(newlist):
    size = len(newlist)

    temp = newlist[0]
    newlist[0] = newlist [size - 1]
    newlist[size - 1] = temp

    return newlist
newlist = [12,55,32,41,57,9]
print(swaplist(newlist))