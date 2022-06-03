# 小公钥指数攻击Rabin算法
# 公钥e很小，一般为2，没有逆元，N可被分解
import gmpy2
import string
from Crypto.PublicKey import RSA

chars = string.ascii_letters + string.digits + '_' + '{}'

with open('pubkey.pem') as f:
    key = RSA.import_key(f.read())
    # print(f'e={key.e}')
    # print(f'n={key.n}')

n = key.n  # 87924348264132406875276140514499937145050893665602592992418171647042491658461
e = key.e  # 2

p = 319576316814478949870590164193048041239
q = 275127860351348928173285174381581152299

assert (p % 4 == 3 and q % 4 == 3)
cipher = int(open('flag.enc', 'rb').read().hex(), 16)
p_inv = gmpy2.invert(p, q)
q_inv = gmpy2.invert(q, p)

m_p = pow(cipher, (p + 1) // 4, p)
m_q = pow(cipher, (q + 1) // 4, q)

a = (p_inv * p * m_q + q_inv * q * m_p) % n
b = n - a
c = ((p_inv * p * m_q - q_inv * q * m_p) % n + n) % n
d = n - c

for s in (a, b, c, d):
    s = format(s, 'x')
    if len(s) % 2 != 0:
        s = '0' + s
    hx = bytes.fromhex(s).decode('latin')
    for ch in hx:
        if ch in chars:
            print(ch, end='')
        else:
            print('.', end='')
