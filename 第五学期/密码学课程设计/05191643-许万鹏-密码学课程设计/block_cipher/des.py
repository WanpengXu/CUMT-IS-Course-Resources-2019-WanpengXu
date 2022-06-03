import re
import base64
from enum import Enum

# class Mode(Enum):
#     ECB = 1
#     CBC = 2
#     CFB = 3
#     OFB = 4
#     CTR = 5


Mode = Enum('Mode', 'ECB CBC CFB OFB CTR')


class DES(object):
    def __init__(self, key=''):
        self.c = ''
        self.p = ''
        self.k = key
        # self.n = num
        # 密钥pc1置换
        self._pc1 = (
            57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4
        )
        # 每轮循环左移位数
        self._left_shift = (
            1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
        )
        # 密钥pc2置换
        self._pc2 = (
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32
        )
        # 初始置换IP
        self._ip = (
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
        )
        # 扩展变换
        self._e_box = (
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        )
        # S 盒
        self._s_box = [
            # S1
            [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
            # S2
            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
            # S3
            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
            # S4
            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
            # S5
            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
            # S6
            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
            # S7
            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
            # S8
            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        ]
        # P-盒置换
        self._p_box = (
            16, 7, 20, 21,
            29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25
        )
        # 末尾IP逆置换
        self._inverse_ip = (
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
        )

    # 字符串转2进制
    @staticmethod
    def str2bin(text):
        res = ''
        for i in text:
            tmp = bin(ord(i))[2:].zfill(8)
            res += tmp
        return res

    # 2进制转字符串
    @staticmethod
    def bin2str(bin_text):
        res = ""
        tmp = re.findall(r'.{8}', bin_text)
        for i in tmp:
            res += chr(int(i, 2))
        return res

    # 字符串转16进制
    @staticmethod
    def str2hex(text):
        res = ''
        for ch in text:
            tmp = hex(ord(ch))[2:].zfill(2)
            res += tmp
        return res

    # 16进制转字符串
    @staticmethod
    def hex2str(hex_text):
        res = ''
        tmp = re.findall(r'.{2}', hex_text)
        for i in tmp:
            res += chr(int('0x' + i, 16))
        return res

    @staticmethod
    def key_process(key):
        if len(key) < 64:
            key += '0' * (64 - len(key))
        elif len(key) > 64:
            key = key[:64]
        return key

    @staticmethod
    def message_process(message, base):
        if len(message) % base != 0:
            message += '0' * (64 - (len(message) % 64))
        return message

    @staticmethod
    def rol(x, s):
        return x[s:] + x[:s]

    @staticmethod
    def xor(r, k):
        new_r = ''
        for i in range(len(r)):
            new_r += str(int(r[i]) ^ int(k[i]))
        return new_r

    def pc_1(self, key):
        res = ''
        for i in self._pc1:  # 1起
            res += key[i - 1]  # 0起
        return res

    def pc_2(self, key):
        res = ''
        for i in self._pc2:
            res += key[i - 1]
        return res

    def get_key(self, key):
        key_list = []
        pc1_output = self.pc_1(key)
        c = pc1_output[:28]
        d = pc1_output[28:]
        for i in self._left_shift:
            c = self.rol(c, i)
            d = self.rol(d, i)
            k_i = self.pc_2(c + d)
            key_list.append(k_i)
        return key_list

    def ip(self, message):
        res = ''
        for i in self._ip:
            res += message[i - 1]
        return res

    def ip_inverse(self, message):
        res = ''
        for i in self._inverse_ip:
            res += message[i - 1]
        return res

    def e_box(self, r):
        new_r = ''
        for i in self._e_box:
            new_r += r[i - 1]
        return new_r

    def s_box(self, r):
        new_r = ''
        box_index = 0
        for i in range(0, len(r), 6):
            block = r[i:i + 6]
            row = int(block[0] + block[5], 2)
            col = int(block[1] + block[2] + block[3] + block[4], 2)
            # col = int(sum(block[1:4 + 1]), 2)
            out = bin(self._s_box[box_index][row][col])[2:].zfill(4)
            # if len(out) != 4:
            #     out = '0' * (4 - len(out)) + out
            new_r += out
            box_index += 1
        return new_r

    def p_box(self, r):
        new_r = ''
        for i in self._p_box:
            new_r += r[i - 1]
        return new_r

    def func_f(self, r, k):
        e_out = self.e_box(r)
        xor_out = self.xor(e_out, k)
        s_out = self.s_box(xor_out)
        p_out = self.p_box(s_out)
        return p_out

    def encrypt(self, message, key):
        """
        DES中每组的加密算法
        @param message: 64位明文
        @param key: 密钥
        @return: 64位密文
        """
        self.message_process(message, 64)
        key = self.key_process(key)
        key_list = self.get_key(key)
        ip_out = self.ip(message)
        l_part = ip_out[:32]
        r_part = ip_out[32:]
        for i in range(15):
            l_part, r_part = r_part, self.xor(l_part, self.func_f(r_part, key_list[i]))
        l_16, r_16 = self.xor(l_part, self.func_f(r_part, key_list[15])), r_part
        cipher = self.ip_inverse(l_16 + r_16)
        return cipher

    # Feistel网络的优点在于加解密相似性，这里可以简化掉
    def decrypt(self, cipher, key):
        """
        DES中每组的解密算法
        @param cipher: 64位密文
        @param key: 密钥
        @return: 64位明文
        """
        key = self.key_process(key)
        key_list_inverse = self.get_key(key)[::-1]
        ip_out = self.ip(cipher)
        l_part = ip_out[:32]
        r_part = ip_out[32:]
        for i in range(15):
            l_part, r_part = r_part, self.xor(l_part, self.func_f(r_part, key_list_inverse[i]))
        l_16, r_16 = self.xor(l_part, self.func_f(r_part, key_list_inverse[15])), r_part
        message = self.ip_inverse(l_16 + r_16)
        return message.strip('\x00')

    def ecb_encrypt(self, message, key, output_mode='h'):
        """
        使用电子密码本(ECB)模式进行DES加密,即使用相同的密钥分别对明文分组独立加密
        @param message: 明文(字符串)
        @param key: 密钥(字符串)
        @param output_mode: 密文输出方式
        @return: 密文
        """
        # 转换为2进制,并补全到64位的倍数
        message_bin = self.message_process(self.str2bin(message), 64)
        # 将密钥转为2进制
        key_bin = self.str2bin(key)
        # 将明文分组
        message_list = re.findall(r'.{64}', message_bin)

        cipher_bin = ''
        for m_i in message_list:
            cipher_bin += self.encrypt(m_i, key_bin)

        cipher = ''
        if output_mode in ('H', 'h'):
            cipher = self.str2hex(self.bin2str(cipher_bin))
        elif output_mode in ('B', 'b'):
            cipher = base64.b64encode(self.bin2str(cipher_bin).encode('latin')).decode('latin')
        return cipher

    def ecb_decrypt(self, cipher, key, input_mode='b'):
        """
        对使用电子密码本(ECB)模式的DES进行解密
        @param cipher: 密文(base64/hex)
        @param key: 密钥(字符串)
        @param input_mode: 密文输入方式
        @return: 明文(字符串)
        """
        cipher_bin = ''
        if input_mode in ('h', 'H'):
            cipher_bin = self.str2bin(self.hex2str(cipher))
        elif input_mode in ('b', 'B'):
            cipher_bin = self.str2bin(base64.b64decode(cipher).decode('latin'))
        # 将密钥转为2进制
        key_bin = self.str2bin(key)
        # 将密文分组
        cipher_list = re.findall(r'.{64}', cipher_bin)

        message_bin = ''
        for c_i in cipher_list:
            message_bin += self.decrypt(c_i, key_bin)

        # 明文2进制转字符串
        message = self.bin2str(message_bin).strip("\x00")
        return message

    def cbc_encrypt(self, message, key, iv, output_mode='h'):
        """
        使用密码分组链接(CBC)模式进行加密,它将前一个分组的加密结果反馈到当前分组的加密中
                M1       M2       M3
               |         |       |
          IV—>xor   ——>xor   ——>xor
               |   |     |  |    |
         key—>enc——|—— enc——|—— enc
               |   |     |  |    |
               C1——     C2——    C3
        @param message: 明文(字符串)
        @param key: 密钥(字符串)
        @param iv: 初始向量(字符串)
        @param output_mode: 输出方式
        @return: 密文
        """
        # 将密钥转为2进制
        key_bin = self.str2bin(key)
        # iv处理方式与key相同(少于8字节补0,大于8字节截断)
        iv_bin = self.key_process(self.str2bin(iv))
        # 将明文进行预处理
        message_bin = self.message_process(self.str2bin(message), 64)
        # 将明文分组
        message_list = re.findall(r'.{64}', message_bin)
        # 第一组的反馈即为iv

        reg = iv_bin
        cipher_bin = ''
        for m_i in message_list:
            # 与反馈进行异或
            encrypt_m_i = self.xor(reg, m_i)
            reg = self.encrypt(encrypt_m_i, key_bin)
            # 链接密文分组
            cipher_bin += reg

        cipher = ''
        if output_mode in ('H', 'h'):
            cipher = self.str2hex(self.bin2str(cipher_bin))
        elif output_mode in ('B', 'b'):
            cipher = base64.b64encode(self.bin2str(cipher_bin).encode('latin')).decode('latin')
        return cipher

    def cbc_decrypt(self, cipher, key, iv, input_mode='b'):
        """
        对使用密码分组链接(CBC)模式的DES进行解密
               C1——     C2——     C3
               |   |    |   |    |
         key—>dec——|—— dec——|—— dec
               |   |    |   |    |
          iv—>xor   ——>xor   ——>xor
               |        |        |
               M1       M2       M3
        @param cipher: 密文
        @param key: 密钥
        @param iv: 初始向量
        @param input_mode: 输出方式
        @return: 密文
        """
        # 将密钥转为2进制
        key_bin = self.str2bin(key)
        # 对iv进行处理
        iv_bin = self.key_process(self.str2bin(iv))
        # 密文转2进制
        cipher_bin = ''
        if input_mode in ('h', 'H'):
            cipher_bin = self.str2bin(self.hex2str(cipher))
        elif input_mode in ('b', 'B'):
            cipher_bin = self.str2bin(base64.b64decode(cipher).decode('latin'))
        # 对密文进行分组
        cipher_list = re.findall(r'.{64}', cipher_bin)

        reg = iv_bin
        message_bin = ''
        for c_i in cipher_list:
            decrypt_c_i = self.decrypt(c_i, key_bin)
            m = self.xor(reg, decrypt_c_i)
            message_bin += m
            # 保存当前密文分组,用于下一个分组的解密异或
            reg = c_i

        # 明文转换为字符串
        message = self.bin2str(message_bin).strip("\x00")
        return message

    def cfb_encrypt(self, message, key, iv, output_mode='h'):
        """
        密文反馈模式(CFB): 这里选择传输单元为8位(即8位一个分组),移位寄存器64位,只需要用到des加密算法。
        先在寄存器中填充IV(64位),然后对寄存器中内容进行加密,加密结果取出前8位与明文分组(8位)异或得到一个密文分组,
        然后寄存器左移8位后,将前一个密文分组(8位)填充在寄存器最后
        @param message: 明文(字符串)
        @param key: 密钥(字符串)
        @param iv: 初始向量(字符串)
        @param output_mode: 密文输出方式(base64/hex)
        @return: 密文
        """
        # 对参数进行预处理
        key_bin = self.str2bin(key)
        iv_bin = self.key_process(self.str2bin(iv))
        message_bin = self.message_process(self.str2bin(message), 8)
        # 对明文进行分组(8位一组)
        message_list = re.findall(r'.{8}', message_bin)
        cipher_bin = ''
        # 初始化移位寄存器
        reg = iv_bin
        for i in message_list:
            # 对寄存器64位进行加密
            enc_out = self.encrypt(reg, key_bin)
            # 选择加密结果的前8位与明文分组异或
            c = self.xor(i, enc_out[:8])
            # 寄存器左移8位,并在最右边填充前一密文分组
            reg = reg[8:] + c
            # 连接密文分组
            cipher_bin += c
        cipher = ''
        if output_mode in ('H', 'h'):
            cipher = self.str2hex(self.bin2str(cipher_bin))
        elif output_mode in ('B', 'b'):
            cipher = base64.b64encode(self.bin2str(cipher_bin).encode('latin')).decode('latin')
        return cipher

    def cfb_decrypt(self, cipher, key, iv, input_mode='b'):
        """
        对DES-CFB进行解密: 先在寄存器中填充IV(64位),然后对寄存器中内容进行加密,加密结果取出前8位与密文分组(8位)异或得到一个明文分组,
        然后将移位寄存器左移8位,用前一密文分组(8位)填充再最右边
        @param cipher: 密文(base64/hex)
        @param key: 密钥(字符串)
        @param iv: 初始向量(字符串)
        @param input_mode: 密文输入方式
        @return: 明文
        """
        # 参数预处理
        key_bin = self.str2bin(key)
        iv_bin = self.key_process(self.str2bin(iv))
        cipher_bin = ''
        if input_mode in ('h', 'H'):
            cipher_bin = self.str2bin(self.hex2str(cipher))
        elif input_mode in ('b', 'B'):
            cipher_bin = self.str2bin(base64.b64decode(cipher).decode('latin'))
        # 对密文进行分组(8位一组)
        cipher_list = re.findall(r'.{8}', cipher_bin)
        message_bin = ''
        # 初始化移位寄存器
        reg = iv_bin
        for c_i in cipher_list:
            # 对移位寄存器进行加密
            enc_out = self.encrypt(reg, key_bin)
            # 选择加密结果的前8位与密文分组异或
            m_i = self.xor(c_i, enc_out[:8])
            # 寄存器左移8位,并在最右边填充前一密文分组
            reg = reg[8:] + c_i
            # 连接明文分组
            message_bin += m_i
        # 明文转换为字符串
        message = self.bin2str(message_bin).strip("\x00")
        return message

    def ofb_encrypt(self, message, key, iv, output_mode='h'):
        """
        输出反馈模式(OFB): 与CFB类似,不过这里把将加密算法的输出的前8位反馈到移位寄存器,而不是前一个密文分组
        @param message: 明文(字符串)
        @param key: 密钥(字符串)
        @param iv: 初始向量(字符串)
        @param output_mode: 密文输出方式(base64/hex)
        @return: 密文
        """
        # 对参数进行预处理
        key_bin = self.str2bin(key)
        iv_bin = self.key_process(self.str2bin(iv))
        message_bin = self.message_process(self.str2bin(message), 8)
        # 对明文进行分组(8位一组)
        message_list = re.findall(r'.{8}', message_bin)
        cipher_bin = ''
        # 初始化移位寄存器
        reg = iv_bin
        for m_i in message_list:
            # 对寄存器64位进行加密
            enc_out = self.encrypt(reg, key_bin)
            # 选择加密结果的前8位与明文分组异或
            c_i = self.xor(m_i, enc_out[:8])
            # 寄存器左移8位,并在最右边填充加密结果的前8位
            reg = reg[8:] + enc_out[:8]
            # 连接密文分组
            cipher_bin += c_i
        cipher = ''
        if output_mode in ('H', 'h'):
            cipher = self.str2hex(self.bin2str(cipher_bin))
        elif output_mode in ('B', 'b'):
            cipher = base64.b64encode(self.bin2str(cipher_bin).encode('latin')).decode('latin')
        return cipher

    def ofb_decrypt(self, cipher, key, iv, input_mode='b'):
        """
        对DES-CFB进行解密:
        @param cipher: 密文(base64/hex)
        @param key: 密钥(字符串)
        @param iv: 初始向量(字符串)
        @param input_mode: 密文输入方式
        @return: 明文
        """
        # 参数预处理
        key_bin = self.str2bin(key)
        iv_bin = self.key_process(self.str2bin(iv))
        cipher_bin = ''
        if input_mode in ('h', 'H'):
            cipher_bin = self.str2bin(self.hex2str(cipher))
        elif input_mode in ('b', 'B'):
            cipher_bin = self.str2bin(base64.b64decode(cipher).decode('latin'))
        # 对密文进行分组(8位一组)
        cipher_list = re.findall(r'.{8}', cipher_bin)
        message_bin = ''
        # 初始化移位寄存器
        reg = iv_bin
        for i in cipher_list:
            # 对移位寄存器进行加密
            enc_out = self.encrypt(reg, key_bin)
            # 选择加密结果的前8位与密文分组异或
            m = self.xor(i, enc_out[:8])
            # 寄存器左移8位,并在最右边填充加密结果的前8位
            reg = reg[8:] + enc_out[:8]
            # 连接明文分组
            message_bin += m
        # 明文转换为字符串
        message = self.bin2str(message_bin).strip("\x00")
        return message

    def ctr_encrypt(self, message, key, nonce, output_mode='h'):
        """
        计数器模式(CTR): 使用与明文分组长度相同(这里选择64位为一组)的计数器,对计数器进行加密,得到的结果与明文分组进行异或,可以并行化的加解密
        初始计数器值是一个随机数,后一个计数器值是前一个计数器值加1
        @param message: 明文(字符串)
        @param key: 密钥(字符串)
        @param nonce: 初始化计数器值的随机数
        @param output_mode: 密文输出方式(base64/hex)
        @return: 密文
        """
        # 参数预处理
        key_bin = self.str2bin(key)
        nonce_bin = self.key_process(self.str2bin(nonce))
        message_bin = self.message_process(self.str2bin(message), 64)
        # 明文分组
        message_list = re.findall(r'.{64}', message_bin)
        cipher_bin = ''
        # 初始化计数器
        counter = nonce_bin  # 一直是二进制字符串
        for m_i in message_list:
            enc_out = self.encrypt(counter, key_bin)
            cipher_bin += self.xor(m_i, enc_out)
            # 计数器加0b1(mod 2^64)
            counter = bin(eval(f'0b{counter} + 0b1 % pow(2, 64)'))[2:].zfill(64)
        cipher = ''
        if output_mode in ('H', 'h'):
            cipher = self.str2hex(self.bin2str(cipher_bin))
        elif output_mode in ('B', 'b'):
            cipher = base64.b64encode(self.bin2str(cipher_bin).encode('latin')).decode('latin')
        return cipher

    def ctr_decrypt(self, cipher, key, nonce, input_mode='b'):
        """
        对DES-CTR进行解密
        @param cipher: 密文
        @param key: 密钥
        @param nonce: 初始化计数器值的随机数
        @param input_mode: 密文输入方式(base64/hex)
        @return: 明文
        """
        # 参数预处理
        key_bin = self.str2bin(key)
        nonce_bin = self.key_process(self.str2bin(nonce))
        cipher_bin = ''
        if input_mode in ('h', 'H'):
            cipher_bin = self.str2bin(self.hex2str(cipher))
        elif input_mode in ('b', 'B'):
            cipher_bin = self.str2bin(base64.b64decode(cipher).decode('latin'))
        # 对密文进行分组(8位一组)
        cipher_list = re.findall(r'.{64}', cipher_bin)
        message_bin = ''
        # 初始化计数器
        counter = nonce_bin
        for c_i in cipher_list:
            enc_out = self.encrypt(counter, key_bin)
            message_bin += self.xor(c_i, enc_out)
            # 计数器加1(mod 2^64)
            counter = bin(eval(f'0b{counter} + 0b1 % pow(2, 64)'))[2:].zfill(64)
        # 明文转换为字符串
        message = self.bin2str(message_bin).strip("\x00")
        return message


def main():
    machine = DES()
    while True:
        mode = input("\nPlease choose a mode:\n[E]Encrypt\t[D]Decrypt\t[Q]Quit\n")
        if mode in ('E', 'e'):
            message = input("Please input the message:\n")
            key = input("Please input the key:\n")
            while True:
                try:
                    work_mode = int(input("Please choose a working mode:\n[1]ECB\t[2]CBC\t[3]CFB\t[4]OFB\t[5]CTR\n"))
                except ValueError:
                    print("Please input again!")
                    continue
                match work_mode:
                    # ECB加密模式
                    case Mode.ECB.value:
                        output_way = input("Please choose the output way:\n[B]Base64\t[H]Hex\n")
                        cipher = machine.ecb_encrypt(message, key, output_way)
                        print("The cipher is:\n" + cipher)
                    # CBC加密模式
                    case Mode.CBC.value:
                        iv = input("Please input the IV:\n")
                        output_way = input("Please choose the output way:\n[B]Base64\t[H]Hex\n")
                        cipher = machine.cbc_encrypt(message, key, iv, output_way)
                        print("The cipher is:\n" + cipher)
                    # CFB加密模式 加密不一样但解密一样？？
                    case Mode.CFB.value:
                        iv = input("Please input the IV:\n")
                        output_way = input("Please choose the output way:\n[B]Base64\t[H]Hex\n")
                        cipher = machine.cfb_encrypt(message, key, iv, output_way)
                        print("The cipher is:\n" + cipher)
                    # OFB加密模式  这个也是？？
                    case Mode.OFB.value:
                        iv = input("Please input the IV:\n")
                        output_way = input("Please choose the output way:\n[B]Base64\t[H]Hex\n")
                        cipher = machine.ofb_encrypt(message, key, iv, output_way)
                        print("The cipher is:\n" + cipher)
                    # CTR加密模式
                    case Mode.CTR.value:
                        nonce = input("Please input the nonce:\n")
                        output_way = input("Please choose the output way:\n[B]Base64\t[H]Hex\n")
                        cipher = machine.ctr_encrypt(message, key, nonce, output_way)
                        print("The cipher is:\n" + cipher)
                    case _:
                        print("Please input again!")
                        continue
                break
        elif mode in ('D', 'd'):
            cipher = input("Please input the cipher:\n")
            key = input("Please input the key:\n")
            while True:
                try:
                    work_mode = int(input("Please choose a working mode:\n[1]ECB\t[2]CBC\t[3]CFB\t[4]OFB\t[5]CTR\n"))
                except ValueError:
                    print("Please input again!")
                    continue
                match work_mode:
                    # ECB解密模式
                    case Mode.ECB.value:
                        input_way = input("Please choose your input way:\n[B]Base64\t[H]Hex\n")
                        message = machine.ecb_decrypt(cipher, key, input_way)
                        print("The message is:\n" + message)
                    # CBC解密模式
                    case Mode.CBC.value:
                        iv = input("Please input the IV:\n")
                        input_way = input("Please choose your input way:\n[B]Base64\t[H]Hex\n")
                        message = machine.cbc_decrypt(cipher, key, iv, input_way)
                        print("The message is:\n" + message)
                    # CFB解密模式
                    case Mode.CFB.value:
                        iv = input("Please input the IV:\n")
                        input_way = input("Please choose your input way:\n[B]Base64\t[H]Hex\n")
                        message = machine.cfb_decrypt(cipher, key, iv, input_way)
                        print("The message is:\n" + message)
                    # CFB解密模式
                    case Mode.OFB.value:
                        iv = input("Please input the IV:\n")
                        input_way = input("Please choose your input way:\n[B]Base64\t[H]Hex\n")
                        message = machine.ofb_decrypt(cipher, key, iv, input_way)
                        print("The message is:\n" + message)
                    # CTR解密模式
                    case Mode.CTR.value:
                        nonce = input("Please input the nonce:\n")
                        input_way = input("Please choose your input way:\n[B]Base64\t[H]Hex\n")
                        message = machine.ctr_decrypt(cipher, key, nonce, input_way)
                        print("The message is:\n" + message)
                    case _:
                        print("Please input again!")
                        continue
                break
        elif mode in ('Q', 'q'):
            break
        else:
            continue


if __name__ == '__main__':
    main()
