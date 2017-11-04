"""连接远程服务器执行命令"""
import paramiko
import pexpect
import time

class sshRemote(object):
    """构造函数"""
    def __init__(self,cmdOne,host,port,username,password):
        self.cmdOne=cmdOne
        self.host=host
        self.port=port
        self.username=username
        self.password=password

    """SSHClient()方法连接远程服务器执行命令"""
    def sshLink(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        stdin,stdout,stderr = ssh.exec_command(self.cmdOne)
        result = stdout.read()
        print(str(result,encoding='utf-8'))
        ssh.close()

    """transport方法登陆执行远程命令"""
    def sshLinkTranprot(linkIP,linkPort,linkUsername,linkPassword):
        transport = paramiko.Transport((linkIP,linkPort))
        transport.connect(username=linkUsername,password=linkPassword)
        ssh=paramiko.SSHClient()
        ssh._transport=transport
        stdin,stdout,stderr = ssh.exec_command('ls')
        print(str(stdout.read(),encoding='utf-8'))
        transport.close()

    """交互登陆执行命令"""
    def exp183(self):
        proc = pexpect.spawn("ssh%s@%s" % str(self.username),str(self.host))
        index = proc.expect(["。*password.*",".*yes.*"])
        if index > 0:
            proc.sendline("yes")
            proc.sendline(".*password.*")
        proc.sendline(self.password)



link183=sshRemote('cd /usr/local/nginx/;pwd','192.168.1.152',22,'root','sls123')
link183.sshLink()
link183=link183=sshRemote('ls','192.168.1.152',22,'root','sls123')
link183.sshLink()
"""
link183=link183=sshRemote('source /etc/profile','192.168.1.152',22,'root','sls123')
link183.sshLink()
"""
link183=link183=sshRemote('ifconfig','192.168.1.152',22,'root','sls123')
link183.sshLink()








