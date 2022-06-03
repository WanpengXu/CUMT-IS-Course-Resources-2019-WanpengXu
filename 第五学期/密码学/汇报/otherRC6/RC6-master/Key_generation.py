import math
import random


#   Константы
P = 0xB7E15163
Q = 0x9E3779B9

#   Таблица превращений
value_table = {
    "0": 0, "1": 1, "2": 2, "3": 3,
    "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12,
    "D": 13, "E": 14, "F": 15
}


#   Основная функция генерациии подключей
def main_key_generation(main_key_STR):
    mas_main_key_INT = key_parse(main_key_STR)
    result_mas_INT = [0 for i in range(44)]

    result_mas_INT[0] = P
    for i in range(len(result_mas_INT)-1):
        result_mas_INT[i+1] = mod(Q + result_mas_INT[i], 2**32)

    A = B = i = j = 0
    for y in range(132):
        A = result_mas_INT[i] = lcm(mod(result_mas_INT[i] + A + B, 2**32), 3)
        B = mas_main_key_INT[j] = lcm(mod(mas_main_key_INT[j] + A + B, 2**32), mod(A + B, 32))
        i = mod(i + 1, 44)
        j = mod(j + 1, 4)

    return result_mas_INT



#   Функция преобразования строчного пароля в 4 int
#   значения соответствующих каждому 32-битному слову
def key_parse(main_key_STR):
    #print("main_key_STR", main_key_STR)
    mas_key_STR = [main_key_STR[(i-1)*8:i*8] for i in range(1, 5)]
    #print("mas_key_STR", mas_key_STR)
    mas_key_STR = [i[::-1] for i in mas_key_STR]
    #print("mas_key_STR", mas_key_STR)
    mas_key_INT = [math.pow(16, t)*value_table[i[t]] for i in mas_key_STR for t in range(len(i))]
    #print("mas_key_INT", mas_key_INT)
    mas_key_INT = [sum(mas_key_INT[(i-1)*8:i*8]) for i in range(1, 5)]
    #print("mas_key_INT", mas_key_INT)
    return mas_key_INT


#   Функция взятия числа value по модулю mod_
def mod(value, mod_):
    return value % mod_


#   Функция циклического сдвига врпаво
def rcm(value, len):
    mask = (value >> len) << len
    part = value ^ mask
    result = (part << 32 - len) ^ (mask >> len)
    return result


#   Функция циклического сдвига влево
def lcm(value, len):
    value = int(value)
    mask = (value >> (32 - len)) << (32 - len)
    part = value >> (32 - len)
    result = ((value ^ mask) << len) ^ part
    return result



#   Мусор
"""
print(mod(-4, 3))
"""
"""
cc = 0
while True:
    value = random.randrange(0, 0xFFFFFFFF)
    len = random.randrange(0, 32)
    in_r = rcm(value, len)
    in_l = lcm(in_r, len)
    if in_l != value:
        print(cc, "ERROR", value, in_l, len)
        f = input()
        cc += 1
    else:
        print(cc, "Suc", value, in_l, len)
        cc += 1

test = "B7E15163222222223333333344444444"
gg = main_key_generation(test)
print(gg, len(gg))
#key_parse(test)
"""