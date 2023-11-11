print("Hello World")

# Simple Calculator Program

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+,-,*,/): ")
if(operator == '+'):
    output = num1+num2
elif(operator == '-'):
    output = num1-num2
elif(operator == '*'):
    output = num1*num2
elif(operator == '/'):
    output = num1/num2
else:
    print("Invalid operator")

print("Output:", output)
