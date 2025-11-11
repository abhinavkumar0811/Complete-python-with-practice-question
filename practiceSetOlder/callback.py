'''callback '''
# def greet(greeting:str, name:str, gender:str):

#     print(f'{greeting}, {gender} {name}')

# def send_greet(callback, greeting, name, gender ):
#     return callback(
#         greeting,
#         name,
#         gender
#     )


# send_greet(greet, 'hello ', gender='Miss', name='Anju devi')
# greet('hello ', gender='Miss', name='Anju devi')

    

''' 
17 Simple greet callback:
 Write a function say_hello(name) that prints "Hello, <name>!".
 Write another function execute_callback(callback, name) that calls the callback with the given name.
 Call it using say_hello as a callback.
 '''

# def say_hello(name:str):
#     print(f'Hello , {name}')

# def excute_callback(callback, name:str):
#     callback(
#         name
#     )

# user = input('Enter name for greet: ')
# excute_callback(say_hello, user)

'''
18 Math operation callback:
Write a function add(a, b) and multiply(a, b).
Write a function calculator(a, b, operation) that takes operation as a callback and returns the result.
Test with both add and multiply.
'''

# add = lambda a,b: a+b
# multiply = lambda a,b: a*b

# def calculator(x:int, y:int, operation):
    
#     result = operation(x,y)
#     return result


# while True:

#     user = input('Calculator for not use press END: ')

#     if not user:
#         print('No data provided')
#         continue
    
#     if user.upper() == 'END':
#         print('Search end')
#         break

#         # map itrator
#     data = tuple(user.split(','))
#     data_type = tuple(map(int, data))


#     #   using loop 
#     # el_list = list(data)
#     # new_set_el = []
#     # for item in el_list:
#     #     new_set_el.append(int(item))
#     # data_type = tuple(new_set_el)
        

    
#     result = calculator(*data_type, add)
#     print(result)




# user = tuple(map(int, input('Enter number for calculate: ').split()))
# cb = calculator(*user, add)
# print(cb)


'''
19 Dynamic greeting:
Write greet(name, time_of_day) that prints "Good <time_of_day>, <name>".
Write a function send_greeting(name, callback) that asks the user for time of day and calls the callback.
'''

# def greet(name, time_of_day):
#     print(f'Good {time_of_day}, {name}')


# def send_greet(name, greeting):
#     time_of_day = input('Enter time of day (morning/ evening/ afternoon / night): ').strip()
#     return greeting(
#         name,
#         time_of_day
#     )

# send_greet('Mr. sent thomas', greet)


'''
20 Process list of numbers:
Write a function process_numbers(numbers, callback) that takes a list of numbers and a callback function.
 Callback 1: square(n) → returns n*n
Callback 2: cube(n) → returns n*n*n
 process_numbers should apply the callback to each element and return a new list.
'''

# square = lambda n: n*n

# cube = lambda n: n**3

# def function_process(numbers, callback):

#     # map 
#     # new_els = list(map(callback, numbers))

#     # loop 
#     new_el = []
#     for item in numbers:
#         result = callback(item)
#         new_el.append(result)
    
#     return new_el

# user = list(map(int, input('Enter number for adding element in list: ').split()))
# result = function_process(user, square)
# print(result)
# result = function_process(user, cube)
# print(result)



# square = lambda n: n*n

# def operation(number, calc):
#     return calc(number)

# user = int(input('Enter number for square: '))

# print(operation(user, square))

# user = list(map(int, input('Enter element of list: ').split()))
# new_el = []

# for item in user:
    
#     result = item * item
#     new_el.append(result)

# print(new_el)

'''
21 Filter and transform:
Filters elements with filter_callback
Applies transform_callback on the filtered elements
Write a function filter_and_transform(lst, filter_callback, transform_callback) that:   
Example: Filter even numbers, then double them.
'''


# def filters(lst:int):

#     ''' This function will filter even number list'''

#     if lst % 2 == 0:
#          return  True
#     else:
#         return  False

# def transform(lst:int):
     
#      return lst*2
    
# def filter_and_transform(lst:int, filter_callback, transform_callback):
     
#      ''' This function will return even number from list and transformed its elements '''
     
#      filtered = filter(filter_callback, lst)
#      transformed = map(transform_callback, lst)

#      return list(transformed)

# user = list(map(int, input('Enter element for cheack even or transform: ').split(',')))
# print(filter_and_transform(user, filters, transform))

''' 
(22) Chained callbacks:
Write a function pipeline(value, callbacks) that takes an initial value and a list of callbacks, and applies each callback in order, returning the final result.
'''

# add = lambda a: a+a

# square = lambda a: a*a

# sub = lambda a: a-5


# def pipline(value:int, callback:list):
#     '''
#     A function which take a current value and list of callbacks function with apply on the current value and reutn the cumulative result
#     '''
#     result = value
    
#     for func in callback:
#        result = func(result)

#     return result

# print(pipline(5, [add, square, sub]))  # multiple sequencial function

    


'''
 23 Event simulation:
Simulate a simple button click system:

def on_click(callback):
    print("Button clicked!")
    callback()

'''
# def techEvent(event):

#     if event == 'click':
#         print('Welcome to event Dashboard')
#     else:
#         print('Not onboard on Dashboard')

# def on_click(event, callback):
#     print('Button clicked!')
#     callback(event)

# user = input('Enter command: ')
# on_click(user, techEvent)

'''
24 Write two callback functions: say_hello and say_goodbye. Call on_click with each.
'''

# say_hello = lambda name: print(f'hello, {name}\n How are you?')
# say_goodbye = lambda name: print(f'Good bye {name}\nwe meet again!')

# def greet(name, callback, callback2):
#     user = input('Enter greet hello/goodbye: ')

#     print('Button clicked!')
#     if user == 'hello' or user == 'hola' or user == 'hii' or user == 'hey':
#         callback(name)
#     else:
#         callback2(name)




# name = input('Enter guest name: ')

# greet(name, say_hello, say_goodbye)



'''
25 Asynchronous simulation:
Write a function fetch_data(callback) that “pretends” to fetch data (just sleep for 2 seconds) and then calls the callback with some data.
Example: fetch_data(print_data) → prints the fetched data.
'''



'''
26 
Higher-order math:
Write apply_operation(a, b, callback) that applies any operation on a and b.
Then create callbacks for:

add

subtract

power
'''

'''
27 Custom sorting using callback:
Write a function custom_sort(lst, compare_callback) where compare_callback(a, b) returns True if a should come before b.
Use it to sort a list of strings by their length.

'''
# Callback Practice Questions (with HOF flavor)
'''

28 Basic Callback
Write a function execute(callback) that takes a function as input and runs it.
Example:

def hello():
    print("Hello from callback!")
execute(hello)  # Output: Hello from callback!
'''


'''
29 Math Operation Callback
Write a function calculate(a, b, operation) where operation is a callback like add, subtract, multiply, etc.
Example:

calculate(10, 5, add)      # 15
calculate(10, 5, multiply) # 50
'''


'''
30 Filter with Callback
Write a function custom_filter(numbers, callback) that returns a new list of elements that satisfy the callback condition.
Example:

custom_filter([1,2,3,4,5], is_even)  # [2,4]

'''

'''
31 Custom Map with Callback
Write a function custom_map(numbers, callback) that applies the callback to each element of the list and returns a new list.
Example:

custom_map([1,2,3], square)  # [1,4,9]

'''

'''
32 Chained Callbacks
Write a function process_string(s, callback1, callback2) that applies two callbacks in sequence.
Example:

def to_upper(s): return s.upper()
def reverse(s): return s[::-1]

process_string("hello", to_upper, reverse)  # "OLLEH"

'''

'''
33 Async Simulation with Callback (practice delayed execution)
Write a function delayed_execution(callback, seconds) that waits for seconds then executes the callback.
Example:

delayed_execution(hello, 3)  
# waits 3 seconds, then prints "Hello"
'''


'''
34 Custom Reduce with Callback
Implement custom_reduce(numbers, callback, initial) where callback combines elements into one value.
Example:

def add(x, y): return x+y
custom_reduce([1,2,3,4], add, 0)  # 10

'''

'''
35 Event System Simulation
Write a function on_event(event, callback) that triggers the callback when the event happens.
Example:

on_event("login", lambda: print("User logged in"))
'''


'''
36 make a dat formate with time_of_day
'''




'''
37 Easy Question
Write a function that takes a list and returns only the even numbers, using a callback function for filtering.
'''
# even_number = lambda x: True if x%2==0 else False

# def parcing(number:list, callback):
    
#     filtered_el = tuple(filter(callback, number))
#     return filtered_el

#       # return func(func(result))

#       # new_list = []

#       # for item in number:
#       #       result = callback(item)
#       #       if result == True:
#       #         new_list.append(result)

#       # return new_list


# el_list = [1,2,3,4,5,6,7,8,9,10]
# print(parcing(el_list, lambda a: a%2==0))


'''
38 Medium Question
Write a function pipeline(value, callbacks) that takes an initial value and a list of callbacks, and applies each callback in order. Return the final result.
Apply at least 3 different operations using callbacks to test it.

'''

# add = lambda a: a+a
# square = lambda a: a*a

# sub = lambda a: a-5

# def pipeline(value, callbacks):
    
# #     list of callback functions
#       result = value

#       for func in callbacks:
#            result = func(result)

#       return result

# results= pipeline(2, [ square,add, sub])
# print(results)
           

'''
39 Topic-based Question (Callbacks/HOFs)
Write a function apply_twice(func, value) that applies a callback function to a value two times and returns the result
'''
# add = lambda a: a+a



# def apply_twice(func, value):
     
#      ''' This function apply a function two time in one value and return value'''

#      results = value
#      for _ in range(0, 2):
#           results = func(results)
          
#      return results


# results = apply_twice(add, 5)
# print(results)


'''
40 Easy (map clone)

Write your own function my_map(callback, iterable) that works like Python’s map.

It should take a list and a callback.

It should return a new list where each element is transformed by the callback.
'''
'''
41 Medium (filter clone)

Write your own function my_filter(callback, iterable) that works like Python’s filter.

It should take a list and a callback.

It should return a new list with only the elements for which the callback returned True.
'''

'''
42 Topic-based (reduce clone)

Write your own function my_reduce(callback, iterable, initializer) that works like Python’s functools.reduce.

It should take a callback of two arguments, an iterable, and an optional initializer.

It should apply the callback cumulatively and return a single result.
'''




'''
Q43: Given a list of numbers, create a new list containing their squares.
'''
# nums = [1,2,3,4,5]
# square = [x*x for x in nums]

# squares_el = []
# for x in nums:
#     result = x*x
#     squares_el.append(result)

# squares_map = map(lambda x: x**2, nums)

# print(nums)
# print(square)
# print(squares_el)
# print(list(squares_map))
    



'''
Q44: Filter out all odd numbers from the list.

'''
# nums = [1,2,3,4,5,6,7]

# odd_nums = [odd for odd in nums if odd%2!=0 ]
# print(odd_nums)

# odd_num = []
# for odd in nums:
#     if odd%2==0:
#         odd_num.append(odd)
    
# print(odd_num)



'''
Q45: Convert all words in a list to uppercase.

'''
# words = ["apple","banana","cat"]
# word_uppercase = [word.upper() for word in words]
# print(word_uppercase)


'''
Intermediate Level

Q46: Create a list of "even" or "odd" labels for numbers 1-10.
'''
# nums = list(range(1,11))

# even_list = [even for even in nums if even%2==0]
# odd_list = [odd for odd in nums if odd%2!=0]

# print(even_list)
# print(odd_list)




'''
Q47: Flatten a 2D matrix into a single list.

'''
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# single_list = [element for item in matrix for element in item]
# print(single_list)

# el_item = []
# for item in matrix:
#     for el in item:
#         el_item.append(el)

# print(el_item)



'''
Q48: Copy a list (make a new list identical to original) using list comprehension.

'''
# nums = [10,20,30,40]
# original_ist = [item for item in nums]
# print(nums)



'''
49 Given a list of strings words = ["Apple", "Banana", "apple"], create a set of lowercase words.

'''
# words = ["Apple", "Banana", "apple"]
# word_set = {item.upper() for item in words}
# print(word_set)


'''
Q 50: Flatten a list of lists matrix = [[1,2],[3,4],[4,5]] into a set of unique numbers.

'''
# matrix = [[1,2],[3,4],[4,5]]
# unique_set = {item for element in matrix for item in element }
# print(unique_set)


# '''
# Q51: Generate a set of numbers from 1 to 15 but exclude multiples of 3.

# '''

# multiplier_set = {item for item in range(1, 15+1) if item%3!=0}
# print(multiplier_set)

'''
Advanced Level

Q52: Create a set of (x, y) pairs where x and y are from 1 to 3 but x != y.

'''
# pairs = {(x, y) for x in range(1, 4) for y in range(1, 4) if x != y}

# print(pairs)

# set_el = set()
# for x in range(1,4):
#     for y in range(1,3+1):
#         if x !=y:
#             set_el.add((x,y))
        
# print(set_el)

# unique_set_el = {(x,y) for x in range(1,4) for y in range(1,4) if x!=y}
# print(unique_set_el)



'''
Q53: Given a list of numbers, create a set of "even" or "odd" strings corresponding to each number.

'''
# nums = [1,2,3,4,5]
# filtred = {'even' if item%2==0 else 'odd' for item in nums}
# print(nums)
# print(filtred)

'''

Q54: Given a list of words, create a set of all unique characters used in the words.

'''
# words = ["apple","banana"]
# unique_char = {ch for item in words for ch in item}
# print(unique_char)



'''
Q55: Given a list of tuples coords = [(1,2),(3,4),(1,2),(5,6)], create a set of unique tuples.

'''
# coords = [(1,2),(3,4),(1,2),(5,6)]

# unique = []

# for nums in coords:
#     if nums not in unique:
#         unique.append(nums)

# print(coords)        
# print(set(unique))


# unique = set(coords)
# print(unique)

# unique_comprihen = {item for item in coords}
# print(unique_comprihen)