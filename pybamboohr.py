from PyBambooHR.PyBambooHR import PyBambooHR
bamboo = PyBambooHR(subdomain='eastvantage', api_key='50acba22408a0d0ebf4b0d1e5f36f64915dd7aa5')

employees = bamboo.get_employee_directory()
print(len(employees))
print('this is the list', employees[0])
for employee in employees:
    if employee['workEmail'] == "tutoo.philip@eastvantage-europe.com":
        print(employee)

