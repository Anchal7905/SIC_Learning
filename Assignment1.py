#SETS
'''Sets
1.	Set Creation: Create a set containing the first 10 prime numbers. Print the set and its length.
2.	Set Operations: Given two sets, A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, find the union, intersection, and difference of the two sets.
3.	Set Membership: Write a function that takes a set and an element as arguments and returns True if the element is in the set; otherwise, return False.
'''
#1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def first_n_primes(n):
    primes = []
    num = 2  # Start checking for primes from 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Print the first 10 prime numbers
print(first_n_primes(10))

#2

A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}
print("A union B is: ",A.union(B))
print("A intersection B is: ",A.intersection(B))
print("B intersection A is: ",B.intersection(A))
print("A diierence B is:",A - B)
print("B diierence A is:",B - A)

#3
set_element = {1,2,4,5,3,7,8,9}
user = int(input("enter element to check: "))
def check(set, input):  #function designed
    print(input in set)

check(set_element, user)      #function call



#TUPLE
'''
4.	Tuple Creation: Create a tuple containing the names of five different countries. Print each country using a loop.
5.	Tuple Indexing: Given a tuple of numbers (10, 20, 30, 40, 50), write a function that returns the second and fourth elements of the tuple.
6.	Tuple Unpacking: Write a function that takes a tuple of three elements and returns the sum of the first two and the product of the last two.
'''

#4
Countries = ('India','Germany','France','Russia','sweden')
for country in Countries:
    print(country,end=", ")

#5
tuple_list =  (10, 20, 30, 40, 50)
def show(list):
    print(f"second element of {list} is: ",list[2])
    print(f"fourth element of {list} is: ",list[4])

show(tuple_list)

def show2(list2):
    for index,num in enumerate(list2):
        if (index+1)%2 ==0 :
            print(f"{index+1} element of lsit is: ", num)
show2(tuple_list)

#6
tuple_value = (2,3,4)
def operation(list):
    print("Sum of first two digit is:",list[0]+list[1])
    print("Product of last two digit is:",list[-1]*list[-2])

operation(tuple_value)


# Dictionaries
'''
7.	Dictionary Creation: Create a dictionary that maps five countries to their capitals. Print the capital of one specific country.
8.	Dictionary Update: Write a function that adds a new key-value pair to a given dictionary and returns the updated dictionary.
9.	Dictionary Iteration: Given a dictionary of student names and their scores, write a function that prints each student’s name along with their score, sorted by score in descending order.
'''

# 7
dic = {"France":"Paris",
"Japan":"Tokyo",
"Brazil" : "Brasilia",
"Canada" : "Ottawa",
"Australia" : "Canberra"}
print(dic["France"])     #to print capital of one specific country

# 8
dic1 = {"India":"Delhi"}
dic.update(dic1)
print(dic)

#9
students = {"person1": 85,"person2": 50,"person3" : 90, "person4": 80}
students = sorted(students.items(),reverse=True)
print(students)

# Functions
'''
10.	Function with Default Argument: Write a function that takes a number and a default multiplier (e.g., 2) and returns the product. Test the function with and without providing the multiplier.
11.	Recursive Function: Write a recursive function to calculate the factorial of a given number.
12.	Lambda Function: Create a lambda function that takes a list of numbers and returns a new list containing only the even numbers.
'''
#10
def multiply(a, b=3):
    print(a*b)
multiply(2)
multiply(2,4)
#11
def fact(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num*fact(num-1)
    
n = int(input("enter the number: "))
result = fact(n)
print("Factorial is: ", result)


#12
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = lambda x: x % 2 == 0
even_numbers = [num for num in numbers if even(num)]
print(even_numbers)

#Combined Concepts
'''
13.	Nested Structures: Create a list of tuples, where each tuple contains a student's name and their score. Write a function that returns a dictionary mapping each student’s name to their score.
14.	Set from Dictionary: Given a dictionary where keys are student names and values are lists of grades, write a function that returns a set of all unique grades.
'''
#13
lst = [("name1", 20),("name2", 40),("name3", 80),("name4", 60)]
print({name: score for name, score in lst})

stu = {"ram": "A",
    "shyam":"B",
       "riya":"C",
       "seeta":"D",
       "geeta":"A",
       "priya":"B",
       "neha": "D"}
unique_value =[]
for value in stu.values():
    if value not in unique_value:
        unique_value.append(value)
print(unique_value)