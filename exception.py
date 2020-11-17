try:
    a = input('enter positive number')
    if a < 0:
        raise ValueError('This is not positive number')
except ValueError as ve:
    print(ve)