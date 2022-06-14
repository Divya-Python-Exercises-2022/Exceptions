if __name__ == '__main__':

    a = 5
    b = 0
    try:
        result = a/b
    except ZeroDivisionError:
        result = "You can't divide by 0"

    print(result)

