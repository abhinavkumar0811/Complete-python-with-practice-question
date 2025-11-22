# Basic Level (1–30):

# Create a string variable s = "Python".

s = 'python'

# Print the string s
print(s)

# Print the length of string s.
print(f'length of string s is {len(s)}')

# Print the first character of s.
print(s[0])

# Print the last character of s.
print(s[-1])

# Print the string s in uppercase.
s_uppercase = s.upper()
print(s_uppercase)

# Print the string s in lowercase.
s_lowecase = s.lower()
print(s_lowecase)

# Capitalize the first letter of s.
s_first_cap = s.capitalize()
print(s_first_cap)

s = 'python'
# Check if the string s starts with "Py".
print(s.startswith('py'))

# Check if the string s ends with "on".
print(s.endswith('on'))
# Print the string s repeated 3 times.
print(s*3)  #repitation

# Concatenate " is fun" to s.
s_concat = s+' is fun'
print(s_concat)


# Print the substring "yth" from s.
print(s[slice(1,4)])
print(s[1:4])

# Slice the first 4 characters of s.
print(s[slice(0,4)])

# Slice the last 3 characters of s.
print(s[-3:])


# Slice the string from index 2 to 5.
print(s[2:5])

# Print every second character of s.
print(s[::2])
print(s[slice(0,None, 2)])

# Reverse the string s.
print(s[::-1])

# Replace "Python" with "Java" in a string.
print(s)
s = s.replace('python', 'java')
print(s)          # one varaible refreance multiple object refrence counting oncept



# Find the index of "t" in s.
# print(s.index('t'))    # it will not in string so it will return value error
print(s.find('t'))         # it will return -1 not value error


# Count occurrences of "o" in s.
s = s.replace('java', 'python is fun')
print(s.count('o'))     # it not found it will return 0 if found it will return occurence count

# Check if all characters are alphabetic.
print(s.isalpha())

# Check if all characters are numeric.
print(s.isdigit())

# Strip whitespace from " Python ".
print(s.strip())

# Split "Python is fun" by space.
s_el = s.split()
print(s_el)
print(type(s_el))   # it will always return list split()

# Join list ["Python", "is", "fun"] into a string.
new_s = ' '.join(s_el)
print(new_s)
print(type(new_s))

# Check if string contains "thon" using in.
if 'thon' in new_s:
    print('True')
else: 
    print('False')

# Check if string contains "abc" using not in.
if 'abc' in new_s:
    print('true')
else:
    print('false')

# Convert string "123" to integer.
new_s = int(123)
print(new_s)
print(type(new_s))    # explicit conversion

# Convert integer 456 to string.
print(str(new_s)) # explict conversion - manual done by us
print(type(new_s))

# Intermediate Level (31–70):

# 31. Convert string "45.67" to float.
data = 'test@123'
data = float(343.33)
print(data)
print(type(data))

# 32. Format string "Hello {}" with your name.
name = input()
print(f'Hello {name}')
print('Hello %s' % name)   # c formate specifier

# 33. Format string "{} + {} = {}" with numbers 5, 3.

a , b = tuple(map(int, input().split()))
# a = int(input())
# b = int(input())
result = a+b
print(f'{a} + {b} = {result}')

# 34. Use f-string to print "My age is 20".
age = input('Enter your age: ')
print(f'My age is {age}')

# 35. Count vowels in string "Python".
word = input()
w = word.lower()
total = w.count('a') + w.count('e') + w.count('i') + w.count('o') + w.count('u')
print(f'Total vowel in {word} is: {total}')

# 36. Count consonants in "Python".
word = input()
w_lower = word.lower()
consonents = 0

all_consonents = 'bcdfghjklmnpqrstvwxyz'

for item in all_consonents:

    consonents += w_lower.count(item)

print(consonents)

# using in membership operator
for char in w_lower:
    if char in all_consonents:
        consonents +=1
print(consonents)

# 37. Check if string is alphanumeric.
user = input()
if user.isd():
    print('true')
else:
    print('false')


# 38. Check if string is lowercase.
user = input()
if user.islower():
    print('True')
else: 
    print('False')

# 39. Check if string is uppercase.
user = input()
if user.isupper():
    print('true')
else:
    print('false')

# 40. Find maximum character in string "python".
word = 'python'
print(max(word))


# 41. Find minimum character in string "python".
word = 'python'
print(min(word))


# 42. Convert string "hello world" to title case.
word = 'hello world'
print(word.title())

# 43. Swap case of "PyTHon".
word = 'pyThon'
print(word.swapcase())

# 44. Strip only leading spaces from " Python".
word = ' python'
print(word)
print(word.lstrip())    # cut the leading space 


# 45. Strip only trailing spaces from "Python ".
word = 'python '
print(word)
print(word.rstrip())       # remove the traling space

# 46. Split "apple,banana,cherry" by comma.
fruit = input().split(',')
print(fruit)


# 47. Replace all "a" with "@" in "banana".
fruit = 'banana'
print(fruit)
converted_fruit = fruit.replace('a', '@')
print(converted_fruit)

# 48. Count how many times "n" appears in "banana".
n = input()
word = 'banana'
counts = word.count(n)
if  counts:
    print(f'Appereance of this char in word: {word} is : {counts} ')
else:
    print(f'Sorry this is not available in word : {word} ')

       
# 49. Check if string "Python" is printable.
word = 'python'
if word.isprintable():
    print('True')
else:
    print('false')
    
# 50. Check if string " " is whitespace.
user = input()
if ' ' in user:
    print('This word contain white space')
else:
    print('This word not contain any white space')

# 51. Print Unicode code point of 'A'.
word = 'A'
print(ord(word))
# 52. Convert Unicode code point 65 to character.
print(chr(65))
# 53. Check if string ends with punctuation ".".
user = input()
print(user.endswith('.'))   # this method return the boolean value 

# with conditional statement
if user[-1] == '.':
    print('Correct end')
else:
    print('Incorrect end')

# 54. Check if string starts with "Py" ignoring case.
user = input().lower()
print(user.startswith('py'))

#  conditinal statement
if user[0:2] == 'py':
    print('Correct start')
else:
    print('Incorrect start') 


# 55. Extract middle character of string "Python".
word = 'python'
mid_word = len(word) // 2   # floor operator it will devide number and  round it to nearest number
print(word[mid_word])  # nearest finding
print(word[mid_word-1: mid_word+1]) # middle word multiple finder


# Advanced Level (71–100):
# 71. Remove all vowels from "Programming".
# 72. Count occurrences of each character in "banana".
# 73. Reverse each word in "Python is fun".
# 74. Check if string is palindrome.
# 75. Remove duplicates characters from "banana".
# 76. Replace every second character with "*".
# 77. Insert a character at specific index in string.
# 78. Convert string to list of ASCII values.
# 79. Convert list of ASCII values back to string.
# 80. Find longest word in "Python is fun and powerful".
# 81. Count total words in a string.
# 82. Find first non-repeating character.
# 83. Find all indices of "n" in "banana".
# 84. Split string into chunks of 3 characters.
# 85. Merge two strings by alternating characters.
# 86. Check if two strings are anagrams.
# 87. Count number of uppercase letters in a string.
# 88. Count number of lowercase letters.
# 89. Count number of digits in string "Python123".
# 90. Remove all digits from string "Py1th2on3".
# 91. Replace spaces with hyphens.
# 92. Remove all punctuation from a string.
# 93. Extract numbers from string "abc123def45".
# 94. Find common characters between two strings.
# 95. Capitalize first letter of every word.
# 96. Check if string contains only letters and numbers.
# 97. Check if string contains only letters.
# 98. Check if string contains only special characters.
# 99. Create acronym from "Hyper Text Markup Language".
# 100. Reverse words in "Python is fun" to "fun is Python".
