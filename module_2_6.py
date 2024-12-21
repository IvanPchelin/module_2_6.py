a = int(input('Введите целое число от 3 до 20: '))
def get_parol(nomer):
    parol =  ""
    for b in range(1, nomer):
        for c in range(2, nomer):
            if b >= c:
                continue
            if nomer % (b+c) == 0:
             parol += str(b) + str(c)
    return parol
result = get_parol(a)
print('Пароль:', result)