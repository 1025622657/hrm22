import yaml
import json
from conf.config import settings


def readfile(filename, type=settings.TYPE):
    """
    文件类型不同，读取并返回相应文件数据，用于数据
    :param filename: 文件名，需录入相对路径
    :param type: 文件类型
    :return: 返回文件数据
    """
    if type == "yml":
        with open("".join([settings.BASE_DIR + filename]), 'r', encoding='utf-8') as f:
            return list(yaml.safe_load_all(f))
    print("===>>>>", readfile())