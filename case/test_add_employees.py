import pytest
import json
import allure
from api.employees import EmployeesApi
from conf.config import settings
from tools.read_file_data import readfile
from tools.log import get_logger


class TestAddEmployees:
    employeesid = None
    del_employees_url = None

    def setup(self):
        """
        实例化员工API对象
        :return:
        """
        # 实例化员工对象
        self.employeesapi = EmployeesApi()
        # 实例化日志对象
        self.loginfo = get_logger()

    @allure.feature("员工-模块")
    @allure.story("员工-测试案例")
    @allure.title("员工添加成功测试")
    @pytest.mark.parametrize('test_data', readfile("/data/add_employees.yml"))
    def test_add_employees(self, test_data):
        """
        添加员工测试
        :param test_data: 添加员工测试数据
        :return:
        """
        # 请求url
        add_employees_url = "".join([settings.BASE_URL, test_data.get("url")])

        # #############发送请求,获取响应结果#############
        response = self.employeesapi.add_employees(method=test_data.get("method"), url=add_employees_url, data=json.loads(test_data.get("body")))
        # 提取添加的员工ID
        TestAddEmployees.employeesid = response.json().get("data").get("id")
        self.loginfo.info("=====发送添加员工api{}，获取响应，获取员工id{}=====".format(add_employees_url, self.employeesid))

        # 删除员工的url与添加员工的url一致
        TestAddEmployees.del_employees_url = add_employees_url

        # #############断言#############
        # 预期结果
        expect_data = json.loads(test_data.get("expect"))
        # 响应结果与预期结果判断
        assert response.json().get("code") == expect_data.get("code")
        self.loginfo.info("=====添加员工api{}，响应数据与预期数据做断言，{}=={}=====".format(add_employees_url, response.json(), expect_data))

    @allure.feature("员工-模块")
    @allure.story("员工-测试案例")
    @allure.title("员工添加成功测试")
    @pytest.mark.parametrize('test_data', readfile("/data/add_employees.yml"))
    def test_add_employees(self, test_data):
        """
        添加员工测试
        :param test_data: 添加员工测试数据
        :return:
        """
        # 请求url
        add_employees_url = "".join([settings.BASE_URL, test_data.get("url")])

        # #############发送请求,获取响应结果#############
        response = self.employeesapi.add_employees(method=test_data.get("method"), url=add_employees_url,
                                                   data=json.loads(test_data.get("body")))
        # 提取添加的员工ID
        TestAddEmployees.employeesid = response.json().get("data").get("id")
        self.loginfo.info("=====发送添加员工api{}，获取响应，获取员工id{}=====".format(add_employees_url, self.employeesid))

        # 删除员工的url与添加员工的url一致
        TestAddEmployees.del_employees_url = add_employees_url

        # #############断言#############
        # 预期结果
        expect_data = json.loads(test_data.get("expect"))
        # 响应结果与预期结果判断
        assert response.json().get("code") == expect_data.get("code")
        self.loginfo.info(
            "=====添加员工api{}，响应数据与预期数据做断言，{}=={}=====".format(add_employees_url, response.json(), expect_data))

def teardown(self):
        # 删除员工url
        del_url = "".join([self.del_employees_url, '/', self.employeesid])
        # 调用删除员工接口，实行数据清理
        self.employeesapi.del_employees(url=del_url, data={"id": self.employeesid})
        self.loginfo.info("=====发送删除员工api{}，做数据清理，删除员工id{}=====".format(del_url, self.employeesid))




if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])
