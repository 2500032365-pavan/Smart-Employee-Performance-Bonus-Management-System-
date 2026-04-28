employees = []

while True:

    print("\n1.Add Employee")
    print("2.View Employees")
    print("3.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        emp_id = input("Enter ID: ")

        employees.append([name, emp_id])

    elif choice == 2:

        print(employees)

    elif choice == 3:
        break
