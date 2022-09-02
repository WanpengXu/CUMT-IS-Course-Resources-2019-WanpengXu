from math import e
from scipy.constants import golden
from math import ceil, log2

w = 32
r = 20
b = 16
MOD = pow(2, 32)


def ROL(x, s):
    x &= 0xFFFFFFFF  # F^8==2^32
    s %= w
    res = ((x << s | x >> (w - s))) & 0xFFFFFFFF
    return res


def ROR(x, s):
    return ROL(x, w - s)


def odd(x):
    x = int(x)
    while x % 2 == 0:
        x += 1
    return x


# def k2l(key, u):
#     L = []
#     res = ''
#     for i in range(0, len(key)):
#         if i % u == 0 and i != 0:
#             L.append(res)
#             res = ''
#         res += bin(ord(key[i]))[2:].zfill(8)
#     L.append(res)
#     return L


def extend_key(key):
    P_w = odd((e - 2) * pow(2, w))
    Q_w = odd((golden - 1) * pow(2, w))
    u = w // 8  # 1word=8byte
    c = ceil(b / u)

    k = [ord(ch) for ch in key] + [0] * (b - len(key))
    L = []
    for i in range(0, len(k), u):
        L.append((k[i] << 24) + (k[i + 1] << 16) + (k[i + 2] << 8) + k[i + 3])

    S = [0] * (2 * r + 4)
    S[0] = P_w
    for i in range(1, 2 * r + 3 + 1):
        S[i] = (S[i - 1] + Q_w) % MOD
    A = B = i = j = 0
    v = 3 * max(c, 2 * r + 4)
    while v := v - 1:
        A = S[i] = ROL(S[i] + A + B, 3)
        B = L[j] = ROL(L[j] + A + B, A + B)
        i = (i + 1) % (2 * r + 4)
        j = (j + 1) % (c)
    return S


def encrypt(plaintext, k):
    ciphertext = ''
    S = extend_key(k)
    bin_plaintext = ''.join([bin(ord(ch))[2:].zfill(8) for ch in plaintext])
    bin_plaintext += '0' * (128 - len(bin_plaintext) % 128)
    for l in range(0, len(bin_plaintext), 128):
        A = int(bin_plaintext[l + 00:l + 32], 2)
        B = int(bin_plaintext[l + 32:l + 64], 2)
        C = int(bin_plaintext[l + 64:l + 96], 2)
        D = int(bin_plaintext[l + 96:l + 128], 2)

        B = (B + S[0]) % MOD
        D = (D + S[1]) % MOD
        for i in range(1, r + 1):
            t = ROL(B * (2 * B + 1), int(log2(w)))
            u = ROL(D * (2 * D + 1), int(log2(w)))
            A = (ROL(A ^ t, u) + S[2 * i]) % MOD
            C = (ROL(C ^ u, t) + S[2 * i + 1]) % MOD
            (A, B, C, D) = (B, C, D, A)
        A = (A + S[2 * r + 2]) % MOD
        C = (C + S[2 * r + 3]) % MOD

        ciphertext += f'{A:032b}{B:032b}{C:032b}{D:032b}'
    res = hex(int(ciphertext, 2))[2:]
    print(res)


def decrypt(ciphertext, k):
    S = extend_key(k)
    plaintext = ''
    for l in range(0, len(ciphertext), 128):
        A = int(ciphertext[l + 00:l + 32], 2)
        B = int(ciphertext[l + 32:l + 64], 2)
        C = int(ciphertext[l + 64:l + 96], 2)
        D = int(ciphertext[l + 96:l + 128], 2)
        C = (C - S[2 * r + 3]) % MOD
        A = (A - S[2 * r + 2]) % MOD
        for i in range(r, 1 - 1, -1):
            (A, B, C, D) = (D, A, B, C)
            u = ROL(D * (2 * D + 1), 5)
            t = ROL(B * (2 * B + 1), 5)
            C = ROR(C - S[2 * i + 1], t) ^ u
            A = ROR(A - S[2 * i], u) ^ t
        D = (D - S[1]) % MOD
        B = (B - S[0]) % MOD
        plaintext += f'{A:032b}{B:032b}{C:032b}{D:032b}'

    res = ''
    for i in range(0, len(plaintext), 8):
        res += chr(int(plaintext[i:i + 8], 2))
    print(res)


while True:
    type = input()
    if type == 'E':
        plaintext = input("请输入明文:\n")
        k = input("请输入密钥(小于32字节):\n")
        encrypt(plaintext, k)
    elif type == 'D':
        ciphertext = input("请输入密文:\n")
        ciphertext = ''.join([f'{int(ch, 16):04b}' for ch in ciphertext])
        k = input("请输入密钥(小于32字节):\n")
        decrypt(ciphertext, k)
