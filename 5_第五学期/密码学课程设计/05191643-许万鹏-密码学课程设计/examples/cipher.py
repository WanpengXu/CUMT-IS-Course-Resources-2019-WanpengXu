import gmpy2
import string
from Crypto.Util.number import long_to_bytes

chars = string.ascii_letters + string.digits + '_' + '{}'
f = open('cipher', 'rb')
cipher = f.readlines()[6:-1]
ns = []
cs = []
e = 65537
cipher = [line.decode() for line in cipher]
for line in cipher:
    if 'n' in line:
        ns.append(int(line[4:].replace('\n', '')))
    elif 'c' in line:
        cs.append(int(line[4:].replace('\n', '')))
for i in range(len(ns)):
    for j in range(i + 1, len(ns)):
        if gmpy2.gcd(ns[i], ns[j]) != 1:
            n = ns[i]
            c = cs[i]
            p = gmpy2.gcd(ns[i], ns[j])
            q = n // p
            phi_n = (p - 1) * (q - 1)
            d = gmpy2.invert(e, phi_n)
            m = long_to_bytes(pow(c, d, n)).decode('latin')
            for ch in m:
                if ch in chars:
                    print(ch, end='')
                else:
                    print('.', end='')
