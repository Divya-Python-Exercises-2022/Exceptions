def add_two_numbers(a, b):
    result = 0
    val = None
    try:
        val = a + b
        result = int(a) + int(b)
    except ValueError:
        print('Expected numbers')
    except TypeError:
        print('Expected correct type of input')  # this is an output here
    return result, val


if __name__ == '__main__':
    print(add_two_numbers('abc', 2))
    print('Success')
