# zip爆破
# Author: zjun
# Github: bestreder
# Data: 2020.02.29

import zipfile
from threading import Thread
import argparse

endflag = 1


def extract(file, password):
    try:
        file.extractall(pwd=password.encode('ascii'))
        global endflag
        endflag = 0
        print('[+]Found Password:', password)
    except:
        print('[-]Not Found...', password)
        pass


def main():
    parser = argparse.ArgumentParser(description='The script is baopozip')
    parser.add_argument('-f', '--file', required=True, help='target file')
    parser.add_argument('-p',
                        '--pwdfile',
                        required=True,
                        help='target pwdfile')
    args = parser.parse_args()
    file = args.file
    pwdfile = args.pwdfile
    file = zipfile.ZipFile(file)
    with open(pwdfile, 'r') as f:
        for password in f.readlines():
            if endflag == 0:
                break
            password = password.strip('\n')
            t = Thread(target=extract, args=(file, password))
            t.start()


if __name__ == '__main__':
    main()
