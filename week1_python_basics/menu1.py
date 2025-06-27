import sys as s

choice = 0
menu = {
    1 : 'Yummy Amul icecream',
    2 : 'Spicy Masala Puri',
    3 : 'Durian Milkshake',
    4 : 'Lot of Pepsi and Kurkure',
    5 : 'End of Program'
}

while True:
    print('1:IceCream 2:Chats 3:MilkShake 4:Junk 5:Exit')
    choice = int(input('Your choice Plz: '))
    string = menu.get(choice, 'Invalid choice entered')
    print(string)
    if choice == 5:
        break