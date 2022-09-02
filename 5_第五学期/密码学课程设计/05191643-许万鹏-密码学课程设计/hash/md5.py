import math
import re


class MD5:
    def __init__(self):
        # 初始链接变量(小端序表示)
        self.IV_A, self.IV_B, self.IV_C, self.IV_D = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)

        # 每轮步函数中循环左移的位数
        self._shift = ((7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22),
                       (5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20),
                       (4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23),
                       (6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21))

        # 每步选择m得索引
        self._M_index = ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                         (1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12),
                         (5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2),
                         (0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9))

    # 非线性函数F、G、H、I
    def F(self, x, y, z):
        return (x & y) | (~x & z)

    def G(self, x, y, z):
        return (x & z) | (y & ~z)

    def H(self, x, y, z):
        return x ^ y ^ z

    def I(self, x, y, z):
        return y ^ (x | (~z))

    # 生成伪随机常数
    def T(self, i):
        return math.floor(pow(2, 32) * abs(math.sin(i)))

    # 二进制的循环左移
    def rol(self, x, s):
        return (x << s) | (x >> 32 - s)

    # 模32加
    def mod_add(self, x, y):
        return (x + y) % pow(2, 32)

    # 字符串转2进制
    def str2bin(self, text):
        res = ''.join([bin(ord(i))[2:].zfill(8) for i in text])
        return res

    # 大端序转小端序(16进制)
    def hex2little(self, x):
        res = re.findall(r'.{2}', x)[::-1]
        res = ''.join(res)
        return res

    # 大端序转小端序(2进制)
    def bin2little(self, x):
        res = re.findall(r'.{8}', x)[::-1]
        res = ''.join(res)
        return res

    # 对消息进行填充
    def message_padding(self, m):
        # 计算附加的64位长度(小端序表示)
        len_padding = self.bin2little(bin(len(m))[2:].zfill(64))
        m += '1'
        while len(m) % 512 != 448:
            m += '0'
        return m + len_padding

    # 压缩函数(对每个512bit分组进行处理)
    def compress_func(self, a, b, c, d, m_i):
        """
        压缩函数函数,对每512bit得分组进行处理,包括4轮,每轮16步
        :param a, b, c, d:  输入链接变量(即前一个分组的输出链接变量)
        :param m_i: 512bit的消息分组
        :return: A,B,C,D 输出链接变量
        """
        # 对每一分组的初始链接变量进行备份
        A, B, C, D = a, b, c, d
        # 将512bit分为16组,每组32bit
        m_list_32 = re.findall(r'.{32}', m_i)
        # 每个分组经过4轮函数
        for round_index in range(4):
            # 每轮有16步
            for step_index in range(16):
                # 对每一步的链接变量进行备份
                AA, BB, CC, DD = A, B, C, D
                # 每一轮选择不同的非线性函数
                match round_index:
                    case 0:
                        func_out = self.F(B, C, D)
                    case 1:
                        func_out = self.G(B, C, D)
                    case 2:
                        func_out = self.H(B, C, D)
                    case 3:
                        func_out = self.I(B, C, D)
                A, C, D = D, B, C
                # B模加非线性函数的输出
                temp = self.mod_add(AA, func_out)
                # 模加消息分组(注意为大端序)
                temp = self.mod_add(temp, int(self.bin2little(m_list_32[self._M_index[round_index][step_index]]), 2))
                # print(type(B))
                # 模加伪随机常数
                temp = self.mod_add(temp, self.T(16 * round_index + step_index + 1))
                # 循环左移s位
                temp = self.rol(temp, self._shift[round_index][step_index])
                # 模加BB
                B = self.mod_add(temp, BB)
            #     print(str(16 * round_index + step_index + 1).zfill(2), end=" ")
            #     print(hex(A).replace("0x", "").replace("L", "").zfill(8), end=" ")
            #     print(hex(B).replace("0x", "").replace("L", "").zfill(8), end=" ")
            #     print(hex(C).replace("0x", "").replace("L", "").zfill(8), end=" ")
            #     print(hex(D).replace("0x", "").replace("L", "").zfill(8))
            # print("*" * 38)
        # 与该分组的初始链接变量异或
        A = self.mod_add(A, a)
        B = self.mod_add(B, b)
        C = self.mod_add(C, c)
        D = self.mod_add(D, d)

        return A, B, C, D

    def hash(self, m):
        # 转为2进制
        m = self.str2bin(m)
        # 消息填充
        m = self.message_padding(m)
        # 对消息分组,每组512位
        m_list_512 = re.findall(r'.{512}', m)
        # 初始链接变量
        A, B, C, D = self.IV_A, self.IV_B, self.IV_C, self.IV_D
        # 对每512bit进行分组处理,前一组的4个输出连接变量作为下一组的4个输入链接变量
        for m_i in m_list_512:
            A, B, C, D = self.compress_func(A, B, C, D, m_i)
        # 把最后一次的分组4个输出连接变量再做一次大端小端转换
        A = self.hex2little(hex(A)[2:]).zfill(8)
        B = self.hex2little(hex(B)[2:]).zfill(8)
        C = self.hex2little(hex(C)[2:]).zfill(8)
        D = self.hex2little(hex(D)[2:]).zfill(8)
        # 拼接到一起的得到最终的md5值
        return f'{A}{B}{C}{D}'


def main():
    machine = MD5()
    while True:
        message = input("请输入要进行md5的内容:\n")
        if len(machine.str2bin(message)) > pow(2, 64):
            print("最多只能处理2^64位！\n")
            continue
        digest = machine.hash(message)
        print("md5后的散列值为:\n" + digest)


if __name__ == '__main__':
    main()
