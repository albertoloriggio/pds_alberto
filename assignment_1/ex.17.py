def calculate(number_1,number_2,operator):
    if operator=='+':
        return number_1+number_2
    elif operator=='-':
        return number_1-number_2
    elif operator=='*':
        return number_1*number_2
    elif operator=='/':
        if num2 !=0:
            return number_1/number_2
        else:
            return 'Division by 0!'
    else:
        return 'Invalid operator'
number_1=int(input('Enter a number:'))
number_2=int(input('Enter an other number:'))
operator=input('Enter an operator(+,-,*,/):')
result=calculate(number_1,number_2,operator)
print(result)
