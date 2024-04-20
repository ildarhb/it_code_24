students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

print('Все люди:')
print(students | employees)
print(students.union(employees))

print('Учится и работает')
print(students & employees)
print(students.intersection(employees))

print('Только работает, но не учится')
print(employees - students)
print(employees.difference(students))

print('Либо учится, либо работает, но не одновременно')
print(employees ^ students)
print(employees.symmetric_difference(students))