# coding: utf-8

# 导入模块
from core.command import Command
from lib.logger import Logger

# 初始化
logger_obj = Logger('2')
command = Command(logger_obj)

# 检测PyInstaller模块是否安装
try:
    import PyInstaller
except ModuleNotFoundError:
    is_ipi = input('无法导入PyInstaller模块，是否自动安装（y/n）')
    if is_ipi == 'y':
        command.install_pyinstaller()

# 定义core函数，以便调用
def core():
    print("使用help命令以获取帮助")

    while True:
        cmd_input = input("请输入命令>>>")

        # 当输入'help'命令时
        if 'help' in cmd_input:
            command.help()
        # 当输入'exit'命令时
        elif cmd_input == 'exit':
            exit()
        # 当输入'pack 打包对象路径'命令时
        elif 'pack' in cmd_input:
            command.pack(cmd_input[5:])


if __name__ == '__main__':
    core()