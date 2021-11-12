import pytest
from api.login import LoginApi
from conf.config import settings
from conf import settings
from tools.log import get_logger

# 日志函数
loginfo = get_logger()
@pytest.fixture(scope='session', autouse=True)
def login():
    # 调用登录接口
    response = LoginApi().login(
        url = settings.LOGIN_USERINFO.get("login_url"),
        data = settings.LOGIN_USERINFO.get("body")
    )
    # 提取响应token
    token = response.json().get("data")
    # 添加token到请求头部
    settings.HEADERS.update({"Authorization": "Bearer " + token})
    loginfo.info("=====发送登录员工api，获取token做认证，请求头传输'Bearer token'，获取token{}=====".format(token))

