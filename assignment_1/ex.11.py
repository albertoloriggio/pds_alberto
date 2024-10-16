grades=input('Enter a grade(A,B,C,D,F):')
match grades.upper():
    case 'A':
        print('Excellent!')
    case 'B':
        print('Good job!')
    case 'C':
        print('Fair.')
    case 'D':
        print('Needs improvement.')
    case 'F':
        print('Failing.')
    case _:
        print('Invalid grade')

