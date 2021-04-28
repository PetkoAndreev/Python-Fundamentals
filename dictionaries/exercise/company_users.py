command = input()
companies = {}

while command != 'End':
    company, employee = command.split(' -> ')
    if company not in companies:
        companies[company] = [employee]
    else:
        if employee not in companies[company]:
            companies[company].append(employee)
    command = input()

companies = dict(sorted(companies.items(), key=lambda s: s[0]))

for company, employees in companies.items():
    for i in range(len(employees)):
        employees[i] = '-- ' + employees[i]
    print(company, end = '\n')
    print('\n'.join(employees))