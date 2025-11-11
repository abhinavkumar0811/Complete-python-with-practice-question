# multiply = lambda x: x*2
# data = [1,2,3,4,5,6,7,8]
# transformed_data = map(multiply, data)   # function, itrable
# print(list(transformed_data))
# # map return itrator not itrable we can change it in itrable for see the result



# addition = lambda x,y: x+y
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [2,4,6,8,9]

# add_data = tuple(map(addition, a,b))
# print(add_data)    # it will end at the sortest

# nums = range(1, 10000, 4)
# transformed = map(lambda a: a*a, nums)
# print(type(transformed))   # <class map>

# # filter 
# even_selector = lambda x: True if x %2 !=0 else False
# data = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,2)
# even_el = filter(even_selector, data)
# print(tuple(even_el))  # it store all the true value

# odd_el = map(even_selector, data)
# print(list(odd_el))


# If None is passed instead of a function, it filters out all falsy values (0,1 None, False, "", [], [1,2]).

# filterd_tuple = filter(None, ('', 0,1, [3,6], False, []))
# print(tuple(filterd_tuple))



# # reduce
# def add(c,d):
#     return c+d

# el = [1,2,3,4,5,6,7,8,9,10]

# from functools import reduce
# add = reduce(add, el, 100)  # intizilaier the value start adding from the intilizier
# print(add)

# # sorted
# el = (45,33,22,77,66,88,22,33,1,2,3,6,5,7,8,99,100)
# sorted_el = sorted(el, reverse=True)
# print(sorted_el)


# data = [0,1 ,5 ,6 ,7]
# print(all(data))  # it stop on the first true value

# data = ['abhinav', 'aryan', 'zeewansh', 'swara', 'shivang']
# for key, value in enumerate(data ,1):
#     print(key, value)

# n = int(input('Enter size of tuple: '))
# integers = map(int, input().split())

# t = tuple(integers)
# print(hash(t))


# def swap_Case(string:str):
    
#     ''' This function change uppercase into lowercase and lowercase into uppercase '''
#     transformed_string = string.swapcase()
#     return transformed_string

# user = input('Enter string for swapcase: ')
# print(swap_Case(user))

# line = 'this is a word'
# el_data = line.split()
# print(el_data)
# a = '-'.join(el_data)
# print(a)


# def mutate_string(string:str, position:int, charactor:str):
    
#     new_el = list(map(str, string))
#     new_el = string
#     new_el[position] = charactor
#     string = ''.join(new_el)

#     return string

# print(mutate_string('Bishrampur', 5, 'e'))


# el = 'string'
# print(id(el))
# new_el = list(map(str, el))
# new_el[3] = 'T'
# el = ''.join(new_el)
# print(new_el)
# print(el)
# print(id(el))




# def count_substring(string, sub_String):
    
#     result = string.count(sub_String)
# #     return result
      
#       len_string = len(string)
#       len_sub_string = len(sub_String)

#       for item in range(len_string - len_sub_string+1):
#            print( item  )              



# string = input('Enter string for count substring: ')
# sub_string = input('Enter sub string for count: ')

# print(count_substring(string, sub_string))   # pending -hackerRank

# comprihensions

# el_list = [1,2,3,4,5,6,7,8]
# new_list = [square*2 for square in el_list if square%2==0]
#         #  expression   loop                 condition
# print(el_list)
# print(new_list)

# list comprihension 
# it is a compect way to create a list by itrating over the itrable and it will also make transorm and filter them

# el_list = [1,2,3,4,5,6,7,8,9,10]
   
# # using loop creating a new list       # it will itrate over he itrable an more complex but basic
# new_el = []
# for item in el_list:
#     new_el.append(item)


# # using map 
# new_map_list = list(map(int, el_list))  # shorter way for itrate over the itrable and return the itrator but it will not return the itrable

# #using list comprihension 
# new_list_el_comprihension = [x for x in new_el]   # same as map but it return the new itrable not itrator and it is fast wil manual function while map is fast with builtin fn

# print(el_list)
# print(new_el)
# print(new_map_list)
# print(new_list_el_comprihension)




# for item in range(3): 
#     for el in range(3):
#         print(item, el)



# for item in range(12):
#     for el in r):
#         print(item, el)


# Example:
# email = "abhi@example.com"
# if email.endswith(".com"):
#     print("Valid domain")







# Q1 Reverse a string without using the [::-1] slice.
# user = input("Enter you word for reverse: ");

# reversed_el = ""

# for el in user:
    
#     reversed_el = el + reversed_el;   #prepand
#     # reversed_el = el   

# print("reversed_el",reversed_el);


# user = input()
# userEl = list(map(str, user))
# reversed_el = []
# reversed_Str = ''

# for ch in userEl:

#     reversed_el.insert(0, ch)



# reversed_Str = ''.join(reversed_el)
# print(reversed_Str)
# print(type(reversed_Str))



# Q2 Count the number of vowels in a string.

# user = input()
# user_el = list(map(str, user.split()))
# vowel_return = 0

# for item in user_el:
#     if user_el.count('aeiou'):
#         vowel_return += 1


# print(vowel_return)


# user = 'abhcc'
# print(user.count('a'))






