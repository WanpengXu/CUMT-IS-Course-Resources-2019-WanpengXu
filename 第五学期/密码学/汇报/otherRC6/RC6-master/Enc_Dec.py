from Clear_work.RC6.Key_generation import *
from Clear_work.RC6.Raund import *
import random


#   Шифрования строки из 32 символов с ключом-строкой из 32 символов
def encrypt(value, main_key):
    #   Вырабатываю подключи
    K = main_key_generation(main_key)
    #   Парсю входящие параметры
    value_mas = key_parse(value)

    #   Начальное отбеливание
    value_mas = enc_start_xor(value_mas, K[0], K[1])
    #   20 раундов шифрования
    for i in range(2, 41, 2):
        value_mas = [int(i) for i in value_mas]
        value_mas = enc_raund(value_mas, K[i], K[i+1])
    #   Конечное отбеливание
    value_mas = enc_end_xor(value_mas, K[42], K[43])
    #   Возврат результата
    value_mas = [hex(i)[2:] for i in value_mas]
    for i in range(len(value_mas)):
        value_mas[i] = "".join(["0" for t in range(8 - len(value_mas[i]))]) + value_mas[i]
    value_mas = value_mas[0] + value_mas[1] + value_mas[2] + value_mas[3]
    return value_mas.upper()


#   Дешиифрование строки из 32 символов с ключом-строкой из 32 символов
def decrypt(value, main_key):
    #   Вырабатываю подключи
    K = main_key_generation(main_key)
    #   Парсю входящие параметры
    value_mas = key_parse(value)
    #   Начальное отбеливание
    value_mas = dec_start_xor(value_mas, K[42], K[43])
    #   20 раундов дешифрования
    g = [i for i in range(2, 41, 2)][::-1]
    for i in g:
        value_mas = [int(i) for i in value_mas]
        value_mas = dec_raund(value_mas, K[i], K[i+1])
    #   Конечное отбеливание
    value_mas = dec_end_xor(value_mas, K[0], K[1])
    #   Возврат результата
    value_mas = [hex(i)[2:] for i in value_mas]
    for i in range(len(value_mas)):
        value_mas[i] = "".join(["0" for t in range(8 - len(value_mas[i]))]) + value_mas[i]
    value_mas = value_mas[0] + value_mas[1] + value_mas[2] + value_mas[3]
    return value_mas.upper()


#   Начальное отбеливание шифроваия
def enc_start_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    B = mod(B + K1, 2**32)
    D = mod(D + K2, 2**32)
    return A, B, C, D
#   Конечное отбеливание шифрования
def enc_end_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    A = mod(A + K1, 2**32)
    C = mod(C + K2, 2**32)
    return A, B, C, D

#   Начальное отбеливание дешифроваия
def dec_start_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    A = mod(A - K1, 2**32)
    C = mod(C - K2, 2**32)
    return A, B, C, D
#   Конечное отбеливание дешифрования
def dec_end_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    B = mod(B - K1, 2**32)
    D = mod(D - K2, 2**32)
    return A, B, C, D



#   Мусор
"""
#for i in range(2, 41, 2):
#    print(i)
value = "B7E15163222222223333333344444444"
test = "B7E15163222222223333333344444444"
enc = encrypt(value, test)
print("enc", enc, len(enc))

dec = decrypt(enc, test)
print("dec", dec, len(dec))
"""
"""
co = 1
while True:
    d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    inpput_ = [random.choice(d) for i in range(32)]
    inpput = ""
    for i in inpput_:
        inpput += i
    key_ = [random.choice(d) for i in range(32)]
    key = ""
    for i in key_:
        key += i
    enc = encrypt(inpput, key)
    dec = decrypt(enc, key)
    if dec != inpput:
        print("ERROR-----------")
        print(co, inpput, key, enc, dec)
        u = input()
        co += 1
    else:
        print("Suc-----<")
        print(co, inpput, key, enc, dec)
        co += 1
"""
"""
inpp = "1DAA113E8E5BE4F0050AA8ECC1D8BF14"
key = "85BE53ECE50ABA11C3F3AAFD5CFA6CB4"
enc = encrypt(inpp, key)
print(enc)
print("\n")
dec = decrypt(enc, key)
print(dec)

#1DAA113E 8E5BE4F0 050AA8EC C1D8BF14
#1DAA113E 8E5BE4F0  50AA8EC C1D8BF14
"""
