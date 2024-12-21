first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third: # проверяет несколько условий
    print('Вывод: 2')
else: # не нужно вводить условия, и если условия не подходят предыдущие вывод будет его
    print('Вывод: 0')