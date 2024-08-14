#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

def greet(name):
    pass
    print (f"Hello, {name}!")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


greet_with_default("Alice")  


greet_with_default()       

   


def add(num1, num2):
    return num1 + num2


result1 = add(5, 3)
print(result1) 

result2 = add(-1, 4)
print(result2)




def halve(number):
    return number / 2


result1 = halve(10)
print(result1) 

result2 = halve(7)
print(result2) 

