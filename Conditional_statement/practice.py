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


charactor = input('Enter charactor: ')

if charactor.isalpha():
    print(f'This is alphabet charactors: {charactor} ')
elif charactor.isdigit():
    print(f'This charactor hold digit {charactor}')
else:
    print(f'This is special charactor {charactor}')

    # Q9. Day of the Week

    # Write a program that takes a number (1–7) and prints the day name using switch.
    # (1 = Monday, 2 = Tuesday, etc.)

    # Q10. Largest of Three Numbers

    # Take three integers from the user and print the largest one using nested if or logical operators (&&).

    # Example Input:


#     Basic Level (1–30):

# Check if a number is positive or negative.

# Check if a number is even or odd.

# Check if a number is divisible by 5.

# Check if a number is divisible by 3 and 5.

# Check if a number is divisible by 3 or 5.

# Check if a number is greater than 10.

# Check if a number is less than 100.

# Check if a number is between 1 and 10.

# Check if a character is a vowel.

# Check if a character is a consonant.

# Check if a string is empty.

# Check if a string length is greater than 5.

# Check if a string starts with "P".

# Check if a string ends with "n".

# Check if a number is positive, negative, or zero.

# Check if a number is a single-digit, two-digit, or three-digit number.

# Check if a number is divisible by 2, 3, or both.

# Check if a year is a leap year.

# Check if a number is a prime number.

# Check if a number is a perfect square.

# Compare two numbers and print the larger one.

# Compare three numbers and print the largest.

# Check if a number is a multiple of 7.

# Check if a number is a multiple of 4 but not 6.

# Check if a character is uppercase.

# Check if a character is lowercase.

# Check if a character is a digit.

# Check if a character is alphanumeric.

# Check if a list is empty.

# Check if an element exists in a list.

# Intermediate Level (31–70):
# 31. Check if all elements in a list are even.
# 32. Check if any element in a list is odd.
# 33. Check if a list contains duplicates.
# 34. Check if two lists have common elements.
# 35. Compare lengths of two lists.
# 36. Check if a dictionary contains a specific key.
# 37. Check if a dictionary contains a specific value.
# 38. Compare values of two dictionary keys.
# 39. Check if a string contains a specific substring.
# 40. Check if string contains only letters.
# 41. Check if string contains only digits.
# 42. Check if string is alphanumeric.
# 43. Check if string is palindrome.
# 44. Check if number is Armstrong number.
# 45. Check if number is divisible by both 2 and 3.
# 46. Check if number is divisible by 2 or 3.
# 47. Check if a number is odd and greater than 10.
# 48. Check if a number is even or divisible by 3.
# 49. Nested if: check if number is positive and even.
# 50. Nested if: check if number is negative and odd.
# 51. Check if a year is century leap year.
# 52. Check if a number is in range 50–100 or 200–300.
# 53. Check if number is single-digit or double-digit or triple-digit.
# 54. Check if number is prime or composite.
# 55. Check if string starts with vowel and ends with consonant.
# 56. Check if character is lowercase letter and not vowel.
# 57. Check if element is in list and greater than 10.
# 58. Check if number divisible by 4 but not by 8.
# 59. Check if sum of two numbers is greater than 100.
# 60. Check if difference of two numbers is less than 10.
# 61. Check if string length is even.
# 62. Check if string length is odd.
# 63. Check if number is divisible by 5 and not divisible by 10.
# 64. Check if list contains only positive numbers.
# 65. Check if list contains at least one negative number.
# 66. Compare two strings alphabetically.
# 67. Compare two numbers and check if difference is even.
# 68. Check if a tuple contains a specific value.
# 69. Check if number is perfect number.
# 70. Check if sum of digits of number is even or odd.

# Advanced Level (71–100):
# 71. Check if number is prime and palindrome.
# 72. Check if string is palindrome and length > 5.
# 73. Check if all elements in list are divisible by 3.
# 74. Check if at least one element in list is divisible by 5.
# 75. Check if set is subset of another set.
# 76. Check if set is superset of another set.
# 77. Check if two sets are disjoint.
# 78. Nested if: check if number is divisible by 2, 3, and 5.
# 79. Nested if: check if number is divisible by 4 but not by 8.
# 80. Check if dictionary has key "a" and value > 5.
# 81. Check if dictionary has key "b" or key "c".
# 82. Check if key exists and value is even.
# 83. Check if two numbers are equal, or one is greater than other.
# 84. Check if number is divisible by 2 or divisible by 3 but not both.
# 85. Check if string starts with capital letter and ends with punctuation.
# 86. Check if number is in range 1–50 or 100–150.
# 87. Check if number is multiple of 3 and 5 but not 7.
# 88. Check if number is odd, positive, and greater than 10.
# 89. Check if number is prime and greater than 50.
# 90. Check if all elements of list are positive and even.
# 91. Check if list contains at least one negative number.
# 92. Check if sum of list elements is even.
# 93. Check if sum of list elements is divisible by 3.
# 94. Check if string contains both vowels and consonants.
# 95. Check if string is lowercase and contains digit.
# 96. Check if tuple contains only numbers.
# 97. Check if tuple contains at least one string.
# 98. Nested if: check if number is positive, even, and divisible by 5.
# 99. Nested if: check if number is negative, odd, and divisible by 3.
# 100. Check if dictionary has all values greater than 0.