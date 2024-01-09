# coding: utf-8
# 日志配置字典
LOGGING_DIC = {
    'version': 1.0,
    'disable_existing_loggers': False,
    # 日志格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(threadName)s:%(thread)d [%(name)s] %(levelname)s [%(pathname)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(name)s] %(levelname)s  %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'test': {
            'format': '%(asctime)s %(message)s',
        },
        'test1': {
            'format': '%(asctime)s %(message)s',
        },
    },
    'filters': {},
    # 日志处理器
    'handlers': {
        'console_warning_handler': {
            'level': 'WARNING',  # 日志处理的级别限制
            'class': 'logging.StreamHandler',  # 输出到终端
            'formatter': 'standard'  # 日志格式
        },
        'file_info_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'filename': 'log\logs.log',
            'maxBytes': 1024*1024*1024*1024*1024,  # 日志大小 1T
            'backupCount': 65536,  # 日志文件保存数量限制 100
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'console_debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 输出到终端
            'formatter': 'standard',
        },
    },
    # 日志记录器
    'loggers': {
        'output_warning_shell': {  # 导入时logging.getLogger时使用的app_name
            'handlers': ['console_warning_handler'],  # 日志分配到哪个handlers中
            'level': 'WARNING',  # 日志记录的级别限制
            'propagate': False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        },
        'output_shell_and_file': {
            'handlers': ['console_warning_handler', 'file_info_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'debug': {  # 导入时logging.getLogger时使用的app_name
            'handlers': ['console_debug_handler'],  # 日志分配到哪个handlers中
            'level': 'DEBUG',  # 日志记录的级别限制
            'propagate': False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        },

        'output_info_shell': {  # 导入时logging.getLogger时使用的app_name
            'handlers': ['console_debug_handler'],  # 日志分配到哪个handlers中
            'level': 'INFO',  # 日志记录的级别限制
            'propagate': False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        }
    }
}