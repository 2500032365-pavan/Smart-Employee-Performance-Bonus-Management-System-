employees = []

def add_employee():

    name = input("Name: ")
    emp_id = input("ID: ")

    employees.append([name, emp_id])


def display():

    for emp in employees:

        print(emp)


def menu():

    while True:

        print("\n1.Add")
        print("2.Display")
        print("3.Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            add_employee()

        elif ch == 2:
            display()

        else:
            break


menu()
