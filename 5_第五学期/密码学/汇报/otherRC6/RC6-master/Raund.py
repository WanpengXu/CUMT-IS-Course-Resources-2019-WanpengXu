from Clear_work.RC6.Key_generation import *


#   Один раунд шифрования
def enc_raund(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    t_1 = lcm(f(B), 5)
    t_2 = lcm(f(D), 5)
    A = mod(lcm(A ^ t_1, mod(t_2, 32)) + K1, 2**32)
    C = mod(lcm(C ^ t_2, mod(t_1, 32)) + K2, 2**32)
    return B, C, D, A


#   Один раунд дешифрования
def dec_raund(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    t_1 = lcm(f(A), 5)
    t_2 = lcm(f(C), 5)
    D = rcm(mod(D - K1, 2**32), mod(t_2, 32)) ^ t_1
    B = rcm(mod(B - K2, 2**32), mod(t_1, 32)) ^ t_2
    return D, A, B, C


#   f функция раудна
def f(x):
    return mod(x * (2 * x + 1), 2**32)



#   Мусор
"""
value_mas = [0xB7E15163, 0xB7E15163, 0xB7E15163, 0x9E3779B9]
enc_value = enc_raund(value_mas, 0xB7E15163, 0xB7E15163)
dec_value = dec_raund(enc_value, 0xB7E15163, 0xB7E15163)
print("value_mas", value_mas)
print("enc_value", enc_value)
print("dec_value", dec_value)
"""