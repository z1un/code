import binascii
import codecs
from pyDes import *


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


if __name__ == "__main__":
    passwd = sys.argv[1]
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
