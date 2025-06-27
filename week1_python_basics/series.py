n = int(input('Enter N (term) value: '))
m = int(input('Enter number of terms: '))

sum_of_series = 0
sign = -1
for i in range(m):
    numerator   = n ** 2 ** i
    dinominator = 2 * i + 1
    sign        = -1 * sign
    term        = numerator / dinominator * sign
    sum = sum + term
    # sum += (n ** 2 ** i) / (2 * i + 1) * (-1 ** i) 

'''
numerator   = n power 2 power i
dinominator = (2 * i + 1)
sign        = -1 power i 
term        = numerator / dinominator * sign
'''