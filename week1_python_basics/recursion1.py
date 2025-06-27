def recursive_function(my_number):
    print('My Number = ', my_number)
    recursive_function(my_number+1)

print('Lets Start')
my_number = 1
recursive_function(my_number)