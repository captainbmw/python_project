# prompt user for twoo numbers
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
# prompt user to enter operator
operator=input("Enter operator(+,-,/,*): ")
# perform calculation based on operator
if operator=="+":
    result = num1+num2
elif operator=="-":
    result = num1-num2
elif operator=="*":
    result = num1*num2
    if num2!=0:
        result = num1/num2
    else:
        result = "Error,divide by zero"
else:
    result = "invalid operator"
print(f"The answer is {result}")