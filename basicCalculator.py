# building a better calculator

num1 = float(input('Type first number: '))
op = input('Enter desired function(+/-/*//): ')
num2 = float(input('Type second number: '))

if op == "+":
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
else:
    print(num1/num2)
