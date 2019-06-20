
import re
mystring= input ("input a string :" )
# check for letters and avalibility " = "
if '=' in mystring and ((re.search("[a-zA-Z]+" ,mystring)) == None): part1, part3 =mystring.split('=')
else :print ('error')

if '+' in mystring : operator = '+'
elif '-' in mystring : operator = '-'
elif '*' in mystring : operator = '*'
elif '/' in mystring : operator = '/'
else :print ('error')

part1, part2 =part1.split(operator)

if part1.isdigit() and part2.isdigit() and part3.isdigit() :
    a = int (part1)
    b = int (part2)
    c = int (part3)
    if (operator == '+') and (a + b == c):
        print ('YES')
    elif operator == '-' and (a - b == c):
        print ('YES')
    elif operator == '*' and (a * b == c):
        print ('YES')
    elif operator == '/' and (a / b == c):
        print ('YES')
    else:
        print ('NO')
else :print ('error')
















