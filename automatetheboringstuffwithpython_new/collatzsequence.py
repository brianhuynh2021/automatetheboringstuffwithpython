# Collatz Sequence

def collatz(number):

    if number % 2 == 0:
        return (number //2)
    elif number % 2 != 0:
        return (3*number + 1)
try:
    number = int(input('Enter a number: '))
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('Please enter an integer number')