import paramiko
import pexpect
import time
import os
import io

class sshRemote(object):
    """构造函数"""
    def __init__(self, host, port, username, password):
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
        result=str(result,encoding='utf-8')
        return result
        ssh.close()

if __name__ == '__main__':
    userInput = True
    while(userInput!= False):
        ssh152 = sshRemote('IP', 22, 'www', '')
        PicSize = ssh152.sshLink('du -sb --max-depth=0 | awk \'{ print $1 }\'')
        PicSize = int(PicSize)
        print(PicSize)
        listPicSize = []
        listPicSize.append(PicSize)
        print(listPicSize)
        print(time.strftime('%H%M%S'))
        localDate=time.strftime('%H%M%S')
        if(localDate==235959):
            userInput=False
        else:
            pass
        #time.sleep(3600)

    """
        监控一下短信量、图片上传。
        一天均值波动，7天均值波动 大于摸个比例提示，再大报警
        最好小时总量和前一天对比
    """

