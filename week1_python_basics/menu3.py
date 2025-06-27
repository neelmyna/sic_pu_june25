import sys as s

def ice_cream():
    print('Yummy Amul icecream')

def chats():
    print('Yummy Amul icecream')

def milk_shake():
    print('Yummy Amul icecream')

def junk():
    print('Yummy Amul icecream')

def exit_program():
    s.exit('End of program')

def invalid_choice():
    print('Invalid Choice entered')

def menu(choice):
    match(choice):
        case 1:
            ice_cream()
        case 2:
            chats()
        case 3:
            milk_shake()
        case 4:
            junk()
        case 5:
            exit_program()
        case _:
            print('Invalid choice')

while True:
    print('1:IceCream 2:Chats 3:MilkShake 4:Junk 5:Exit')
    choice = int(input('Your choice Plz: '))
    menu(choice)