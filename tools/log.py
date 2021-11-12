import logging
from conf.config import settings

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_name = ''.join([settings.BASE_DIR, r'/log/logger'])
    print("--------->>>><<<",file_name)
    #if not logger.handlers:
    fh = logging.FileHandler(file_name)
    fh.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    fm = logging.Formatter("%(asctime)s-%(pathname)s-%(module)s-%(funcName)s-%(levelname)s-%(lineno)d-%(message)s")
    fh.setFormatter(fm)
    sh.setFormatter(fm)

    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger


if __name__ == "__main__":
    Loggin = get_logger()
    Loggin.debug('debug messages1')
    Loggin.info('info messages1')