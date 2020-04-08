# 凯撒密码加解密
# Author: zjun
# Github: bestreder
# Data: 2020.02.29

import os


def encryption():
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


def decryption():
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


while True:
    print(u"1. 加密")
    print(u"2. 解密")
    choice = input("请选择：")
    if choice == "1":
        encryption()
    elif choice == "2":
        decryption()
    else:
        print(u"您的输入有误！")

