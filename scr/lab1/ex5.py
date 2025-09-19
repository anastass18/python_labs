user_name = input(' ').split()
name = ' '.join(user_name)
print(f"ФИО: {name}")
print('Инициалы: {}{}{}'.format(user_name[0][0], user_name[1][0], user_name[2][0]))

print(f"Длина (символов): {len(name)}")
