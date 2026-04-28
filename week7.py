class Employee:

    def __init__(self, id, name, salary, rating):

        self.__id = id
        self.name = name
        self.salary = salary
        self.rating = rating


    def calculate_bonus(self):

        if self.rating >= 4.5:

            bonus = self.salary * 0.20

        elif self.rating >= 3:

            bonus = self.salary * 0.10

        else:

            bonus = self.salary * 0.05

        return bonus


emp = Employee(101, "Rahul", 40000, 4.6)

print("Bonus:", emp.calculate_bonus())
