def add_two_numbers(a, b):
    result = 0
    val = None
    try:
        val = a + b
        result = int(a) + int(b)
        #return result
    except ValueError:
        print('Expected numbers')
        return 3
    except TypeError:
        print('Expected correct type of input')   # executed with invalid input
        return result  # executed with invalid input
    finally:
        print('Finally block is executed')  # This is executed (valid and invalid)
        return result, val  # This part is executed with valid input


if __name__ == '__main__':
    print(add_two_numbers(2, 2))  # valid input
    print(add_two_numbers(2, 'abc'))
    print('Success')
