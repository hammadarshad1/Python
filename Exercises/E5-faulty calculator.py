num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))

operator = input('Enter the operation do you want: ')

if num1==45 and num2==3 and operator=='*':
    print('555')

elif num1==56 and num2==9 and operator=='+':
    print('77')

elif num1==56 and num2==6 and operator=='/':
    print('4')

elif operator == '+':
    print(num1+num2)

elif operator == '-':
    print(num1-num2)

elif operator == '*':
    print(num1*num2)

elif operator == '/':
    print(num1/num2)

else:
    print('Wrong numbers or Operator!')