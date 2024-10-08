'''Sets
1.	Set Creation: Create a set containing the first 10 prime numbers. Print the set and its length.
2.	Set Operations: Given two sets, A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, find the union, intersection, and difference of the two sets.
3.	Set Membership: Write a function that takes a set and an element as arguments and returns True if the element is in the set; otherwise, return False.
'''

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


A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}
print("A union B is: ",A.union(B))
print("A intersection B is: ",A.intersection(B))
print("B intersection A is: ",B.intersection(A))
print("A diierence B is:",A - B)
print("B diierence A is:",B - A)

set_element = {1,2,4,5,3,7,8,9}
user = int(input("enter element to check: "))
def check(set, input):
    print(input in set)

check(set_element, user)