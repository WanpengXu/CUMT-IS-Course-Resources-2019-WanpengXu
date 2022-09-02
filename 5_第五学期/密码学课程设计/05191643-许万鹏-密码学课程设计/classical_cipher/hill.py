import numpy as np


class Hill(object):
    def __init__(self, encryption_matrix: np.ndarray = np.array([]), order: int = 0) -> None:
        self.o = order
        self.k = encryption_matrix
        self.k_inv = np.array([])
        self.p = ''
        self.c = ''

    @property
    def key(self) -> np.ndarray:
        return self.k

    @property
    def plaintext(self) -> str:
        return self.p

    @property
    def ciphertext(self) -> str:
        return self.c

    def text2matrix(self, text) -> None:
        text = text.lower()
        blocks = [text[i:i + self.o] for i in range(0, len(text), self.o)]
        blocks[-1] = blocks[-1].ljust(self.o, 'a')
        matrix = np.array([list(map(ord, block)) for block in blocks]) - ord('a')
        return matrix

    def encrypt(self, plaintext: str) -> None:
        """
        希尔密码加密方法
        @param plaintext: 明文
        @return: 无
        """
        self.p = plaintext.lower()
        blocks = [self.p[i:i + self.o] for i in range(0, len(self.p), self.o)]  # 每 阶数个 明文作为一组
        blocks[-1] = blocks[-1].ljust(self.o, 'a')  # 对最后一组进行填充以进行矩阵乘法
        temp = np.array([list(map(ord, block)) for block in blocks]) - ord('a')  # 将每组的字母转换为字母序号
        encrypted_code = (temp @ self.k) % 26 + ord('A')
        decryption_matrix_text = ''.join(map(chr, encrypted_code.ravel()))
        self.c = decryption_matrix_text[:len(self.p)]  # 取出密文，忽略填充字符

    def decrypt(self, ciphertext: str) -> None:
        """
        希尔密码解密方法
        @param ciphertext: 密文
        @return: 无
        """
        self.c = ciphertext.lower()
        self.k_inv = self.solve_mod26_inverse_matrix(self.k)  # 求密钥矩阵的逆矩阵
        blocks = [self.c[i:i + self.o] for i in range(0, len(self.c), self.o)]
        blocks[-1] = blocks[-1].ljust(self.o, 'a')
        temp = np.array([list(map(ord, block)) for block in blocks]) - ord('a')
        encrypted_code = ((temp @ self.k_inv) % 26) + ord('a')
        decryption_matrix_text = ''.join(map(lambda x: chr(int(x)), encrypted_code.ravel()))
        self.p = decryption_matrix_text[:len(self.c)]

    def ex_gcd(self, a, b, arr) -> int:  # 扩展欧几里得
        if b == 0:
            arr[0], arr[1] = 1, 0
            return a
        g = self.ex_gcd(b, a % b, arr)
        arr[0], arr[1] = arr[1], arr[0] - int(a / b) * arr[1]
        return g

    def mod_reverse(self, a, n) -> int:  # ax=1(mod m) 求a模m的乘法逆元x(a^(-1))
        arr = [0, 1]
        gcd = self.ex_gcd(a, n, arr)
        if gcd == 1:
            return (arr[0] % n + n) % n
        else:
            return -1

    def solve_mod26_inverse_matrix(self, matrix) -> None:
        det = int(np.linalg.det(matrix))  # det(p)
        inverse_matrix = np.linalg.inv(matrix)  # p在实数域的逆矩阵
        adjoint_matrix = (inverse_matrix * det)  # p的伴随矩阵=det(p)*p^(-1)
        adjoint_matrix_mod26 = adjoint_matrix % 26  # p的模26伴随矩阵=p的伴随矩阵模26
        modular_multiplicative_inverse = self.mod_reverse(det, 26)  # det(p)^(-1) mod 26
        inverse_matrix = np.around((modular_multiplicative_inverse * adjoint_matrix_mod26)).astype('int') % 26
        return inverse_matrix

    def crack(self, plaintext, ciphertext, order) -> None:
        self.p = plaintext
        self.c = ciphertext
        self.o = order
        p_matrix = self.text2matrix(self.p)[0:self.o:1]  # 切片为方阵以计算行列式
        c_matrix = self.text2matrix(self.c)[0:self.o:1]
        p_inverse_matrix = self.solve_mod26_inverse_matrix(p_matrix)
        self.k = (p_inverse_matrix @ c_matrix) % 26

        det_p = int(np.linalg.det(p_matrix)) % 26
        if (det_p != 0 and self.ex_gcd(det_p, 26, [0, 1]) == 1):  # 可逆检测
            return True
        else:
            return False

    def load(self) -> None:
        while True:
            try:
                n = int(input('请输入key的阶数n以创建密码机：'))
                break
            except ValueError:
                print('请重新输入！')
        self.o = n
        key = []
        if n != 0:
            print('请输入key以创建密码机：')
            for i in range(n):
                key.append([int(i) for i in input().split()])
            self.k = np.array(key)

    def clear(self):
        self.o = 0
        self.k = np.array([])
        self.k_inv = np.array([])
        self.p = ''
        self.c = ''


def main():
    # 加密测试1 2
    # encryption_matrix = np.array([[10, 5, 12, 0, 0],
    #                               [3, 14, 21, 0, 0],
    #                               [8, 9, 11, 0, 0],
    #                               [0, 0, 0, 11, 8],
    #                               [0, 0, 0, 3, 7]])
# 10 5 12 0 0
# 3 14 21 0 0
# 8 9 11 0 0
# 0 0 0 11 8
# 0 0 0 3 7
    # machine = Hill(encryption_matrix)
    # machine.encrypt('cryptologyinformationsets', 5)
    # machine.encrypt('informationsecuritycenter', 5)
    # print(machine.ciphertext)

    # 加密测试3
    # encryption_matrix = np.array([[7, 19], [8, 3]])
    # machine.encrypt('friday', 2)
    # print(machine.ciphertext)

    # 破解密钥1 2
    # machine = Hill()
    # # machine.crack("cryptologyinformationsets", "DWVOTZMHIIDHIXXMXPAGIPGDS", 5)
    # machine.crack("friday", "PQCFKU", 2)
    # print(machine.k)

    # 解密测试1
    # encryption_matrix = np.array([[7, 19], [8, 3]])
    # machine2 = Hill(encryption_matrix)
    # machine2.decrypt("PQCFKU", 2)
    # print(machine2.plaintext)

    machine = Hill()
    while True:
        mode = input('请选择密码机模式：\n[E]加密Encrypt\t[D]解密Decrypt\t[C]破解Crack\t[R]重置Reset\t[Q]关闭Quit\n')
        if mode in ('E', 'e'):
            try:
                if machine.k.size == 0:
                    machine.load()
                plaintext = input('请输入明文：')
                machine.encrypt(plaintext)
                print(f'密文：{machine.ciphertext}')
            except IOError:
                print("请重新输入！")
        elif mode in ('D', 'd'):
            try:
                if machine.k.size == 0:
                    machine.load()
                ciphertext = input('请输入密文：')
                machine.decrypt(ciphertext)
                print(f'明文：{machine.plaintext}')
            except IOError:
                print("请重新输入！")
        elif mode in ('C', 'c'):
            try:
                plaintext = input('请输入明文：')
                ciphertext = input('请输入密文：')
                n = int(input('请输入key的阶数n：'))
                if (machine.crack(plaintext, ciphertext, n)):
                    print(f'密码机已获取密钥：\n{machine.key}')
                else:
                    print(f"明文矩阵不可逆！")
            except IOError:
                print("请重新输入！")
        elif mode in ('R', 'r'):
            machine.clear()
            print("密码机已重置")
        elif mode in ('Q', 'q'):
            print("密码机已关闭")
            break
        else:
            print("请重新输入！")
            continue


if __name__ == '__main__':
    main()
