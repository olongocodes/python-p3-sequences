#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    count=2

    if length == 0:
        print([])
    elif length == 1:
        print([a])
    else:
        print (a, end=" ")
        print (b, end=" ") 
        while count < length:
            c = a + b 
            print (c, end=" ")
            count +=1
            a = b
            b = c 

        pass     
        # fibonacci_sequence = [a, b]
        # for _ in range(2, length):
        #     c = a + b
        #     a, b = b, c
        #     fibonacci_sequence.append(c)

        # print(f"Fibonacci sequence up to length {length}:")
        # print(fibonacci_sequence)

# Example usage:
#print_fibonacci(10)
      
    