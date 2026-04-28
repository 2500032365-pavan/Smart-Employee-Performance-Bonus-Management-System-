employees = []

def add_employee():

    name = input("Name: ")
    emp_id = input("ID: ")

    employees.append([name, emp_id])


def search_employee():

    search = input("Enter name to search: ")

    for emp in employees:

        if emp[0].lower() == search.lower():

            print("Employee Found:", emp)


add_employee()
add_employee()

search_employee()
