N = int(input('Enter number of elements of the array: '))
try:
    numbers = [float(num) for num in input().split()]
    # Normal execution continues
    print(numbers)
except ValueError as err:
    print('You may have entered an invalid float number')
numbers.sort()
print(numbers)