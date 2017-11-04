"""连接远程服务器执行命令"""
import paramiko
import pexpect
import time

class sshRemote(object):
    """构造函数"""
   # def __init__(self,cmdOne,host,port,username,password):
    def __init__(self, host, port, username, password):
        #print("请根据顺序输入：1、执行的命令、2、IP、3、端口、4、用户名、5、密码")
        #self.cmdOne=cmdOne
        self.host=host
        self.port=port
        self.username=username
        self.password=password

    """SSHClient()方法连接远程服务器执行命令"""
    def sshLink(self,cmdOne):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        stdin,stdout,stderr = ssh.exec_command(cmdOne)
        result = stdout.read()
        print(str(result,encoding='utf-8'))
        ssh.close()

ssh152=sshRemote('192.168.1.152',22,'sls','')
ssh152.sshLink('ls')