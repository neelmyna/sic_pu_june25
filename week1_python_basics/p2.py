# Check if a the given input number is Even or not.

print('Enter a number to check if it is Even: ')
input_number = int(input())

if input_number % 2 == 0:
    print(input_number, 'is an Even number')
else:
    print(input_number, 'is not an Even number')