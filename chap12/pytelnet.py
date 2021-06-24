# AUTHOR : 温幸文
# TIME : 2021/6/23  上午9:51
import logging
import os.path
import telnetlib
import time

'''同时开多个telnet连接，用于快速传输yuv文件'''


class TelnetClient():
    def __init__(self):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self, host_ip, username, password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip, port=23)
        except:
            logging.warning('%s网络连接失败' % host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'login: ', timeout=10)
        self.tn.write(username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password: ', timeout=10)
        self.tn.write(password.encode('ascii') + b'\n')
        # 延时再收取返回结果，给服务端足够响应时间
        time.sleep(0.3)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'Login incorrect' not in command_result:
            logging.warning('%s登录成功' % host_ip)
            return True
        else:
            logging.warning('%s登录失败，用户名或密码错误' % host_ip)
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    # def execute_some_command(self, command):
    #     # 执行命令
    #     self.tn.write(command.encode('ascii') + b'\n')
    #     time.sleep(2)
    #     # 获取命令结果
    #     command_result = self.tn.read_very_eager().decode('ascii')
    #     logging.warning('命令执行结果：\n%s' % command_result)

    # 进入UDISK目录的命令
    def enter_U(self):
        command1 = 'cd ..'
        command2 = 'cd UDISK/'
        # 执行命令
        self.tn.write(command1.encode('ascii') + b'\n')
        time.sleep(0.5)
        self.tn.write(command2.encode('ascii') + b'\n')
        time.sleep(0.5)

    # 获取板端中对应文件的大小
    def get_size(self):
        command = 'll|grep yuv|grep -v Fail'
        # 存放文件大小的字典
        fileSize = {}
        # 执行命令
        self.tn.write(command.encode('ascii') + b'\n')
        time.sleep(0.5)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        rs1 = command_result.split('\r\n', 3)
        rs2 = rs1[3].split('\r\n')
        for rs in rs2:
            if 'yuv' in rs:
                fileSize[rs.split()[8]] = rs.split()[4]
        return fileSize

    # 此函数用来获取yuv文件的名称，已弃用，get_size函数更为方便
    # def get_yuv(self):
    #     command = 'ls|grep yuv|grep -v Fail'
    #     # 执行命令
    #     self.tn.write(command.encode('ascii') + b'\n')
    #     time.sleep(0.5)
    #     # 获取命令结果
    #     command_result = self.tn.read_very_eager().decode('ascii')
    #     rs1 = command_result.split('\r\n')
    #     rs2 = []
    #     for r in rs1:
    #         if 'DATA' in r:
    #             rs2.append(r)
    #     # logging.warning('命令执行结果：\n%s' % command_result)
    #     return rs2

    # 进行tftp传输
    def tftp(self, fileName, localIp):
        command = 'tftp -pl ' + fileName + ' ' + localIp
        # 执行命令
        self.tn.write(command.encode('ascii') + b'\n')
        time.sleep(0.5)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        logging.warning('命令执行结果：\n%s' % command_result)

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")
        print('登出')


if __name__ == '__main__':
    # 板端ip
    host_ip = '192.168.31.233'
    # 电脑ip
    local_ip = '192.168.31.5'
    # 账户和密码
    username = 'root'
    password = '123456'
    # tftp目录
    tftpPath = '/tftp'
    # 用于存储tftp文件路径的字典
    tftpPaths = {}
    # 用于存储文件是否传输完成的标志的字典
    finishs = {}
    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    if telnet_client.login_host(host_ip, username, password):
        telnet_client.enter_U()
        fileSize = telnet_client.get_size()
        # yuv文件个数
        sum = len(fileSize)
        for f in fileSize:
            tftpPaths[f] = tftpPath + '/' + f
            finishs[f] = False
        # 存储telnet连接与文件名对应关系的字典
        telnets = {}

        start = time.time()
        for f in fileSize:
            telnet = TelnetClient()
            telnets[f] = telnet
            if telnet.login_host(host_ip, username, password):
                telnet.enter_U()
                telnet.tftp(f, local_ip)
                print('进行', f, '的传输')
        time.sleep(2)
        # 传输完毕文件个数
        finish = 0

        # 通过对比电脑里面的文件与板端文件大小，看是否传输完毕，每十秒检查一遍
        while True:
            for f in fileSize:
                # 若已传输完毕，则不用管
                if finishs[f]:
                    continue
                # 获取对应文件目前大小
                size = os.path.getsize(tftpPaths[f])
                if size == int(fileSize[f]):
                    finish += 1
                    print(f, '已经传输完毕')
                    for _ in range(0, finish):
                        print('####', end='')
                    for _ in range(finish, sum):
                        print('    ', end='')
                    print(finish, '/', sum)
                    end = time.time()
                    print('截止目前耗时', int(end - start), '秒')
                    # 对应文件标志设定为传输完成
                    finishs[f] = True
                    # 登出连接
                    telnets[f].logout_host()

            if finish == sum:
                break
            else:
                # 设定为10秒检查一次
                time.sleep(10)

        telnet_client.logout_host()
