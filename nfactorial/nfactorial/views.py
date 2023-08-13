from django.shortcuts import render
from django.http import HttpResponse

def nfactorial_view(request):
    return HttpResponse("Hello, nfactorial school!")

def add_view(request, first, second):
    result = first + second
    return HttpResponse(f"The sum of {first} and {second} is {result}.")

def upper_view(request, text):
    upper_text = text.upper()
    return HttpResponse(f"Uppercase text: {upper_text}")
def is_palindrome(s):
    return s == s[::-1]

def palindrome_view(request, word):
    is_palindrome_result = is_palindrome(word)
    return HttpResponse(f"Is '{word}' a palindrome? {is_palindrome_result}")


def calculator_view(request, first, operation, second):
    if operation == 'add':
        result = first + second
    elif operation == 'sub':
        result = first - second
    elif operation == 'mult':
        result = first * second
    elif operation == 'div':
        if second != 0:
            result = first / second
        else:
            return HttpResponse("Division by zero is not allowed.")
    else:
        return HttpResponse("Invalid operation.")

    return HttpResponse(f"Result: {result}")