#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    
        
    return "Access denied"
        

def hows_the_weather(temperature):
    # your code here
    if temperature == 33:
        return "It's brisk out there!"
    elif temperature == 55:
        return "It's a little chilly out there!"
    elif temperature == 99:
        return "It's too dang hot out there!"
    elif temperature == 75:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    if not num % 15:
        return "FizzBuzz"
    elif not num % 3:
        return "Fizz"
    elif not num % 5:
        return "Buzz"
    
    return num

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    
    print ("Invalid operation!")
    return None 
