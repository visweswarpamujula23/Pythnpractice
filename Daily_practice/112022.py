df = spark.read.parquet("user.parquet")

outliers = df.filter(df[age]>100)

print(outliers.count)







'''
user_input1 = int(input("Enter the first number: "))
user_input2 = int(input("Enter the second number: "))

for number in range(min(user_input1,user_input2),0,-1):
    if user_input1 % number == 0 and user_input2% number ==0:
        print(f"{number} is HCF of {user_input1} and {user_input2}")
        break
else:
    print(f"We should pass only non zero positive numbers. but we got {user_input1} and {user_input2}")
    '''