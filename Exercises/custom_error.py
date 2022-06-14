def add_numbers(a, b):
    class add2numbersError(Exception):
        try:
            if a is not int:
                raise add2numbersError('Invalid input for var a')
            if b is not int:
                raise add2numbersError('Invalid input for var b')
        except:
            print('Invalid input')


if __name__ == '__main__':
    add_numbers(1, 2)