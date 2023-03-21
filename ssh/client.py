import paramiko
import time

def ssh_client():
    ip = input("请输入IP地址：")
    port = 22
    username = input("请输入用户名：")
    password = input("请输入密码：")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    channel = ssh.invoke_shell()
    while True:
        command = input(f"{username}]# ")
        if command == "exit":
            break
        channel.send(command + "\n")
        time.sleep(0.5)  # 等待返回结果
        while channel.recv_ready():
            output = channel.recv(1024)
            print(output.decode('utf-8', 'ignore'))
    ssh.close()

if __name__ == '__main__':
    ssh_client()
