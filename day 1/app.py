import repo

# Create employees
employee1 = (101, 'Banu', 23, 50000, True)
repo.create_employee(employee1)
print(f'Employee {employee1[1]} Created Successfully')
print('After Add:', repo.read_all_employee())

employee2 = (102, 'Manu', 23, 30000, True)
repo.create_employee(employee2)
print(f'Employee {employee2[1]} Created Successfully')
print('After Add:', repo.read_all_employee())

# Test read by id
employee = repo.read_by_id(102)
if employee is None:
    print('Employee Not Found')
else:
    print('Read by ID:', employee)

# Test update
employee_to_update = repo.read_by_id(102)
if employee_to_update is None:
    print('Employee Not Found')
else:
    id, name, age, salary, is_active = employee_to_update
    salary += 20000  # Increase salary
    updated_employee = (id, name, age, salary, is_active)
    repo.update(102, updated_employee)
    print(f'Employee {id} Updated Successfully')
    print('After Update:', repo.read_all_employee())

# Test delete
repo.delete_employee(102)
print('After Delete:', repo.read_all_employee())
