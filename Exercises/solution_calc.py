# create a new exception class called "MathematicalError" from BaseException class
class MathematicalError(Exception):
    pass

# write a function called parse_input that pars(var[1]) != '+'es all the user input according to rules list defined in the exercise
# text


def parse_input(user_input):

    var = user_input.split()

    try:
        if len(var) != 3:
            raise MathematicalError('Input does not consist of three elements')
        elif type(float(var[0])) != float or type(float(var[2])) != float:
            #raise MathematicalError(f'{user_input} is not float')
            raise MathematicalError('The first and third input value must be numbers')
        elif (var[1]) != '+' and (var[1]) != '-':
            raise MathematicalError('Invalid operator. Can only use "+" or "-"')
    except ValueError:
        raise MathematicalError('The first and third input value must be numbers')
    return var


# function calculate takes 2 integers and an operation type as an argument
def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2


if __name__ == '__main__':

    while True:
        user_input = input('Enter the expression >>> ')

        if user_input == 'quit':
            break
        else:
            var = parse_input(user_input)
            result = calculate(float(var[0]), var[1], float(var[2]))
            print(result)
