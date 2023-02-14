import random

print('Добро пожаловать в числовую угадайку')

def is_valid(number):
        if number.isdigit() and int(number) > 0 and int(number) < 101:
            return True
        else:
            return False


def game():
    n, m = int(input('Введите нижнюю границу загаданного числа: ')), int(input('Введите верхнюю границу загаданного числа: '))

    num = random.randint(n, m)
    count = 0
    print('У вас пять попыток')
    
    while True:    
        if count != 5:
            count += 1
            print(f'{count} попытка')
            user_number = input(f"Введите число от {n} до {m}: ")
            if is_valid(user_number) == True:
                user_number = int(user_number)
                if user_number < num:
                    print('Ваше число меньше загаданного')
                elif user_number > num:
                    print('Ваше число больше загаданного')
                
                else:
                    print('Вы угадали, поздравляем!')
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    break
        
            else:
                print(f'А может быть все-таки введем целое число от {n} до {m} ?')
        else:
            print('Вы использовали все возможные попытки.')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

game()

def one_more_game():
    while True:
        answer = input('Хотите сыграть еще раз? (да/нет) ')
        if answer.lower() == 'да':
            game()
        else:
            print("До свидания! Будем ждать вас снова!")
            break

one_more_game()