# Q4. Voting Eligibility
# Take a person’s age as input and check if they are eligible to vote (age ≥ 18).
age = int(input("Enter you age for voating elegiblity: "))

if age >=18:
    print('You are elegible for voating !')
else:
    print(f'Sorry you are not elegible for voating !  \n you are elegible for  voating after: {18-age} years')




# Q5. Grade Calculation

# Input marks (0–100) and print the grade using the following rules:
# >=90: Grade A
# >=75: Grade B
# >=50: Grade C
# <50: Fail
# Use if-else-if ladder.

marks = int(input('Enter your marks for grade: '))

if marks>= 90 and marks < 100:
    print('Grade A')
elif marks >= 75 and marks < 90:
    print('Grade B')
elif marks >= 50 and marks < 50:
    print('grade C')
elif marks < 50 and marks >= 0:
    print('Fail')
else:
    print('please provide number in range')



# Q6. Simple Calculator
# Build a simple calculator using switch.
# Input: two numbers and an operator (+, -, *, /)
# Output: the result of the operation.

print('Calculator')
first_num = int(input('Enter first number: '))
operation = input('enter operation: ')
second_num = int(input('Enter send number: '))

match operation:

    case '+':
       result = first_num + second_num
       print(f'Addition of {first_num} and {second_num} is {result}')
    #    break - fall through follow python so where condition match it will terminated
    case '-':
        result = first_num - second_num
        print(f'Substraction of {first_num} and {second_num} is {result}')
    case '*':
        result = first_num * second_num
        print(f'Multiplication of {first_num} and {second_num} is {result}')
    case '/':
        result = first_num / second_num 
        print(f'Division of {first_num} and {second_num} is {result}')
    case _: 
        print('Invalid operation !')
        






#  Q7. Leap Year Check
# Write a program to check if a given year is a leap year or not.
# Conditions:
# Divisible by 4 → leap year
# But if divisible by 100 → not a leap year
# Unless divisible by 400 → leap year again
# Use nested if.


year = int(input("Enter year: "))

if year%4==0 and year%100 !=0 or year%400 ==0:
    print(f'This year: {year} is a leap year')
else:
    print('This year is not a leap year')




    # Q8. Character Type Checker

    # Input a character and check whether it is:

    # An alphabet,

    # A digit, or

    # A special character.

    # Use if-else-if.

    # Q9. Day of the Week

    # Write a program that takes a number (1–7) and prints the day name using switch.
    # (1 = Monday, 2 = Tuesday, etc.)

    # Q10. Largest of Three Numbers

    # Take three integers from the user and print the largest one using nested if or logical operators (&&).

    # Example Input: