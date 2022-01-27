# sorting a list

names = ["chicken", "mutton", "fish", "rabbit"]

#sorting done depending on the names
#names.sort()
#print(names)

#sorting is done depending on the size of the variables

names.sort(key = lambda x : len(x))
print(names)

