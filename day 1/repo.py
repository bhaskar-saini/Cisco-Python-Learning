Employees = []  # [(Id, Name, Age, Salary, is_active)]

# CRUD : Create, Read, Update, Delete

def create_employee(employee):
    global Employees
    Employees.append(employee)

def read_all_employee():
    return Employees

def read_by_id(id):
    for employee in Employees:
        if employee[0] == id:
            return employee
    return None

def update(id, new_employee):
    global Employees
    for i, employee in enumerate(Employees):
        if employee[0] == id:
            Employees[i] = new_employee
            break

def delete_employee(id):
    global Employees
    index = -1
    for i, employee in enumerate(Employees):
        if employee[0] == id:
            index = i
            break
    if index != -1:
        Employees.pop(index)
