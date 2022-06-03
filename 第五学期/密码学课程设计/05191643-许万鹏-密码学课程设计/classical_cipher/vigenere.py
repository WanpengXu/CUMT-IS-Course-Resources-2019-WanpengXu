import wordninja


class Vigenere(object):
    def __init__(self, key: str = '') -> None:
        self.k = key.upper()
        self.p = ''
        self.c = ''
        self.alpha_c = ''
        self.probability = [0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881, 0.0158610, 0.0492888,
                            0.0558094,
                            0.0009033, 0.0050529, 0.0331490, 0.0202124, 0.0564513, 0.0596302, 0.0137645, 0.0008606,
                            0.0497563,
                            0.0515760, 0.0729357, 0.0225134, 0.0082903, 0.0171272, 0.0013692, 0.0145984, 0.0007836]

    @property
    def key(self) -> str:
        return self.k

    @property
    def plaintext(self) -> str:
        return self.p

    @property
    def ciphertext(self) -> str:
        return self.c

    def encrypt(self, plaintext: str) -> None:
        """
        维吉尼亚加密
        @param plaintext: 明文
        @return: 无
        """
        self.clear(False)
        self.p = plaintext
        len_k = len(self.k)
        j = 0
        for i, _p in enumerate(self.p):
            if _p.isupper():
                self.c += chr(ord('A') + ((ord(_p) - ord('A')) + (ord(self.k[j % len_k]) - ord('A'))) % 26)
            elif _p.islower():
                self.c += chr(ord('a') + ((ord(_p) - ord('a')) + (ord(self.k[j % len_k]) - ord('A'))) % 26)
            else:
                self.c += _p
                continue
            j += 1

    def decrypt(self, ciphertext: str) -> None:
        """
        维吉尼亚解密
        @param ciphertext: 密文
        @return: 无
        """
        self.clear(False)
        self.c = ciphertext
        len_k = len(self.k)
        j = 0
        for i, _c in enumerate(self.c):
            if _c.isupper():
                self.p += chr(ord('A') + ((ord(_c) - ord('A')) - (ord(self.k[j % len_k]) - ord('A'))) % 26)
            elif _c.islower():
                self.p += chr(ord('a') + ((ord(_c) - ord('a')) - (ord(self.k[j % len_k]) - ord('A'))) % 26)
            else:
                self.p += _c
                continue
            j += 1

    def crack(self, ciphertext: str) -> None:
        """
        维吉尼亚唯密文攻击
        @param ciphertext: 密文
        @return: 无
        """
        self.clear()
        # 确定密钥长度
        self.c = ciphertext
        self.alpha_c = self.c_alpha(self.c)
        m = self.pre_10(self.alpha_c)
        key_len = self.gcd(m[1:3 + 1])  # 取1~3为高可信密钥长度，取他们的最大公因数为密钥长度
        # key_len = int(input())  # 输入猜测的秘钥长度
        # 确定密钥
        self.one_key(ciphertext, key_len)
        self.decrypt(ciphertext)

    @staticmethod
    def gcd(ls: list) -> int:
        """
        用于求多个整数的最大公因数
        @param ls: 若干整数组成的列表
        @return: 列表中所有整数的最大公因数
        """
        smallest = min(ls)
        for i in reversed(range(2, smallest + 1)):
            if not list(filter(lambda x: x % i != 0, ls)):
                return i

    @staticmethod
    def c_alpha(cipher: str) -> str:
        """
        用于去除（密文）字符串中的非字母字符
        @param cipher: （密文）字符串
        @return: 仅包含字母字符的字符串
        """
        cipher_alpha = ''
        for c in cipher:
            if c.isalpha():
                cipher_alpha += c
        return cipher_alpha

    def count_ic(self, cipher: str) -> float:
        """
        用于计算密文的重合指数
        @param cipher: 待求重合指数的密文字符串
        @return: 密文字符串的重合指数
        """
        x = [0.0 for _ in range(26)]
        cipher = self.c_alpha(cipher)
        len_c = len(cipher)
        if cipher == '':
            return 0
        else:
            for ch in cipher.lower():
                x[ord(ch) - ord('a')] += 1
            ic_1 = 0  # IC的无偏估计值 P57
            for i in range(26):
                ic_1 += ((x[i] / len_c) * ((x[i] - 1) / (len_c - 1)))
            return ic_1

    def count_key_len_ic(self, key_len: int) -> float:
        """
        用于计算指定密钥长度的密文所对应的平均重合指数
        @param key_len: 密钥长度
        @return: 指定密钥长度的密文所对应的平均重合指数
        """
        un_cip = ['' for _ in range(key_len)]  # un_cip 是分组
        un_cip2 = [0.0 for _ in range(key_len)]
        aver_ic = 0.0
        for i in range(len(self.alpha_c)):  # 形成每组的密文子串
            un_cip[i % key_len] += self.alpha_c[i]
        for i in range(key_len):  # 计算每个密文子串的IC'及平均IC
            un_cip2[i] = self.count_ic(un_cip[i])
            aver_ic += un_cip2[i]
        aver_ic /= key_len
        return aver_ic

    # 找出最可能的前十个秘钥长度, 然后选取靠前的几个计算gcd（在crack_key函数中）
    def pre_10(self, cipher: str) -> list:
        """
        用于找出密文最可能的前十个密钥长度
        @param cipher: 密文字符串
        @return: 按可能性升序排序的密钥长度
        """
        # 计算密钥长度为1~50时的IC
        m = [(1, self.count_ic(cipher))] + \
            [(0, 0.0) for _ in range(49)]
        for i in range(2, 50):  # 在最后一列上求距0.065的距离（对0.065的绝对值）
            m[i] = (i, abs(0.065 - self.count_key_len_ic(i)))  # 当密钥长度大于2时有不止一个密文子串，所以再写一个方法
        m = sorted(m, key=lambda x: x[1])  # 按照距0.065的距离排序，越小越接近真实密钥长度
        # for i in range(1, 10):
        #     print(m[i])
        return [i[0] for i in m]  # 按密钥长度可信性取出长度

    # 猜测单个秘钥得到的重合指数
    def count_ic2(self, cipher: str, n: int) -> float:
        """
        用于计算指定单个密钥的密文所对应的重合指数
        @param cipher: 密文字符串
        @param n: 指定单个密钥，使用偏移量表示，n = ord('指定密钥') - ord('A')
        @return: 指定单个密钥的密文所对应的重合指数
        """
        frequency = [0.0 for _ in range(26)]
        cipher = self.c_alpha(cipher)
        n_prime = len(cipher)
        for ch in cipher.lower():  # 计算所有字母的频数，存在数组frequency当中
            frequency[(ord(ch) - ord('a') - n) % 26] += 1
        ic_2 = 0
        for i in range(26):
            ic_2 += (frequency[i] / n_prime) * self.probability[i]
        return ic_2

    def one_key(self, cipher: str, key_len: int) -> None:
        """
        用于得到一个确定的密钥
        @param cipher: 密文字符串
        @param key_len: 确定的密钥长度
        @return: 无
        """
        un_cip = ['' for _ in range(key_len)]
        cipher_alpha = self.c_alpha(cipher)
        for i in range(len(cipher_alpha)):  # 完成分组工作
            un_cip[i % key_len] += cipher_alpha[i]
        for i in range(key_len):
            # print(i)  # 这里可以将排名前5的猜测秘钥打印出来
            self.pre_n_key(un_cip[i])  # 猜测每个密文子串的密钥（单表分析）

    # 找出前n个最可能的单个秘钥k_i
    def pre_n_key(self, cipher: str) -> None:
        """
        用于得到单个密钥（作用于单表）
        @param cipher: 使用单表加密的密文字符串
        @return: 无
        """
        m = [('', 0.0) for _ in range(26)]
        for i in range(26):
            m[i] = (chr(ord('a') + i), abs(0.065 - self.count_ic2(cipher, i)))  # 计算每个字母为密钥的可能性，距0.065的距离越小可信度越高
        m = sorted(m, key=lambda x: x[1])  # 按照可信度排序
        self.k += (m[0][0]).upper()  # 取出可信度最高的单个密钥加入密钥
        # for i in range(10):
        #     print(m[i])

    def load(self):
        """
        用于将密钥载入密码机
        @return: 无
        """
        while True:
            try:
                key = input('请输入key以创建密码机（若无key可留空）：')
                break
            except IOError:
                print('请重新输入！')
        self.k = key.upper()

    def clear(self, clear_all=True):
        """
        用于在清理密码机的数据
        @param clear_all: 为True时清除全部数据，为False时清除除密钥外的数据
        @return: 无
        """
        self.k = '' if clear_all else self.k
        self.p = ''
        self.c = ''
        self.alpha_c = ''


def main():
    machine = Vigenere()
    while True:
        mode = input('请选择密码机模式:\n[E]加密Encrypt\t[D]解密Decrypt\t[C]破解Crack\t[R]重置Reset\t[Q]关闭Quit\n')
        if mode in ('E', 'e'):
            try:
                if machine.k == '':
                    machine.load()
                plaintext = input('请输入明文：')
                machine.encrypt(plaintext)
                print(f'密文：{machine.ciphertext}')
            except IOError:
                print("请重新输入！")
        elif mode in ('D', 'd'):
            try:
                if machine.k == '':
                    machine.load()
                ciphertext = input('请输入密文：')
                machine.decrypt(ciphertext)
                print(f'明文：{machine.plaintext}')
            except IOError:
                print("请重新输入！")
        elif mode in ('C', 'c'):
            try:
                ciphertext = input('请输入密文：')
                machine.crack(ciphertext)
                print(f'密码机已获取密钥：{machine.key}')
                print(f"明文：{machine.plaintext}")
                print(f"明文：{' '.join(wordninja.split(''.join(machine.plaintext.split()).lower()))}")
            except IOError:
                print("请重新输入！")
        elif mode in ('R', 'r'):
            machine.clear(True)
        elif mode in ('Q', 'q'):
            print("密码机已关闭")
            break
        else:
            print("请重新输入！")
            continue

    # with open('cipher.txt', 'r') as f:
    #     ciphertext = f.read()
    # # test3 = pythonProject("JANET")
    # test3 = Vigenere()
    # test3.crack(ciphertext)
    # # test3.decrypt(ciphertext)
    # print(test3.key)
    # print(' '.join(wordninja.split(''.join(test3.plaintext.split()).lower())))


if __name__ == '__main__':
    main()
