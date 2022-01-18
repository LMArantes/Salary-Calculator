# Lucas Medeiros - ByLearn Challenge

import statistics

new_wage_dict = {}
above_average_list = []
biggest_wage_codes = []
smallest_wage_codes = []
above_average_codes = []

while True:
    worker_num = input('What is the number of the employee? ')
    if not worker_num.isnumeric():
        print('Please insert a NUMBER.')
        continue

    if worker_num == '0':
        break

    wage = input('Insert the salary: ')
    print('')

    try:
        float(wage)
    except ValueError:
        print('Please insert a NUMBER.')
        continue

    wage = float(wage)
    new_wage = wage

    if wage <= 0:
        print('Please insert a valid number.')
    elif wage <= 400:
        new_wage = (wage*115)/100
    elif wage <= 700:
        new_wage = (wage*112)/100
    elif wage <= 1000:
        new_wage = (wage*110)/100
    elif wage <= 1800:
        new_wage = (wage*107)/100
    elif wage <= 2500:
        new_wage = (wage*104)/100
    else:
        new_wage = wage

    new_wage = round(new_wage, 2)
    new_wage_dict[worker_num] = new_wage

biggest_wage = max(new_wage_dict.values())
smallest_wage = min(new_wage_dict.values())

# Selecionar a quais códigos (funcionários) se referem o maior/menor salário
for i in new_wage_dict.items():
    if i[1] == max(new_wage_dict.values()):
        biggest_wage_codes.append(i[0])
    else:
        continue

for i in new_wage_dict.items():
    if i[1] == min(new_wage_dict.values()):
        smallest_wage_codes.append(i[0])
    else:
        continue

print(f'\nThe biggest salary is: ${biggest_wage} in regards to the employee(s) of code '
      f'{biggest_wage_codes}.')
print(f'The smallest salary is: ${smallest_wage} in regards to the employee(s) of code '
      f'{smallest_wage_codes}.')
print(f'The average salary is: ${round(statistics.mean(new_wage_dict.values()), 2)} .')
print('\n Employees data:')

for worker in new_wage_dict:
    print(f'The employee of code {worker} has a salary of ${new_wage_dict[worker]} .')

for wage in new_wage_dict.values():
    if wage > statistics.mean(new_wage_dict.values()):
        above_average_list.append(wage)
    else:
        continue

above_percentage = (len(above_average_list)*100)/len(new_wage_dict.keys())

for i in new_wage_dict.items():
    if i[1] > statistics.mean(new_wage_dict.values()):
        above_average_codes.append(i[0])
    else:
        continue

print(f'\nThe above-average salaries are: {above_average_list} in regards to the employee(s) of code '
      f'{above_average_codes}.'
      f' \nTherefore, {above_percentage}% employees have a above-average salary.')
