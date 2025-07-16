'''
fruits1 = {1:"apple", 2:"banana", 3:"cherry"}
fruits = ("apple", "banana", "cherry")
myit = iter(fruits)
print(next(myit))
print(next(myit))
print(next(myit))

print(type(myit))

for i in range(len(fruits)):
    print(i+1, fruits[i+1])

for fruit in fruits:
    print(key, value)
'''
vegetables = ['brinjal', 'onion', 'capsicum', 'ladies-finger' , 'tomato']

for vegetable in vegetables:
    print(vegetable)
print('--------------------------------')
itr = iter(vegetables)
while True:
    try:
        print(next(itr))
    except:
        print(end='')
        break

