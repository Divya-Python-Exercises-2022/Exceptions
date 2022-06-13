def add_two_numbers(a, b):
    result = 0
    try:
        result = a + b
    except:
        print('Expected numbers')
    return result


if __name__ == '__main__':
    print(add_two_numbers(2, 'a'))
    print('Success')
