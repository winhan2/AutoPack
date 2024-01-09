# coding: utf-8

import subprocess
import os

class Command:
    def __init__(self, logger_obj):
        self.logger_obj = logger_obj

    # 定义'help'函数
    def help(self):
        help_content = """
命令\t\t\t功能

help\t\t获取帮助
exit\t\t退出程序
pack\t\t打包文件
"""
        print(help_content)
        self.logger_obj.info('help命令执行成功')

    # 定义'pack'函数
    def pack(self, route):
        with open('..\AutoPack.sh', mode='wt', encoding='utf-8') as apfw:
            self.logger_obj.info('AutoPack.sh文件创建（打开并全部清除）成功')
            apfw.write(f'cd {os.path.split(route)[0]}\n')
            apfw.write(f'pyinstaller -F {route}\n')
            self.logger_obj.info('AutoPack.sh文件写入完成')
        self.logger_obj.info('AutoPack.sh文件关闭成功')
        os.system('../AutoPack')
        self.logger_obj.info('AutoPack.sh文件执行成功')
        print(f'AutoPack.sh({os.path.split(route)[1]}打包用文件)在{os.path.split(route)[0]}路径下')

    # 定义'install_pyinstaller'函数
    def install_pyinstaller(self):
        # 模拟控制台执行'pip install pyinstaller'命令
        ipi_cmd = subprocess.Popen(
            'pip install pyinstaller',
            shell=True,
            stderr=subprocess.PIPE
        )
        # 获取执行结果，并且对其进行使用utf-8编码解码
        stderr_res = ipi_cmd.stderr.read().decode('utf-8')

        # 判断结果是否正确
        # 如果结果正确
        if stderr_res:
            self.logger_obj.error(f"""pyinstaller模块安装失败，错误信息如下：
            {stderr_res}
            """)
        # 如果结果错误
        else:
            self.logger_obj.info('pyinstaller模块安装成功')


if __name__ == '__main__':
    from lib.logger import Logger
    logger_o = Logger('3')
    command = Command(logger_o)
    command.help()