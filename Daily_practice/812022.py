#amstrong number range

user_input1 = int(input("Enter the first number:"))
usr_input2 = int(input("Enter the second number:"))

for i in range(user_input1,usr_input2+):
    print(i)
    num =i
    result =0
    n=len(str(num))
    while(i!=0):
        digit = i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)

#bitwise operators

