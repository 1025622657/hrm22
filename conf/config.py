import importlib
import os

class Settings(object):
    """
    实现默认配置与自定义配置的整合，注默认配置写在前面，
    程序从上往下执行，若配置自定义则覆盖默认配置
    """

    def __init__(self):

        ##########找到自定义配置#########
        # 自定义配置获取方式
        # from config import settings#这种方式导入，则该路径固定
        # os.environ.get获取方式时，需在当前运行程序的环境变量添加如bin/start.py，
        os.environ['USER_SETTINGS'] = "conf.settings"
        settings_module = os.environ.get('USER_SETTINGS')  # 获取
        if not settings_module:  # 没有自定义配置，则不执行如下
            return
        # 有自下定义配置则执行
        # 根据字符串导入模块
        m = importlib.import_module(settings_module)
        for name in dir(m):  # dir(m)即全局属性
            if name.isupper():
                value = getattr(m, name)
                setattr(self, name, value)
        # 找到自定义配置


settings = Settings()

