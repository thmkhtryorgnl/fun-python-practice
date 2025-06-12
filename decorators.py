#!/usr/bin/python3.13
#In this exmaple we write function for multiplication and use decorators to power inputs:
def pw(f):
    def power(n,o):
        p = n
        for _ in range(o-1): # multoplication to power:
            p = f(p,n)
        return p
    return power
        

@pw  #multiplication = pw(multiplication)
def multiplication(n,o):
    a = 0
    for _ in range(n):
        a+= o
    return a

print(multiplication(int(input()),int(input())))
