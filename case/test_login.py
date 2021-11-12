import pytest
import json
import allure
from api.login import LoginApi
from conf.config import settings
from tools.read_file_data import readfile
from tools.log import get_logger


class TestLogin:
    def setup(self):
        """
        实例化登录API对象
        :return:
        """
        # 实例化登录对象
        self.loginapi = LoginApi()
        # 实例化日志对象
        self.loginfo = get_logger()


    @allure.feature("登录-模块")
    @allure.story("登录-测试案例")
    @allure.title("登录成功测试")
    @pytest.mark.parametrize('test_data', readfile("/data/login.yml"))
    def test_login(self, test_data):
        """
        登录测试
        :param test_data: 登录测试数据
        :return:
        """
        # 请求url
        login_url = "".join([settings.BASE_URL, test_data.get("url")])

        # #############发送请求,获取响应结果#############
        response = self.loginapi.login(url=login_url, data=json.loads(test_data.get("body")))
        self.loginfo.info("=====发送登录员工api{}，获取响应{}=====".format(login_url, response))

        # #############断言#############
        # 预期结果
        expect_data = json.loads(test_data.get("expect"))
        # 响应结果与预期结果判断
        assert response.json().get("code") == expect_data.get("code")
        self.loginfo.info("=====登录员工api{}，响应数据与预期数据做断言，{}=={}=====".format(login_url, response.json(), expect_data))


    def teardown(self):
        pass


if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])