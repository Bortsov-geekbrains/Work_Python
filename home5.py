# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def Del_Word(s):
    return False if 'абв' in s else True

print('Введите текст ')
a = input()

a = a.split()
print(a)
a = list(filter(Del_Word,a))
print(a)

# 2. оздайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# вариант человек против человека:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# вариант человек против бота:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# вариант человек против бота c "интеллектом":
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# 3. Создайте программу для игры в ""Крестики-нолики"".

# Инициализация карты
maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# Инициализация победных линий
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Вывод карты на экран
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
     
# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
# Получить текущий результат игры
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
 
#Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O,sum_X):
 
    step = ""
    for line in victories:
        o = 0
        x = 0
 
        for j in range(0,3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1
 
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]
                 
    return step
 
#Искусственный интеллект: выбор хода
def AI():        
 
    step = ""
 
    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    step = check_line(2,0)
 
    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if step == "":
        step = check_line(0,2)        
 
    # 3) если 1 фигура своя и 0 чужих - ставим
    if step == "":
        step = check_line(1,0)           
 
    # 4) центр пуст, то занимаем центр
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5           
 
    # 5) если центр занят, то занимаем первую ячейку
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1           
   
    return step
 
# Основная программа
game_over = False
human = True
 
while game_over == False:
 
    # 1. Показываем карту
    print_maps()
 
    # 2. Спросим у играющего куда делать ход
    if human == True:
        symbol = "X"
        step = int(input("Человек, ваш ход: "))
    else:
        print("Компьютер делает ход: ")
        symbol = "O"
        step = AI()
 
    # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
    if step != "":
        step_maps(step,symbol) # делаем ход в указанную ячейку
        win = get_result() # определим победителя
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "дружба"
 
    human = not(human)        
 
# Игра окончена. Покажем карту. Объявим победителя.        
print_maps()
print("Победил", win)   

