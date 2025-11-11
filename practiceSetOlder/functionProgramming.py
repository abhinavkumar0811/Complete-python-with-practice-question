# Strings (1–8)

'''
Q1 Reverse a string without using the [::-1] slice.

'''

 

user = input('Enter string: ')
 
new_string = ''

for char in user:
    new_string = char + new_string  # prepand


print(user)
print(new_string)

# need more practice

# using stack

string_list = list(user)
string = ''

while string_list:
    string += string_list.pop()


print(string)


# using list 
# new_list = list(user)
# el_list = []

# for ch in new_list:
#     el_list.insert(0, ch)


# new_string = ''.join(el_list)
# print(new_string)



'''
Q2 Count the number of vowels in a string.

'''
# user = input('Enter string for counting vowel: ')

# vowel = 0

# for item in user:
#     if item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u':
#         vowel +=1

    
# if vowel <= 0:
#     print('No vowel exist')
# else:
#     print(vowel)


'''
Q3 Convert the first character of each word in a sentence to uppercase.

'''

# user = input('Enter sentence for captital first word: ')
# print(user.title())

'''
Q4 Check if a string is a palindrome.

'''

# def palindrom(string:str):

#     ''' This function is used to cheack word is palindro or not '''

#     palindrom_word = ''
#     for ch in string:

#         palindrom_word = ch + palindrom_word     #prepand
    
#     if palindrom_word != string:
#         return f'{[string]}: This word is not palindrom {[palindrom_word]}'
#     else:
#         return f'This {string} is palindrom {[palindrom_word]}'
    

# while True:

#     user = input('Enter word for cheack palindrom or not: ')

#     if not user:
#         print('please neter word for cheack palindrom')
#         continue


#     if user.upper() == 'STOP':
#         break
#     else:
#         print(palindrom(user))


    
'''
Q5 Count how many times a specific character appears in a string.

'''

# user = input('Enter word: ')
# subString = input('Enter sub string: ')

# # result = user.count(subString)
# # print(result)

# def count_sub_word(user:str, subChar:str):
    
#     char_count = 0

#     for char in user:

#         if char == subChar:
#             char_count +=1

#     return char_count

# print(count_sub_word(user, subString))






'''
Q6 Replace all spaces in a string with underscores.
'''

# data = ' abhinav kumar chaubey'
# new_data = data.replace(' ', '_')
# print(data)
# print(new_data)

# data = ' Aryan Chaubey '
# new_data = ''
# for el in data:
#     if el == ' ':
#         el = '_'

#     new_data += el

# print(new_data)
    

'''
Q7 Remove all vowels from a string.
'''


# sentance = input('Enter sentance: ')
# vowel = 'aeiou'
# new_sentance = ''


# for item in sentance:
#     if item not in vowel:
#         new_sentance +=item
    
# print(new_sentance)




# def remove_vowel(sentence:str):
#     sentance = input('Enter sentance: ')

#     sentance_list = list(sentance)
#     vowel = 'aeiou'
#     new_sentance = ''

#     for item in sentance_list:
#         if item.lower() in vowel:
#             sentance_list.remove(item)
    

#     new_sentance = "".join(sentance_list)
#     print(new_sentance)

    
# user = input('Enter sentance for removing vowel: ')
# print(remove_vowel(user))
        
        





'''
Q8 Find the longest word in a sentence.

'''

# def longest_word(sentance:str):
#     '''
#     This function returns the longest word

#     '''
#     # split_sentance = sentance.split()
#     sentance_list = list(map(str, sentance.split()))

#     longest_word = ''

#     for word in sentance_list:
#         if len(word) > len(longest_word):
#             longest_word =word      
        
#     return longest_word



# user = input('Enter sentance: ')
# print(longest_word(user))


# word_list = list(map(str, user.split()))
# largest_word = max(word_list, key=len)

# print(largest_word)



# Lists (9–16)
'''
Q9 Create a list of numbers from 1 to 20.
'''
# el_list = [item for item in range(1,21)]
# print(el_list)



'''
Q10 Extract all even numbers from a list.
'''
# user = map(int, input('Enter elemet for finding even number: ').split())
# even_list = [item for item in user if item%2==0]
# print(even_list)

'''
Q11 Find the sum of all elements in a list.

'''
# user = map(int, input('Enter elemet for finding even number: ').split())

# from functools import reduce
# sum_el = reduce(lambda x,y: x+y , user)
# print(sum_el)

# print(sum(user))


'''
Q12 Reverse a list without using reverse() or slicing.

'''

# el = [1,2,3,4,5,67,8,9]
# new_list = []

# new_el = [item , 0for item in el[:: -1]]
# print(new_el)

# for item in el:
#     new_list.insert(0, item)

# print(new_list)

# for item in range(len(el)-1, -1 ,-1):  # take index of last el, end in last, step back -1
#     print(item)
#     new_list.append(el[item])


# print(new_list)
'''
Q13 Find the maximum and minimum values in a list.

'''
# def min_max(number:list):

    # smallest = number[0] 
#     largest = number[0]

#     for el in number:
#         if el < smallest:
#             smallest = el
#         if el > largest:
#             largest = el

#     return f'Smallest num in list is {smallest}' f'Largest number in list is {largest}'

# size_of_list = input('Enter size of array: ')
# el_arr = []

# for repeate in range(int(size_of_list)):

#     number = int(input('Enter el for adding in array'))
#     el_arr += [number]

# result = min_max(el_arr)
# print(result)
    

# el_list = [4,6,7,8,9,34,56,78,4.5,1,3]
# minimum = min(el_list)
# maximum = max(el_list)
# print(minimum)
# print(maximum)




'''
Q14 Remove duplicates from a list.
'''

# now remove duplicates elements for array

# def duplicates_el(array:list):

#     ''' For removing duplicate elements we have many method (manually, set, membership cheack )'''
#     # set
#     set_duplicate_removed = set(array)
#     membership_cheack_duplicate_removed = []

#     # membership cheack
#     for duplicateEl in array:
#         if duplicateEl not in membership_cheack_duplicate_removed:
#             membership_cheack_duplicate_removed += [duplicateEl]

#     # done manually without membership

#     return set_duplicate_removed, membership_cheack_duplicate_removed



# user = input('Enter el for array: ')
# arr = user.split(',')
# int_arr = []
# print(arr)

# for item in arr:
#     int_arr += [int(item)]

# print(int_arr)
# done manually for some hands on practice 

# print(duplicates_el(int_arr))



# #  user with map 
# el_arr = list(map(int, input('Enter el: ').split()))
# unique_el = [] 
# [unique_el.append(item) for item in el_arr if item not in unique_el]

# print(el_arr)
# print(unique_el)


# this concept pending 
# using dict key with comprihensions
# dict.fromkeys(x, y)

# user = input('Enter el: ').split()
# no_duplicate = list(dict.fromkeys(user, None))
# print(no_duplicate)
# [no_duplicate.append() for item.fromkeys(user, none)]

'''
Q15 Multiply all elements in a list by 2.

'''
# callbacks
# mul = lambda x: x*2

# def multiplier(callback:None, /, nums:int): 

#     return callback(nums)

# print(multiplier(mul, 4))

# # using hof built-in funcs

# user = list(map(int, input('enter el: ').split()))
# multipling = map(mul, user)
# print(tuple(multipling))



'''
Q16 Flatten a list of lists with only one level.

'''

# def flatten_arr(array:list):

#     '''This function makes a flatten array in one level'''

#     # flatten_level = int(input('How many flatten level array you want: '))

#     flatten_arr = []
    
#     for item in array:
#         for el in item:
#             flatten_arr += [el]

#     return flatten_arr

# flatten_array = [[1,2], [3,4], [5,6]]
# print(flatten_arr(flatten_array))




'''
@17 Access the third element of a tuple.

'''

# user = tuple(map(int, input('Enter el: ').split()))
# print(user[2])

'''
Q18 Count how many times an element appears in a tuple.

'''

# tuples = 1,2,3,4,5,3,2,2
# # print(tuple.count(2))

# count_el = 2
# repeat = 0

# for el in tuples:
#     if el == count_el:
#         repeat += 1

# print(repeat)






'''
Q19 Convert a tuple into a list.

'''

# tupples = 1,2,4,5,6,7,8,9,10
# tuple_convert_to_list = [item for item in tupples]
# print(tupples)
# print(tuple_convert_to_list)
# print(type(tuple_convert_to_list))

'''
Q20 Concatenate two tuples.

'''

# first_tuple = 1,2,3,4,5
# second_tuple = 6,7,8,9,10,1
# concate = first_tuple + second_tuple
# print(concate)


# Sets (21–24)

'''
Q21 Create a set from a list to remove duplicates.

'''
# arr = [1,2,4,5,6,7,8,9,9,10,12,1,2,3,5,7]
# unique = set(arr)
# print(unique)


'''
Q22 Find the intersection of two sets.

'''

# a = {1,2,4,5,6,7}
# b = {1,2,4,5,7,8,8,9}
# print(a.intersection(b))

'''
Q23 Find the union of two sets.

'''

# a = {3,4,5,7}
# b = {9,2,1,6,7,8,5}
# print(a.union(b))
# '''
# Q24 Remove an element from a set safely.

# '''

# a = {1,2,3,4,5,6,7,8,8,9}
# a.discard(2)
# print(a)
# Dictionaries (25–28)

'''
Q25 Create a dictionary from two lists: keys and values.

'''

def dictronary(key:list, value:list):

   pass



# print(dictronary(key, value))

# key = [1,2,3,4,5]
# value = ['abhinav', 'aryan', 'zeewansh', 'swara', 'shivang']


# # Zip - it make a key value pair - tuple and dict convert tuple in to dictonary
# dict = dict(zip(key, value))
# print(dict)

# manual_dict = {}

# # maually using loop 
# for i in range(len(key)):
#    manual_dict[key[i]] = value[i]


# print(manual_dict)
   

'''
Q26 Get all keys from a dictionary.

'''

# mini_dictionary = {
#     "Serendipity": "The occurrence of events by chance in a happy or beneficial way.",
#     "Ephemeral": "Lasting for a very short time; fleeting.",
#     "Eloquent": "Fluent or persuasive in speaking or writing.",
#     "Tenacious": "Holding firmly to a goal or belief; persistent.",
#     "Ambiguous": "Open to more than one interpretation; unclear.",
#     "Catalyst": "Something that sparks change or action.",
#     "Resilient": "Able to recover quickly from difficulties; tough.",
#     "Nostalgia": "A sentimental longing for the past.",
#     "Pragmatic": "Dealing with things sensibly and realistically.",
#     "Quixotic": "Extremely idealistic, unrealistic, and impractical."
# }

# for  _, keys in enumerate(mini_dictionary):
#    print(keys)

# for item in mini_dictionary.keys():
#    print(item)


# for item in mini_dictionary:
#    print(item)

# key value with enumrate
# for _ ,(key, value) in enumerate(mini_dictionary.items()):
#    print(key)
#    print(value)
#    print(key, value)

'''
Q27 Get all values from a dictionary.

'''

# for value in mini_dictionary.values():
#    print(value)



'''
Q28 Check if a key exists in a dictionary.

'''

# mini_dictionary = {
#     "Serendipity": "The occurrence of events by chance in a happy or beneficial way.",
#     "Ephemeral": "Lasting for a very short time; fleeting.",
#     "Eloquent": "Fluent or persuasive in speaking or writing.",
#     "Tenacious": "Holding firmly to a goal or belief; persistent.",
#     "Ambiguous": "Open to more than one interpretation; unclear.",
#     "Catalyst": "Something that sparks change or action.",
#     "Resilient": "Able to recover quickly from difficulties; tough.",
#     "Nostalgia": "A sentimental longing for the past.",
#     "Pragmatic": "Dealing with things sensibly and realistically.",
#     "Quixotic": "Extremely idealistic, unrealistic, and impractical."
# }



# while True:

#     user = input('Enter key for search: ')

#     if not user:
#        print('Provide key for search')
#        continue

#     if user.lower() == "stop":
#        print('Search end')
#        break
#     else:
#        if user in mini_dictionary:
#           print("key Exsited")
#        else:
#           print("key not Exsited")



# Functions / HOFs (29–32)
'''
Q29 Write a function that squares a number.

'''

# square = lambda x: x*x
# user = int(input('Enter number for square: '))
# print(square(user))


'''
Q30 Write a function that accepts a list and returns a list of squares.

'''
# square = lambda x: x*x

# # callback
# def Square_array(callback:None, /, rray:list):
   
#    square_list_el = []
   
#    for el in rray:
#     #   square_list_el += [callback(el)]
#       square_list_el.append(callback(el))

    
#    return square_list_el
      
   



# el_list = list(map(int, input('Enter el: ').split()))
# result = Square_array(square, el_list )

# print(result)


# # Hofs
# square_list = list(map(square, el_list))
# print(square_list)

# # using comprihension 
# square_comprihension = [item for item in square_list if item*item]
# print(square_list)
   



'''
Q31 Write a function with a default argument.

'''

# def default_args(*args):
#    print(args)
   
#    '''   
#    args always return a tuple and kwargs return dictonary

#    '''


# default_args('aryan ', 'shivang', 'zeewansh', 'swara', 1 ,3 ,4)

'''
Q32 Use map to add 5 to each element in a list.

'''
# adder = lambda x: x+5
# user= list(map(int, input('Enter el: ').split()))
# adder_el_list = list(map(lambda x:x+5, user))
# print(user)
# print(adder_el_list)

# Control Structures (33–40)

'''
Q33 Print all numbers from 1 to 10 using a loop.

'''

# for number in range(1, 11):
#    print(number)

'''
Q34 Print only odd numbers from 1 to 20.

'''
# using loop 
# for odd in range(1, 20+1):
#    if odd%2!=0:
#       print(odd)

# if itrable then use filter 

# comprihension
# odd_array = [item for item in range(1, 21) if item%2!=0]
# print(odd_array)


'''
Q35 Sum all numbers from 1 to 50 using a loop.

'''


# sum = 0
# for number in range(1, 51):
#    sum += number

# print(sum)

# aggrigate builtin func 

# num_list = range(1,51)
# print(sum(num_list))

'''
Q36 Use a for loop with break when number 10 is reached.

'''

# for item in range(21):
#    print(item)
#    if item >=10:
#       break


# value = 20;
# item = 0
# while item <= value:
#    print(item)
   
#    if item >= 10:
#       break;

#    item += 1



'''
Q37 Use a for loop with continue to skip multiples of 3.

'''

# user = input('Enter number for loop: ')
# for el in range(int(user)+1):
   
#    if el%3==0:
#       continue
#    print(el)

'''
Q38 Print numbers from 1 to 10 using a while loop.

'''

# stop = 10
# start = 1

# while start <= stop:
#    print(start)

#    start +=1

'''
Q39 Check if a number is prime using a loop.

'''
# A number which is devide by itself and by 1 

# user = int(input('Enter number for finding prime number: '))

# if user == 1:
#    print('this is not prime number')

# if user%1 ==0 & user%user ==0:
#    print('This is prime number {}'.format(user))


'''
Q40 Print the multiplication table of a number using a loop.

'''

# user = int(input('Enter a table number which you want: '))

# def table(number:int):  

#    if table == 0: 
#       print('there is no table of Zero ')
      
      
#    #  loop over the number 
#    for item in range(1, 10+1):  
      
#    #   print( item * user)
#     print(f'{number} x {item} = {item*number} ')


# table(user)
      


'''
Q41 Given a list of numbers, return a list containing only the numbers that are divisible by 3 but not by 5.

'''

# user = list(map(int, input('Enter el for list entry').split(',')))

# def divisible_by_3(array:list):

#    ''' This function will return the number which divisible by 3 and not devisible by 5 '''

   

#    divisible = lambda num: num%3 == 0 and num%5 != 0 

#    divisible_by_3_not_by_5 = list(filter(divisible, array))

#    return divisible_by_3_not_by_5

# result = divisible_by_3(user)
# print(f'Result is: ', result)




# impliment using simple loop




      
'''
Q42 Reverse the words in a sentence while keeping the word order intact.

'''
# user = input('Enter word: ')
# print(user)


# def reverse_Word(word:list):

#    word = user.split()
#    # print(word)

#    unique_word_list = []

#    # reverse_Words = ''

#    '''
#    This function will reverse the word 
#    '''

#    for item in word:
#       unique_word_list.append(item)
   
#    # reverse_Word

#    unique_word_list.reverse()
#    reverse_Word = ' '.join(unique_word_list)
#    return reverse_Word


# print(reverse_Word(user))


   

'''
Q43 Find all numbers in a list that are greater than their previous element.

'''

'''
Q44 Given a string, return a new string with every second character removed.

'''
'''
Q45 Count the frequency of each character in a string and return as a dictionary.

'''

'''
Q45 Given a list of lists, flatten it into a single list without using built-in flattening functions.

'''
'''
Q46 Swap the first and last elements of a list.

'''
'''
Q47 Create a set of all characters in a string that appear more than once.

'''

'''
Q48 Given a dictionary, invert it so that values become keys and keys become values.

'''
'''
Q49 Find all pairs of numbers in a list that add up to a target sum.

'''
'''
Q50 Remove all duplicate words from a sentence while preserving order.

'''
# Given a list of tuples (name, age), return the names of people above 25.

# Generate a list of squares for numbers divisible by 4 between 1 and 50.

# Given two lists, return a list of elements common to both without duplicates.

# Count the number of words in a string that start with a vowel.

# Merge two dictionaries, summing values if keys are the same.

# Find the longest sequence of consecutive numbers in a list.

# Replace every occurrence of a substring in a string with another substring.

# Given a list, move all zeros to the end while maintaining order of other elements.

# Compute the factorial of a number using recursion.

# Return a list of all numbers in a list whose digits sum to an even number.

# Given a string, return the first non-repeating character.

# Check if two strings are anagrams of each other.

# Given a list of dictionaries with keys name and score, return the dictionary with the highest score.

# Find all numbers in a list that are prime.

# Given a string, return a new string with characters in sorted order.

# Rotate a list to the right by k steps.

# Count the number of unique elements in a list.

# Given a sentence, return a dictionary mapping each word to its length.

# Remove all elements from a list that are divisible by both 2 and 3.

# Given a string of numbers separated by spaces, return their sum.

# Given a list of strings, return the strings that are palindromes.

# Replace all vowels in a string with *.

# Return a list of all numbers less than 100 divisible by either 7 or 9.

# Given a nested list, return the sum of all numeric elements.

# Given a list, return True if it contains duplicates, else False.

# Return a list of numbers whose squares are greater than 50.

# Given a string, return the most frequent character.

# Swap keys and values in a dictionary where values are unique.

# Return all elements from a list that appear exactly twice.

# Given a list of integers, return a list of numbers whose digits are in strictly increasing order.

# Count the number of uppercase letters in a string.

# Given a list of numbers, return a list with each number replaced by the sum of its digits.

# Merge two lists into a dictionary where the first list is keys and the second is values.

# Return a list of all words in a string that are longer than 4 characters.

# Given a list of numbers, return the running sum as a new list.

# Return all numbers in a list that are perfect squares.

# Given a string, return True if it contains at least one digit, else False.

# Return a list of elements from a list that are greater than the average of the list.

# Given a dictionary of items and prices, return the most expensive item.

# Count the number of substrings of length 3 in a string that start and end with the same character.

# Given a list of numbers, return the second largest element.

# Remove all elements from a list that are not prime.

# Given a string, return a dictionary with each character and its positions in the string.

# Generate a list of numbers divisible by 3 or 5 up to 100.

# Given a list, return True if the list is sorted in ascending order.

# Return a list of all numbers whose binary representation contains exactly two 1s.

# Given a list of strings, return a list of strings sorted by their last character.

# Replace all occurrences of a character in a string with its ASCII value.

# Count the number of words in a string that contain at least one vowel.

# Given a list of numbers, return the length of the longest increasing subsequence.

# Create a dictionary from a list of numbers where keys are numbers and values are their cubes.

# Return all elements from a list that are multiples of both 2 and 3.

# Given a string, check if it can become a palindrome by removing at most one character.

# Generate a list of factorials for numbers from 1 to 10.

# Given a list, return a new list containing only elements at even indices.

# Given a string, return True if it contains all letters of the alphabet.

# Find all unique pairs in a list whose sum is divisible by 7.

# Given a list of words, return the words that contain all vowels at least once.

# Given a list of integers, return the product of all odd numbers.

# Given a nested dictionary, extract all the leaf values into a list.

# Given a string, return a string with characters appearing in sorted order by frequency.

# Remove all elements from a list that appear more than twice.

# Given a list, return a list of tuples (element, frequency) for each unique element.

# Return all numbers in a list that are divisible by their index (excluding index 0).

# Given a string, return True if it contains any consecutive repeating characters.

# Given a list of numbers, shift all negative numbers to the left and positive numbers to the right.

# Given a string, count the number of substrings that start with a vowel and end with a consonant.

# Given a list of numbers, return the median value.

# Given a string, return True if it contains a palindrome of length 5 or more.

# Given a list of numbers, return a list of numbers whose sum of digits is a prime number.

# Generate all possible substrings of a string that are palindromes.

# Given a list of numbers, return all triplets (a, b, c) where a + b = c.

# Flatten a nested list of arbitrary depth using recursion.

# Given a dictionary, return a new dictionary where keys are sorted by their values in descending order.

# Given a string, return the shortest substring that contains all unique characters of the string.

# Find all unique pairs of numbers from a list whose product is a perfect square.

# Given a list of strings, return all anagrams grouped together as sublists.

# Given a list, return a new list where each element is replaced by the product of all other elements.

# Generate all combinations of elements from two lists whose sum is even.

# Given a string, compress it using counts of repeated characters (e.g., "aaabb" → "a3b2").

# Implement a function that rotates a matrix 90 degrees clockwise.

# Given a list of numbers, return the longest subsequence where difference between consecutive elements is 1.

# Return all subsets of a set using recursion.

# Given a list of numbers, return all pairs where the sum is closest to a given target.

# Given a nested dictionary, flatten it to a single-level dictionary with compound keys.

# Count all distinct substrings of a string.

# Implement a function that returns True if a string can be rearranged into a palindrome.

# Return the top k frequent elements from a list.

# Given a list of numbers, find the maximum product of three numbers.

# Implement a function to check if a list can be partitioned into two subsets with equal sum.

# Given a string, find all permutations of it.

# Implement a memoized recursive Fibonacci function.

# Given a list, return the length of the longest increasing subsequence.

# Implement a queue using two stacks.

# Given a string, return the minimum number of characters needed to make it a palindrome.

# Remove duplicates from a list of dictionaries based on a key.

# Given a 2D grid of numbers, find the maximum sum path from top-left to bottom-right.

# Implement a function to find all valid parentheses combinations of length 2n.

# Given a list, find the largest contiguous subarray sum.

# Count the number of inversions in a list.

# Given a list of numbers, return a list of cumulative XOR values.

# Generate all binary numbers of length n without consecutive 1s.

# Given a string, find the longest substring with at most k distinct characters.

# Merge k sorted lists into a single sorted list.

# Implement a function to check if two trees are identical.

# Given a dictionary of words, return all words that can be formed by rearranging a target word.

# Implement a function to find the longest common prefix of a list of strings.

# Given a list, return True if it contains a 132 pattern (i < k < j).

# Count all palindromic substrings in a string.

# Given a list of intervals, merge all overlapping intervals.

# Implement a function that rotates a list by k positions in-place.

# Given a matrix, return all elements in spiral order.

# Implement a function to find the number of connected components in a graph.

# Generate all possible expressions by inserting + and - between digits to reach a target sum.

# Implement a Least Recently Used (LRU) cache.

# Given a list of numbers, find all unique quadruplets that sum to a target.

# Count all subarrays where the sum is divisible by k.

# Implement a function to find all prime numbers up to n using the Sieve of Eratosthenes.

# Given a string, find the longest substring that appears at least twice.

# Return all permutations of a list of numbers using recursion.

# Implement a stack that supports retrieving the minimum element in O(1) time.

# Find all numbers in a list that appear more than n//3 times.

# Given a 2D grid of 0s and 1s, find the largest rectangle of 1s.

# Implement a function to serialize and deserialize a binary tree.

# Given a list of numbers, return the maximum sum of a non-adjacent subsequence.

# Generate Pascal’s triangle up to row n.

# Implement a function to evaluate a postfix expression.

# Given a list of strings, return all words that differ by exactly one character.

# Implement a function to find the shortest path in a weighted graph using Dijkstra’s algorithm.

# Given a string, return the number of ways it can be decoded (like "123" → "ABC").

# Implement a function to find the median of two sorted arrays.

# Given a matrix, rotate it 180 degrees in-place.

# Return all possible subsets of size k from a list of numbers.

# Implement a function to check if a number is happy.

# Given a string, return the minimum number of cuts to partition it into palindromes.

# Implement a function to solve the N-Queens problem.

# Given a list of intervals, return the maximum number of overlapping intervals.

# Implement a trie and functions to insert and search words.

# Given a list of numbers, return the largest number formed by concatenating them.

# Find the longest substring where each character appears at least k times.

# Given a list, return the smallest missing positive integer.

# Implement a function to find all subsets whose sum equals a target.

# Given a 2D grid, find the number of islands.

# Given a string, find all unique substrings of length k.

# Implement a function to convert infix expressions to postfix.

# Given a list of numbers, find the maximum product subarray.

# Implement a function to find the topological order of a DAG.

# Given a string, find the shortest substring containing all unique characters.

# Implement a function to solve the coin change problem (minimum coins to make amount).





