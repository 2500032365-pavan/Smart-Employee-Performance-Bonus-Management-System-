class Employee:

    def __init__(self, emp_id, name, dept, salary, rating):

        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary
        self.rating = rating


    def display(self):

        print(self.emp_id, self.name, self.dept, self.salary, self.rating)
