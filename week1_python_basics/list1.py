
l1 = [1, 2, 5, 2, 4, 3]
print(l1)
element = 12
l1 = [1, 2]
try:
    print(l1[2])
    l1.remove(element) # error is raised
    print('Hi')
except ValueError as e:
    print(f'{element} was not found')
except Exception as e:
    print('An error occured at runtime may be while removing the element')
except:
    print('Some error occured')
print('Normal execution continued')