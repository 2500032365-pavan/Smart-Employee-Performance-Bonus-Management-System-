import json


employees = [

    {"id":101,"name":"Rahul","salary":40000,"rating":4.6}

]


with open("employees.json","w") as file:

    json.dump(employees,file)


with open("employees.json","r") as file:

    data=json.load(file)

    print(data)
