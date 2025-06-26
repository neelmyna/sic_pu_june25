# Accept a number from user and print itsa Math table

input_number = int(input('Enter a number to print its Math table: '))
# Assume for multiple upto 10
for i in range(1, 11):
    #print(input_number, '*', i, '=', (input_number * i))
    print('%2d * %02d = %03d' % (input_number, i, (input_number*i) ))

'''
9 * 1 = 9
9 * 2 = 18
num = 57.06
%05.1f
057.1
'''