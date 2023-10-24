import random
import math

# encryption
alp = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5,
    'E': 6,
    'F': 7,
    'G': 8,
    'H': 9,
    'I': 10,
    'J': 11,
    'K': 12,
    'L': 13,
    'M': 14,
    'N': 15,
    'O': 16,
    'P': 17,
    'Q': 18,
    'R': 19,
    'S': 20,
    'T': 21,
    'U': 22,
    'V': 23,
    'W': 24,
    'X': 25,
    'Y': 26,
    'Z': 27,
    '.': 28,
    ',': 29,
    ' ': 30,
    '!': 31,
    '?': 32,
    '%': 33,
    '@': 34,
    '#': 35,
    '*': 36,
    '^': 37,
    ':': 38,
    ';': 39,
}
numbers = [i for i in range(1, 10001)]
prime = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Получение Значния по ключу
def alp_check():
    print('Введите слово для шифрования')
    vod = str.upper((input()))
    tapok = tuple(vod)
    input_list = []
    for i in tapok:
        for key, value in alp.items():
            if key == i:
                input_list.append(value)
    print(input_list)
    return generate_O_K(input_list)

# Генерация Открытого Ключа
def generate_O_K(input_list):
    p = random.choice(prime)
    q = random.choice([x for x in prime if x != p])
    N = p * q
    F_N = (p - 1) * (q - 1)
    e = random.choice([x for x in prime if x != p and x != q and math.gcd(x, F_N) and x > 1 and x < F_N])
    return generate_C_K(e, N, F_N, input_list)

# Генерация Закрытого Ключа
def generate_C_K(e, N, F_N, input_list):
    for D in reversed(numbers):
        Del = (D * e) % F_N
        if Del == 1:
            return crypt(e, D, N, input_list)
        else:
            continue

# Шифровка Ввода
def crypt(e, D, N, input_list):
    output_crypt = []
    crypt_num = 0
    for i in input_list:
        crypt_num = (i ** e) % N
        output_crypt.append(crypt_num)
    print('encryption', output_crypt)
    print('Open_Key', e, N)
    print('Close_Key', D, N)

# Получение ключа по значению
def alp_cry_check(output_list):
    final = []
    for i in output_list:
        for key in alp.keys():
            if alp[key] == i:
                final.append(key)
    print(''.join(final))
# Расшифровка Ввода
def decrypt():
    print('Введите зашифрованное слово через пробел')
    vod_crypt = input().split()
    print('Введите первую часть ключа D')
    D = int(input())
    print('Введите вторую часть ключа N')
    N = int(input())
    tapok_crypt = tuple(vod_crypt)
    output_list = []
    tapok_int = [int(x) for x in tapok_crypt]
    num = 0
    for i in tapok_int:
        num = i ** D % N
        output_list.append(num)
    return alp_cry_check(output_list)

# Выбор действия
def start():
    print('Если нужно зашифровать слово, то выберете 1, если расшифровать тогда нажмите 2')
    choice = int(input())
    if choice == 1:
        alp_check()
    elif choice == 2:
        decrypt()
    else:
        print('Незвестный запрос')


start()
