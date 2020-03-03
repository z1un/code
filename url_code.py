# url解码、编码
# Author: zjun
# Github: bestreder
# Data: 2020.02.29

from urllib.parse import quote, unquote


def urlquote():
    a = input('请输入: ')
    print(quote(a, 'utf-8'))


def urlunquote():
    a = input('请输入: ')
    print(unquote(a, 'utf-8'))


print('url解码、编码')
print('1. url编码')
print('2. url解码')
a = input('请选择: ')
if a == '1':
    urlquote()
elif a == '2':
    urlunquote()
else:
    print('无此选项')
