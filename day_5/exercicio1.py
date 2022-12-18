'''

Create a function that takes an integer as an argument 
and returns "Even" for even numbers or "Odd" for odd numbers.

'''


def even_or_odd(number):
    dividir = number % 2
    if dividir == 0:
        print('Even')
    else:
        print('Odd')
    return number
even_or_odd(2)

