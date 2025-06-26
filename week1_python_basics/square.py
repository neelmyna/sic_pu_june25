# Print a Square of n lines made up of @ char

def my_range(*args):
    if len(args) == 0 or len(args) > 3 or type(args[0]) is not int:
        raise TypeError
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            yield i
            i += 1
    elif len(args) == 3:
        if args[2] == 0:
            raise ValueError
        if args[2] > 0:
            i = args[0]
            while i < args[1]:
                yield i
                i += args[2]
        else:
            i = args[0]
            while i > args[1]:
                yield i
                i += args[2]

number_of_lines = int(input('Enter number of lines of the Square: '))

for i in my_range(number_of_lines):
    print('@ ' * number_of_lines)
