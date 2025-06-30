import sys as s

def en_queue():
    element = input('Enter element to be inserted: ')
    queue.insert(0, element)
    print(f'{element} inserted in Queue')

def de_queue():
    if len(queue) == 0:
        print('Queue is empty')
        return
    print(f'The element {queue[-1]} is deleted')
    del queue[-1]

def display_queue():
    if len(queue) == 0:
        print('Queue is empty')
        return
    print('Queue elements are:', queue[::-1])

def exit_program():
    s.exit('End of program')

def invalid_choice():
    print('Invalid Choice entered')

def menu(choice):
    match(choice):
        case 1:
            en_queue()
        case 2:
            de_queue()
        case 3:
            display_queue()
        case 4:
            exit_program()
        case _:
            print('Invalid choice')

queue = [] # queue = list()
while True:
    print('1:Insert 2:Delete 3:Display-Q 4:Exit')
    choice = int(input('Your choice Plz: '))
    menu(choice)