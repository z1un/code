# base64编码、解码
# Author: zjun
# Github: bestreder
# Data: 2020.02.29

import base64
from base64 import decode, encode


def encode():
    a = input('请输入明文: ')
    a = str(base64.b64encode(a.encode("utf-8")), "utf-8")
    print(a)


def decode():
    try:
        a = input('请输入密文: ')
        a = a + '=='
        a = str(base64.b64decode(a), "utf-8")
        print(a)
    except:
        print('无法识别密文')


def main():
    print('base64')
    print('1. 加密')
    print('2. 解密')
    a = input('请选择: ')
    if a == '1':
        encode()
    elif a == '2':
        decode()
    else:
        pass


main()
