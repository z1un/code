# _*_  coding:utf-8 _*_
import socket
import sys
PASSWORD_DIC=['redis','root','oracle','password','p@aaw0rd','abc123!','123456','admin']
def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "redis_version" in result:
            return u"未授权访问"
        elif "Authentication" in result:
            for pass_ in PASSWORD_DIC:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("AUTH %s\r\n" %(pass_))
                result = s.recv(1024)
                if '+OK' in result:
                    return u"存在弱口令，密码：%s" % (pass_)
    except Exception, e:
        pass
if __name__ == '__main__':
    ip=sys.argv[1]
    port=sys.argv[2]
    print check(ip,port, timeout=10)