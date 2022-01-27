student = ["ravi teja", "bharath", "avinash", "mahesh", "visweswar","sumanth"]

for index in student:
    print(index)

for index in range (0, len(student)):
    print(index,student[index])

    if student[index]=="mahesh":
        #mahesh_place = index
        print(f"...{mahesh_place} is{student[index]}")
        print(f"...{mahesh_place-1} is{student[index-1]}")
        print(f"...{mahesh_place+1} is{student[index+1]}")

# print(student)
#
# #6 people went to jait will mahesh