def add_two_numbers(a, b):
    #result = 0
    try:
        result = a + b
    except UnboundLocalError:
        print('Error')
    except:
        print('Expected numbers')
    return result


if __name__ == '__main__':
    try:
        print(add_two_numbers(2, 'a'))
    except UnboundLocalError:
        print('Error')

    print('Success')
