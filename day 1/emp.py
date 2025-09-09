employees = []

#create employee
employee = ('Bhaskar', 25, 50000, True)
employees.append(employee)
employee = ('Bhanu', 22, 40000, True)
employees.append(employee)
employee = ('Muskan', 24, 30000, True)
employees.append(employee)

print('after add all employee: ', employees)

#search employee
i = 0
search = 'Muskan'
index = -1

for emp in employees:
    if emp[0] == search:
        index = i
        break
    i += 1

if index == -1:
    print('Employee not found')
else:
    search_employee = employees[index]
    print(search_employee)
    salary = float(input('Salary:'))
    employee = (search_employee[0], search_employee[1], salary, search_employee[3])
    employees[index] = employee
print('after search and update:', employees)

employee = ('Dravid', 50, 200.75, True)
employees.append(employee)
print('after add Dravid:', employees)
employees.pop()
print('after delete Dravid:', employees)

position = 1
employees.pop(position)
print('after delete Bhanu', employees)