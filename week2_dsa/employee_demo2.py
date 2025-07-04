import employee_crud_oop as e

def menu(choice, emp):
    match choice:
        case 1 : emp.insert_employee()
        case 2 : emp.delete_employee()
        case 3 : emp.update_employee()
        case 4 : emp.search_employee()
        case 5 : emp.read_all_employees()
        case 6 : pass
        case _ : print('Invalid Choice')

def start_app():
    employee = e.EmployeeCRUD()
    while True:
        choice = int(input('1:Insert 2:Delete 3:Update 4:Search 5:ListAll 6:Exit \nYour Choice: ' ))
        if choice == 6:
            break
        menu(choice, employee)
    print('Application closed')

if __name__ == '__main__': # Why we have to do this
    start_app()