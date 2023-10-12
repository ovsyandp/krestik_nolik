pole = [[1,2,3], [4,5,6], [7,8,9]]
a = None
count = 0
user1=input('Игрок 1: Введите свое имя: ')
user2=input('Игрок 2: Введите свое имя: ')
def proverka_user1():
    if pole[0][0] == 'X' and pole[0][1] == 'X' and pole[0][2] == 'X' or pole[1][0] == 'X' and pole[1][1] == 'X' and pole[1][2] == 'X' or pole[2][0] == 'X' and pole[2][1] == 'X' and pole[2][2] == 'X' or pole[0][0] == 'X' and pole[1][0] == 'X' and pole[2][0] == 'X' or pole[0][1] == 'X' and pole[1][1] == 'X' and pole[2][1] == 'X' or pole[0][2] == 'X' and pole[1][2] == 'X' and pole[2][2] == 'X' or pole[0][0] == 'X' and pole[1][1]  == 'X' and pole[2][2] == 'X' or pole[0][2] == 'X' and pole[1][1] == 'X' and pole[2][0] == 'X':
        print('Победил', user1)
        quit()
def proverka_user2():
    if pole[0][0] == 'O' and pole[0][1] == 'O' and pole[0][2] == 'O' or pole[1][0] == 'O' and pole[1][1] == 'O' and pole[1][2] == 'O' or pole[2][0] == 'O' and pole[2][1] == 'O' and pole[2][2] == 'O' or pole[0][0] == 'O' and pole[1][0] == 'O' and pole[2][0] == 'O' or pole[0][1] == 'O' and pole[1][1] == 'O' and pole[2][1] == 'O' or pole[0][2] == 'O' and pole[1][2] == 'O' and pole[2][2] == 'O' or pole[0][0] == 'O' and pole[1][1]  == 'O' and pole[2][2] == 'O' or pole[0][2] == 'O' and pole[1][1] == 'O' and pole[2][0] == 'O':
        print('победил', user2)
        quit()
def pokaz_pole():
    print(pole[0][0], pole[0][1], pole[0][2], sep=' ')
    print(pole[1][0], pole[1][1], pole[1][2], sep=' ')
    print(pole[2][0], pole[2][1], pole[2][2], sep=' ')
def step_user1():
    print(user1, 'введите цифру на место которой хотите поставить Х')
    a= int(input())
    if a == 1:
        if pole[0][0] == 1:
            pole[0][0] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 2:
        if pole[0][1] == 2:
            pole[0][1] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 3:
        if pole[0][2] == 3:
            pole[0][2] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 4:
        if pole[1][0] == 4:
            pole[1][0] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 5:
        if pole[1][1] == 5:
            pole[1][1] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 6:
        if pole[1][2] == 6:
            pole[1][2] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 7:
        if pole[2][0] == 7:
            pole[2][0] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 8:
        if pole[2][1] == 8:
            pole[2][1] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    elif a == 9:
        if pole[2][2] == 9:
            pole[2][2] = 'X'
            pokaz_pole()
            proverka_user1()
        else:
            print('Эта ячейка уже занята')
            step_user1()
    else:
        print('Ячейки с таким номером не существует')
        step_user1()
def step_user2():
    print(user2, 'введите цифру на место которой хотите поставить O')
    a = int(input())
    if a == 1:
        if pole[0][0]==1:
            pole[0][0] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 2:
        if pole[0][1]==2:
            pole[0][1] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 3:
        if pole[0][2]==3:
            pole[0][2] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 4:
        if pole[1][0] == 4:
            pole[1][0] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 5:
        if pole[1][1] == 5:
            pole[1][1] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 6:
        if pole[1][2] == 6:
            pole[1][2] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 7:
        if pole[2][0] == 7:
            pole[2][0] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 8:
        if pole[2][1] == 8:
            pole[2][1] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    elif a == 9:
        if pole[2][2] == 9:
            pole[2][2] = 'O'
            pokaz_pole()
            proverka_user2()
        else:
            print('Эта ячейка уже занята')
            step_user2()
    else:
        print('Ячейки с таким номером не существует')
        step_user2()
print('Поле для игры')
pokaz_pole()
while count<=8:
    step_user1()
    count+=1
    if count<=8:
        step_user2()
        count+=1
print('Ничья!')