"""
本程序实现两部分内容：
1.实现RSA加密通信双方公私钥生成，并实现发起方Alice使用接收方Bob公钥加密发送数据，Bob接收后使用自身私钥解密数据
2.实现对Bob身份的验证，Bob使用自身私钥进行签名，Alice收到后使用Bob公钥进行解密验签
"""
import os
import string
import base64
import random
import shutil
from hash.md5 import MD5
from block_cipher.des import DES

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

chars = string.ascii_letters + string.digits

BUFFSIZE = 1024


def get_des_param():
    """
    产生64位随机的key和IV
    @return: des密钥和cbc的初始向量iv
    """
    while True:
        key = ''.join(random.sample(chars, 8))
        iv = ''.join(random.sample(chars, 8))
        if key != iv:
            break
    return key, iv


def transfer_encrypt(message):
    """
    对分组传输的每一个分组进行des_cbc加密,且每次使用不同的key和iv
    @param message: 被加密的分组
    @return: key,iv,cipher
    """
    des_key, iv = get_des_param()
    des_cipher = DES().cbc_encrypt(message, des_key, iv, 'b')
    with open(r'key\bob_public.pem') as f:
        key = f.read()
        pubkey = RSA.importKey(key)  # 将bob_public.pem中的公钥导出
        cipher = Cipher_pkcs1_v1_5.new(pubkey)  # 按照pkcs1_v1_5的标准对公钥进行处理，如填充字段等
        # 对message使用bob的公钥进行加密，加密结果再用base64进行处理生成最终密文
        # 用base64进行处理的原因是为了防止原来的二进制数据某些字符被当做控制指令，或者一些不可见的二进制字符(ascii值在128～255之间的)在路由传输过程中被滤过
        # 使用base64可将所有不可见二进制字符显示
        key_encrypted = base64.b64encode(cipher.encrypt(des_key.encode(encoding="utf-8")))
        iv_encrypted = base64.b64encode(cipher.encrypt(iv.encode(encoding="utf-8")))
    return key_encrypted, iv_encrypted, des_cipher


# 首先生成各自公私钥
"""实现RSA通信双方公私钥生成，并实现使用接收方公钥加密，接收方私钥解密功能"""
random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)
# 生成Alice的公钥和私钥
private_pem = rsa.exportKey()
# print(private_pem)
public_pem = rsa.publickey().exportKey()
with open(r'key\alice_private.pem', 'wb') as f:
    f.write(private_pem)
with open(r'key\alice_public.pem', 'wb') as f:
    f.write(public_pem)

# 生成Bob的公钥和私钥
private_pem = rsa.exportKey()
public_pem = rsa.publickey().exportKey()
with open(r'key\bob_private.pem', 'wb') as f:
    f.write(private_pem)
with open(r'key\bob_public.pem', 'wb') as f:
    f.write(public_pem)


def get_file_md5(filepath):
    """
    对文件内容进行md5产生消息摘要来确保文件传输过程中的完整性
    :param filepath: 文件路径
    :return: 文件摘要
    """
    with open(filepath, 'rb') as fs:
        digest = MD5().hash(fs.read().decode('latin'))
    return digest


filepath = r'Alice\file'
# 确定文件路径
print("Send: " + filepath)

if os.path.isfile(filepath):
    file_size = str(os.path.getsize(filepath))
    # 总共要传输的次数
    count = (int(file_size) // BUFFSIZE) + 1

    # 获得原文件的md5
    file_digest = get_file_md5(filepath)
    send_size = 0
    f1 = open(filepath, 'rb')
    print("Start transferring...")
    i = 0
    shutil.rmtree('Bob')
    os.mkdir('Bob')
    # 循环发送文件
    while count:
        print('=' * 45 + f'round{i}' + '=' * 45 + '\n')
        print('*' * 45 + "Alice->Bob:" + '*' * 45)
        filedata = base64.b64encode(f1.read(BUFFSIZE)).decode()
        key_encrypted, iv_encrypted, allfiles_encrypted = transfer_encrypt(filedata)
        # 发送des-cbc加密后的内容(16进制)
        print(f'encrypted_file_part{i} is:')
        print(allfiles_encrypted)
        with open(rf'Bob\file.encry{i}', 'wb') as f:
            f.write(allfiles_encrypted.encode())
        # 发送RSA加密后的key(10进制)
        print('encrypted_des_key is:')
        print(key_encrypted.decode())
        # 发送RSA加密后的iv
        print('encrypted_des_iv is:')
        print(iv_encrypted.decode())
        # time.sleep(0.2)
        # 计算已发送的大小
        send_size += BUFFSIZE
        if send_size > int(file_size):
            send_size = file_size
        count -= 1
        i += 1
        print('*' * 100 + '\n')
        # print("Bob:")
        print('*' * 45 + "Bob->Alice" + '*' * 45)
        """对Bob身份进行验证，Bob用自己的私钥进行签名，Alice收到签名后，用Bob公钥进行解密验签"""
        # 签名
        with open(r'key\bob_private.pem') as f:
            key = f.read()
            signkey = RSA.importKey(key)
            signer = Signature_pkcs1_v1_5.new(signkey)  # 按照pkcs1_v1_5的标准对私钥进行处理，用于签名计算，将处理后的私钥存入signer变量
            digest = SHA.new()
            digest.update(allfiles_encrypted.encode("utf8"))  # 对message用SHA进行散列计算，得到摘要，防止篡改
            sign = signer.sign(digest)  # 对摘要用私钥进行处理
            signature = base64.b64encode(sign)
            print('signature is:')
            print(signature)
        print('*' * 100 + '\n')
        print('*' * 45 + "Alice" + '*' * 45)
        # 验签
        with open(r'key\bob_public.pem') as f:
            key = f.read()
            unsignkey = RSA.importKey(key)
            unsigner = Signature_pkcs1_v1_5.new(unsignkey)  # 按照pkcs1_v1_5的标准对公钥进行处理，用于签名解密，将处理后的公钥存入unsigner变量
            digest = SHA.new()
            digest.update(allfiles_encrypted.encode("utf8"))
            is_verify = unsigner.verify(digest,
                                        base64.b64decode(signature))  # 将签名数据用unsigner进行解密，然后与原文digest的摘要进行比较是否一致
            print('verify result is:', is_verify)
        print('*' * 100 + '\n')
    print("Get the file Successfully.")
    f.close()
    print('*' * 45 + "Alice->Bob" + '*' * 45)
    # 发送md5
    print("file's md5:")
    print(file_digest.encode())
    print('*' * 100 + '\n')
else:
    print("[Error]: Can't find the file")

# print("Bob:")
# Bob收到密文后使用自己的私钥进行解密
# with open(r'key\bob_private.pem') as f:
#     key = f.read()
#     prikey = RSA.importKey(key)
#     cipher = Cipher_pkcs1_v1_5.new(prikey)
#     plain_text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
#     plain_text = plain_text.decode()
#     # 输出明文
#     print('plain text is:')
#     print(plain_text)
