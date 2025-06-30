# def my_function(param1 = 55, param2): # Error
# def my_function(param1, param2 = 50, param3): # Error

def my_function(param1, param2 = 45): # default Args
    print(f'Num1={param1}, Num2={param2}')
    return param1 + param2

num1 = 49
num2 = 68

result = my_function() # Not allowed
print(f'Result = {result}')

result = my_function(num1) # 
print(f'Result = {result}')

result = my_function(num1, num2)
print(f'Result = {result}')
