#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    x, y = 0, 1
    for _ in range(length):
        sequence.append(x)
        x, y = y, x + y

    if length == 0:
            print([])
    
    else:
        print (sequence)
    
        pass     
        

    #Fibonacci sequence   
# def fib(n):

#     a = 0
#     b = 1

#     if n == 1:
#         print(a)

#     else:
#     print(a)
#     print(b)

#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)

# fib(10)
    