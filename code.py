import base64
from urllib.parse import quote, unquote
import binascii
import codecs
from pyDes import *
import os


def base64encode():
    a = input('请输入明文: ')
    a = str(base64.b64encode(a.encode("utf-8")), "utf-8")
    print(a)


def base64decode():
    try:
        a = input('请输入密文: ')
        a = a + '=='
        a = str(base64.b64decode(a), "utf-8")
        print(a)
    except:
        print('无法识别密文')


def kaisaencode():
    str_raw = input("请输入明文：")
    k = int(input("请输入位移值："))
    str_change = str_raw.lower()
    str_list = list(str_change)
    str_list_encry = str_list
    i = 0
    while i < len(str_list):
        if ord(str_list[i]) < 123 - k:
            str_list_encry[i] = chr(ord(str_list[i]) + k)
        else:
            str_list_encry[i] = chr(ord(str_list[i]) + k - 26)
        i = i + 1
    print("加密结果为：" + "".join(str_list_encry))


def kaisadecode():
    str_raw = input("请输入密文：")
    k = int(input("请输入位移值："))
    str_change = str_raw.lower()
    str_list = list(str_change)
    str_list_decry = str_list
    i = 0
    while i < len(str_list):
        if ord(str_list[i]) >= 97 + k:
            str_list_decry[i] = chr(ord(str_list[i]) - k)
        else:
            str_list_decry[i] = chr(ord(str_list[i]) + 26 - k)
        i = i + 1
    print("解密结果为：" + "".join(str_list_decry))


def urlencode():
    a = input('请输入: ')
    print(quote(a, 'utf-8'))


def urldecode():
    a = input('请输入: ')
    print(unquote(a, 'utf-8'))


def DesEncrypt(Key, str):
    k = des(str, ECB, pad=None)
    EncryptStr = k.encrypt(Key)
    return binascii.b2a_hex(EncryptStr)


def ZeroPadding(str):
    b = []
    l = len(str)
    num = 0
    for n in range(l):
        if (num < 8) and n % 7 == 0:
            b.append(str[n:n + 7] + '0')
            num = num + 1
    return ''.join(b)


def main():
    print('''选择编码方式：
    1. Base64
    2. 凯撒密码
    3. Url编码
    4. LMhash
    5. NTLMhash
    6. Hex
    7. Unicode
    8. Base32
    9. Base16''')
    a = input('请选择: ')
    if a == '1':
        print('''Base64
    1. 编码
    2. 解码''')
        b = input('请选择: ')
        if b == '1':
            base64encode()
        elif b == '2':
            base64decode()
        else:
            print('您的输入有误！')
    if a == '2':
        print('''凯撒密码
    1. 加密
    2. 解密''')
        b = input('请选择：')
        if b == '1':
            kaisaencode()
        elif b == '2':
            kaisadecode()
        else:
            print('您的输入有误！')
    if a == '3':
        print('''Url解码、编码
    1. 编码
    2. 解码''')
        b = input('请选择: ')
        if b == '1':
            urlencode()
        elif b == '2':
            urldecode()
        else:
            print('您的输入有误！')
    if a == '4':
        passwd = input('''LMhash
    输入带加密字符: ''')
        print('你的输入是:', passwd)
        print('转化为大写:', passwd.upper())

        # 用户的密码转换为大写,并转换为16进制字符串
        passwd = codecs.encode(passwd.upper().encode(), 'hex_codec')
        print('转为hex:', passwd.decode())

        # 密码不足28位，用0在右边补全
        passwd_len = len(passwd)
        if passwd_len < 28:
            passwd = passwd.decode().ljust(28, '0')
        print('补齐28位:', passwd)

        # 28位的密码被分成两个14位部分
        PartOne = passwd[0:14]
        PartTwo = passwd[14:]
        print('两组14位的部分:', PartOne, PartTwo)

        # 每部分分别转换成比特流，并且长度为56位，长度不足用0在左边补齐长度
        PartOne = bin(int(PartOne, 16)).lstrip('0b').rjust(56, '0')
        PartTwo = bin(int(PartTwo, 16)).lstrip('0b').rjust(56, '0')
        print('两组56位比特流:', PartOne, PartTwo)

        # 两组分别再分为7位一组末尾加0，再分别组合成新的字符
        PartOne = ZeroPadding(PartOne)
        PartTwo = ZeroPadding(PartTwo)
        print('两组再7位一组末尾加0:', PartOne, PartTwo)

        # 两组数据转hex
        PartOne = hex(int(PartOne, 2))[2:]
        PartTwo = hex(int(PartTwo, 2))[2:]
        if '0' == PartTwo:
            PartTwo = "0000000000000000"
        print('两组转为hex:', PartOne, PartTwo)

        # 16位的二组数据，分别作为DES key为"KGS!@#$%"进行加密。
        LMOne = DesEncrypt("KGS!@#$%", binascii.a2b_hex(PartOne)).decode()
        LMTwo = DesEncrypt("KGS!@#$%", binascii.a2b_hex(PartTwo)).decode()
        print('两组DES加密结果:', LMOne, LMTwo)

        # 将二组DES加密后的编码拼接，得到LM HASH值。
        LM = LMOne + LMTwo
        print('LM hash:', LM)
    if a == '5':
        passwd = input('''NTLMhash
    输入带加密字符: ''')
        os.system(
            '''python2 -c "import hashlib,binascii; print binascii.hexlify(hashlib.new('md4', '{}'.encode('utf-16le')).digest())"'''.format(
                passwd))
    if a == '6':
        print('''Hex
    1. hex转字符串
    2. 字符串转hex''')
        b = input('请选择: ')
        if b == '1':
            code = input('输入hex: ')
            print(bytes.fromhex(code).decode())
        if b == '2':
            code = input('输入字符串: ')
            print(code.encode().hex())
    if a == '7':
        print('''Unicode
    1. Unicode转中文
    2. 中文转Unicode''')
        b = input('请选择: ')
        if b == '1':
            code = input('请输入Unicode字符: ')
            print(code.encode('utf-8').decode("unicode_escape"))
        if b == '2':
            code = input('请输入中文: ')
            print(code.encode("unicode_escape").decode())
    if a == '8':
        print('''Base32
    1. 编码
    2. 解码''')
        b = input('请选择: ')
        if b == '1':
            code = input('请输入：')
            code = bytes(code, encoding="utf8")
            print(base64.b32encode(code).decode())
        if b == '2':
            code = input('请输入：')
            code = bytes(code, encoding="utf8")
            print(base64.b32decode(code).decode())
    if a == '9':
        print('''Base16
    1. 编码
    2. 解码''')
        b = input('请输入：')
        if b == '1':
            code = input('请输入：')
            code = bytes(code, encoding="utf8")
            print(base64.b16encode(code).decode())
        if b == '2':
            code = input('请输入：')
            code = bytes(code, encoding="utf8")
            print(base64.b16decode(code).decode())


if __name__ == '__main__':
    print('编码解码，一个就够了!\n')
    main()
