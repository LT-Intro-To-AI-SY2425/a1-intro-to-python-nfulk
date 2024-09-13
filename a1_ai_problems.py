# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
assert fibonacci_iterative(0) == 0, "true"
assert fibonacci_iterative(1) == 1, "true" 

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
assert is_palindrome("racecar") == True, "true"
assert is_palindrome("python") == False, "false"

def is_prime(n):
    if n <= 1:
        return False
    if n<= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i<= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i+= 6
    return True
assert is_prime(2) == True, "test 1 failed"
assert is_prime(4) == False, "test 2 failed"