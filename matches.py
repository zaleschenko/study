"""
Игра в спички
Два игрока
В начале рандомно создается количество спичек от 10 до 40
Каждый участник может забирать не более 5 спичек
тот, кто забирает последнюю спичку - проиграл
"""
import random
player_number = 1
n = random.randint(10, 40)
while n > 0:
    print('На столе осталось', n, 'спичек.')
    print('Сейчас ходит игрок номер ', player_number)
    print('Введите следующее число.')
    a = int(input())
    n = n - a
    if player_number == 1:
        player_number = 2
    else:
        player_number = 1
print('Выиграл игрок номер', player_number)
