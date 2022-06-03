from hash.md5 import MD5
from publickey_cipher.rsa import RSA
import libnum


def sign(m, d, n):
    """
    对消息m进行签名
    @param m: 消息m
    @param d: 签名使用的私钥d
    @param n: 签名使用的模数，公钥n
    @return: 消息m的签名
    """
    machine = MD5()
    d = int(d)
    n = int(n)
    # 先用md5产生消息的摘要
    digest = machine.hash(m)
    # 转为10进制
    digest = libnum.s2n(digest)
    # 对摘要进行签名
    s = pow(digest, d, n)
    return hex(s)[2:]


def check(m, s, e, n):
    """
    对签名进行验证
    @param m: 消息
    @param s: 消息的的签名
    @param e: 公钥e
    @param n: 公钥n
    @return: 是否通过验证
    """
    machine = MD5()
    s = int(s, 16)
    e = int(e)
    n = int(n)
    # 先用md5产生消息的摘要
    digest = machine.hash(m)
    # 转为10进制
    digest = libnum.s2n(digest)
    # 用公钥对进行验证
    temp = pow(s, e, n)
    if digest == temp:
        return True
    else:
        return False


def main():
    while True:
        machine = RSA()
        try:
            print("Alice:")
            message = input("请输入您要签名的消息:\n")
            print("请等待...")
            # 生成密钥(这里使用1024位素数)
            e, n, d = machine.get_keys(1024)
            s = sign(message, int(d), int(n))
            print("你的消息为:\n" + str(message))
            print("对应的签名为:\n" + str(s))
            print("Bob:")
            signature = input("请输入您所得到签名:\n")
            message = input("请输入与之对应的消息:\n")
            if check(message, signature, int(e), int(n)):
                print("验证成功!\n")
            else:
                print("验证失败!\n")
        except ValueError:
            print("请重试！")


if __name__ == '__main__':
    main()
