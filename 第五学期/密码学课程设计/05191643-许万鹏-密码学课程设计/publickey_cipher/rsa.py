import os
from random import randint
import libnum
import gmpy2
import base64


class RSA:
    def __init__(self):
        self.q = None
        self.p = None
        self.d = None
        self.n = None
        self.e = None

    def extended_gcd(self, a, b):
        """
        扩展的欧几里得算法计算最大公因数(a,b)以及x和y,满足sa+tb=(a,b)=gcd
        :return: (gcd,s,t)
        """
        if b == 0:
            return a, 1, 0
        else:
            gcd, s, t = self.extended_gcd(b, a % b)  # 先得到更里层的x₂,y₂,
            return gcd, t, s - (a // b) * t  # 再根据得到的x₂,y₂,计算x₁,y₁

    def mod_inverse(self, a, m):
        """
        计算a模m的逆元a^-1 (mod m)
        :param a: 底数
        :param m: 模数
        :return: 逆元
        """
        gcd, s, t = self.extended_gcd(a, m)  # sa + mt = 1
        # 若a,m不互素，即(a,m)>1，则不可逆
        if gcd != 1:
            raise Exception(str(a) + ' is not invertible!')
        else:
            return s % m

    def miller_rabin(self, n, k=10):
        """
        用Miler-Rabin算法进行素性检验
        :param n: 被检验的数
        :param k: 检验的次数，默认为10次
        :return: 是否通过检验
        """
        # 偶数直接不通过
        if n % 2 == 0:
            return False
        s, d = 0, n - 1
        # 将p-1分解为(2**s)d
        while d % 2 == 0:
            s += 1
            d //= 2
        # 进行k次检验566++3.+6
        for i in range(k):
            # 每次测试时,随机选取一个[1,n-1]的整数a
            a = randint(1, n - 1)
            x = pow(a, d, n)  # x = a**d mod(n)
            # 如果a**d(mod n)=1,说明当次检验通过(不是合数),进行下一轮检验
            if x == 1 or x == n - 1:
                continue
            else:
                flag = 0
                # 对所有的r∈[0, s-1],判断a**((2**r)*d) (mod n)是否等于-1，
                for r in range(s):
                    # x**pow(2,r) == a**d**pow(2,r)
                    x = pow(x, 2, n)
                    if x == n - 1:
                        flag = 1
                        break
                # 若a**d≠1(mod n)且a**pow(2,r)**≠
                if flag == 0:
                    return False
        return True

    def get_prime(self, n):
        """
        得到一个n位的素数(10进制表示)
        :param n: 二进制位数
        :return: n位素数(10进制表示)
        """
        while True:
            # 最高位为1,保证是n位（若随机生成可能为0，即n-1位）
            # 随机生成n-2位数
            # 最低位为1,保证是奇数
            num = '1' + ''.join([str(randint(0, 1)) for _ in range(n - 2)]) + '1'
            num = int(num, 2)
            if self.miller_rabin(num):
                return num

    def get_keys(self, nbits):
        """
        :param nbits: 密钥长度(512/1024/2048...)
        :return: 公钥(e,n),私钥d
        """
        nbits = int(nbits)
        while True:
            p = self.get_prime(nbits)
            # print("p: " + str(p))
            q = self.get_prime(nbits)
            # print("q: " + str(q))
            # 保证p != q
            if p == q:
                continue

            self.p = p
            self.q = q
            n = p * q
            phi_n = (p - 1) * (q - 1)
            e = randint(500, 10000)
            # 保证e与phiN互素
            if self.extended_gcd(e, phi_n)[0] == 1:
                # 计算私钥
                # print("p: " + str(p))
                # print("q: " + str(q))
                d = self.mod_inverse(e, phi_n)
                self.e = e
                self.n = n
                self.d = d
                return e, n, d

    def i2b_ASN1(self, n):
        """
        将数字转换为字节，返回字节流及其长度
        供ASN.1相关函数使用
        @param n: 待转换的数字
        @return: 字节流的长度,字节流
        """
        n = int(n)
        length = (len(bin(n)[2:]) + 7) // 8
        data = n.to_bytes(length, byteorder='big')
        return length, data

    def derInteger(self, n):
        """
        ASN.1标准中，INTEGER数据类型号为02。
            若数据长度小于128 Bytes，后接一个字节的数据长度，再接数据。
            否则，接一个0x8?，?代表数据长度为几个字节，之后为?字节的数据长度，再接数据。
            注意此处的数据为有符号的，即如果数据最高位为1，前面必须再接0x00，以避免产生负数。
            而根据观察，数据长度不需要带符号位。
            由此，这个函数不能处理负数的情况，如果数据长度非常非常大，也不能处理。
        @param n:
        @return:
        """
        length, data = self.i2b_ASN1(n)
        # print(data)
        if data[0] >= 128:
            data = b'\x00' + data
            length += 1
        if length < 128:
            return b'\x02' + int.to_bytes(length, 1, 'big') + data
        else:
            lengthlength, lengthdata = self.i2b_ASN1(length)
            return b'\x02' + int.to_bytes(128 + lengthlength, 1, 'big') + lengthdata + data

    def derTag(self, data):
        """
        ASN.1标准中，TAG数据类型号为30。
        @param data:
        @return:
        """
        if len(data) < 128:
            return b'\x30' + int.to_bytes(len(data), 1, 'big') + data
        else:
            lengthlength, lengthdata = self.i2b_ASN1(len(data))
            return b'\x30' + int.to_bytes(128 + lengthlength, 1, 'big') + lengthdata + data

    def derBitString(self, data):
        """
        ASN.1标准中，BITSTRING数据类型号为03。
        @param data:
        @return:
        """
        data = b'\x00' + data
        if len(data) < 128:
            return b'\x03' + int.to_bytes(len(data), 1, 'big') + data
        else:
            lengthlength, lengthdata = self.i2b_ASN1(len(data))
            return b'\x03' + int.to_bytes(128 + lengthlength, 1, 'big') + lengthdata + data

    def derOctetString(self, data):
        """
        ASN.1标准中，OCTETSTRING数据类型号为04。
        @param data:
        @return:
        """
        if len(data) < 128:
            return b'\x04' + int.to_bytes(len(data), 1, 'big') + data
        else:
            lengthlength, lengthdata = self.i2b_ASN1(len(data))
            return b'\x04' + int.to_bytes(128 + lengthlength, 1, 'big') + lengthdata + data

    def derRSAPublicKey(self, n, e):
        """
        生成RSA公钥的der格式字节流并转换为pem格式。
        @param n: 公钥n
        @param e: 公钥e
        @return: pem文件的列表
        """
        data = self.derBitString(self.derTag(self.derInteger(n) + self.derInteger(e)))

        data = b'\x30\x0d\x06\x09\x2a\x86\x48\x86\xf7\x0d\x01\x01\x01\x05\x00' + data
        # print(showbytes(derTag(data)))
        rsapk = base64.b64encode(self.derTag(data))
        ret = []
        ret.append(b'-----BEGIN PUBLIC KEY-----')
        for i in range(0, len(rsapk), 64):
            ret.append(rsapk[i:i + 64])
        ret.append(b'-----END PUBLIC KEY-----')
        return ret

    def derRSAPrivateKey(self, n, e, d, p, q):
        """
        生成RSA私钥的der格式字节流并转换为pem格式。
        @param n: 公钥n
        @param e: 公钥e
        @param d: 私钥d
        @param p: 大素数p
        @param q: 大素数q
        @return: pem文件的列表
        """
        para1 = d % (p - 1)
        para2 = d % (q - 1)
        para3 = gmpy2.invert(q, p)
        data = self.derTag(
            self.derInteger(0) + self.derInteger(n) + self.derInteger(e) + self.derInteger(d) + self.derInteger(p) +
            self.derInteger(q) + self.derInteger(para1) + self.derInteger(para2) + self.derInteger(para3))

        data = self.derTag(self.derInteger(
            0) + b'\x30\x0d\x06\x09\x2a\x86\x48\x86\xf7\x0d\x01\x01\x01\x05\x00' + self.derOctetString(data))
        # print(showbytes(data))
        rsapk = base64.b64encode(data)
        ret = []
        ret.append(b'-----BEGIN PRIVATE KEY-----')
        for i in range(0, len(rsapk), 64):
            ret.append(rsapk[i:i + 64])
        ret.append(b'-----END PRIVATE KEY-----')
        return ret

    # 输出私钥
    def outputPrivateKey(self, filepath, filename='private', sep='\n'):
        pempath = os.path.join(filepath, filename + '.pem')
        with open(pempath, 'w') as f:
            for i in self.derRSAPrivateKey(self.n, self.e, self.d, self.p, self.q):
                f.write(i.decode('utf-8') + sep)
        txtpath = os.path.join(filepath, filename + '.txt')
        with open(txtpath, 'w') as f:
            f.write('n = ' + str(self.n) + sep)
            f.write('e = ' + str(self.e) + sep)
            f.write('d = ' + str(self.d) + sep)
            f.write('p = ' + str(self.p) + sep)
            f.write('q = ' + str(self.q) + sep)
        return txtpath

    # 输出公钥
    def outputPublicKey(self, filepath, filename='public', sep='\n'):
        pempath = os.path.join(filepath, filename + '.pem')
        with open(pempath, 'w') as f:
            for i in self.derRSAPublicKey(self.n, self.e):
                f.write(i.decode('utf-8') + sep)
        txtpath = os.path.join(filepath, filename + '.txt')
        with open(txtpath, 'w') as f:
            f.write('n = ' + str(self.n) + sep)
            f.write('e = ' + str(self.e) + sep)
        return txtpath

    # 输入密钥
    def inputKey(self, keypath):
        with open(keypath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(' ')
                if line[0].lower() == 'n':
                    self.n = int(line[2])
                elif line[0].lower() == 'e':
                    self.e = int(line[2])
                elif line[0].lower() == 'd':
                    self.d = int(line[2])
                elif line[0].lower() == 'p':
                    self.p = int(line[2])
                elif line[0].lower() == 'q':
                    self.q = int(line[2])
        if self.n == 1 or self.e == 1:
            raise ('请检查n和e。')
        self.mode = 'public'
        if self.d == 1 or self.p == 1 or self.q == 1:
            print('公钥加载成功，当前运行模式为：仅加密。')
            return self.n, self.e
        self.mode = 'private'
        print('私钥加载成功，当前运行模式为：加密解密。')
        return self.n, self.e, self.d

    def encrypt(self, m, e, n):
        e = int(e)
        n = int(n)
        c = pow(m, e, n)
        return hex(c)

    def encrypt2(self, m):
        c = pow(m, self.e, self.n)
        return hex(c)

    def decrypt(self, c, d, n):
        d = int(d)
        n = int(n)
        m = pow(c, d, n)
        return m

    def decrypt2(self, c):
        m = pow(c, self.d, self.n)
        return m

    def crack(self, c, e, n, p, q):
        fai = (p - 1) * (q - 1)  # 欧拉函数 φ(n)=(p-1)(q-1)
        d = gmpy2.invert(e, fai)  # 解密钥（私钥） d*e%φ(n)=1 d*e=kφ(n)+1 关键！！
        m = gmpy2.powmod(c, d, n)  # 明文 m=c^d mod n

        flag = bytes.fromhex(hex(m)[2:]).decode()
        return flag

    def show(self):
        self.get_keys(512)
        self.outputPublicKey('key')
        self.outputPrivateKey('key')
        self.inputKey(r'key\private.txt')
        print('hello'.encode('utf-8'))
        x = self.encrypt(libnum.s2n('hello'), self.e, self.n)
        print(x)
        y = self.decrypt(int(x, 16), self.d, self.n)
        print(libnum.n2s(y))


def main():
    machine = RSA()
    machine.show()
    while True:
        mode = input("\n请选择模式:\n[E]加密Encrypt\t[D]解密Decrypt\t[C]破解Crack\n")
        match mode:
            case 'E' | 'e':
                m = input("请输入明文:\n")
                nbits = input("请输入位数（k*512）:\n")
                e, n, d = machine.get_keys(nbits)
                print("公共模数n为: " + str(n))
                print("公钥e为: " + str(e))
                print("私钥d为: " + str(d))
                m = libnum.s2n(m)
                # print(m)
                c = machine.encrypt(m, e, n)
                print("密文为: " + str(c))
            case 'D' | 'd':
                c = input("请输入密文(16进制):\n")
                d = input("请输入私钥d:\n")
                n = input("请输入公共模数n:\n")
                c = machine.decrypt(int(c, 16), d, n)
                c = libnum.n2s(c)
                print("密文为: " + str(c))
            case 'C' | 'c':
                c = input("请输入密文(16进制):\n")
                e = input("请输入公钥e:\n")
                n = input("请输入公共模数n:\n")
                p = input("请输入分解出的素数p:\n")
                q = input("请输入分解出的素数q:\n")
                m = machine.crack(int(c, 16), int(e), int(n), int(p), int(q))
                print(m)
            case _:
                continue


if __name__ == '__main__':
    main()
