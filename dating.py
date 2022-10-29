boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if (len(boys) != len(girls)):
    print("Количество участников разное")
boys.sort()
girls.sort()
dating = zip(boys, girls)
print("Идеальные пары: ")
for item in zip(boys, girls):
    print(f'{item[0]} и {item[1]}')