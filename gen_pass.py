import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
char = ''

pwd_num = int(input('Введите количество паролей для генерации: '))
pwd_len = int(input('Введите длину одного пароля: '))
pwd_dig = input('При генерации пароля включать цифры от 0 до 9? (y/n) ').lower()
pwd_alhup = input('При генерации пароля включать прописные буквы? (y/n) ').lower()
pwd_alhlow = input('При генерации пароля включать строчные буквы? (y/n) ').lower()
pwd_symb = input('При генерации пароля включать символы !#$%&*+-=?@^_ ? (y/n) ').lower()
pwd_excep = input('При генерации пароля включать неоднозначные символы il1Lo0O ? (y/n) ').lower()

if pwd_dig == 'y':
    char = char + digits
if pwd_alhup == 'y':
    char = char + lowercase_letters
if pwd_alhlow == 'y':
    char = char + uppercase_letters
if pwd_symb == 'y':
    char = char + punctuation
if pwd_excep == 'y':
    for c in 'il1Lo0O':
        char = char.replace(c,'')

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

for i in range(pwd_num):
    print(f'Ваш {i+1} пароль {generate_password(pwd_len, char)}')
