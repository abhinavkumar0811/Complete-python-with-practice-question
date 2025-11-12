# Q8. Character Type Checker
# Input a character and check whether it is:
# An alphabet,    
# A digit, or
# A special character.
# Use if-else-if.


import random;
charactor = input('Enter your charactor: ')

digits = random.randint(0, 12);
print(digits)

if charactor == charactor.lower():
    print('this is smallest alphabet')
elif charactor == charactor.upper():
    print('This charactor is capital charactor')
elif charactor == charactor.isdigit():
    print('This charactor is digit')
else:
    print('It is a alphabet charactor')