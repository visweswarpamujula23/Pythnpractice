#prime number

# user_input = int(input("Enter the number:"))
# if user_input>1:
#     for x in range(2,user_input):
#         if(user_input%x) == 0:
#             print("not a prime number")
#             break
#         else:
#             print("given number is prime number")
#             break
# else:
#     print("not prime number")


#fibonacci number:


#even or odd

# user_input = int(input("enter number:"))
# if user_input%2==0:
#     print("given number is even number")
# else:
#     print("the given numbr is odd")


#prime number

user_input = int(input("enter the number"))
if user_input>1:
    for k in range(0,user_input):
        if(user_input%k == 0):
            print("given number is not prime number")
            break
        else:
            print("given number is prime number")
            break
else:
    print("the given number is not prime number")