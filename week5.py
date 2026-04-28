employees = []

def add_employee():

    emp = {

        "id": int(input("ID: ")),
        "name": input("Name: "),
        "department": input("Department: "),
        "salary": float(input("Salary: ")),
        "rating": float(input("Rating: "))
    }

    employees.append(emp)


add_employee()

print(employees)
