import pytest
import json
import allure
from api.employees import EmployeesApi
from conf.config import settings
from tools.read_file_data import readfile
from tools.log import get_logger
import warnings
warnings.filterwarnings("ignore")


class TestGetEmployees:
    # 员工id
    employeesid = None
    employees_url = None

    def setup_class(self):
        """
        实例化员工API对象
        :return:
        """
        # 实例化员工对象
        self.employeesapi = EmployeesApi()

        # 修改员工API参数化，从文件读取
        add_employess_info = readfile("/data/get_employees.yml")[0]
        # 日志
        self.loginfo = get_logger()

        # 添加员工api请求的url
        add_employees_url = "".join([settings.BASE_URL, add_employess_info.get("url")])

        # #############发送请求,获取响应结果#############
        response = self.employeesapi.add_employees(method=add_employess_info.get("method"),
                                                   url=add_employees_url,
                                                   data=json.loads(add_employess_info.get("body"))
                                                   )
        # 提取添加的员工ID
        TestGetEmployees.employeesid = response.json().get("data").get("id")
        self.loginfo.info("=====修改员工api,前置发送添加员工api{}，获取响应，获取员工id{}=====".format(add_employees_url, self.employeesid))

        # 员工的url
        TestGetEmployees.employees_url = add_employees_url

    @ allure.feature("员工-模块")
    @ allure.story("员工-测试案例")
    @ allure.title("员工查询成功测试")
    @ pytest.mark.parametrize('test_data', readfile("/data/get_employees.yml")[1:])
    def test_put_employees(self, test_data):
        """
        查询员工测试
        :param test_data: 查询员工测试数据
        :return:
        """
        # 请求url
        get_employees_url = "".join([settings.BASE_URL, test_data.get("url")]).format(self.employeesid)

        # #############发送请求,获取响应结果#############
        response = self.employeesapi.get_employees(method=test_data.get("method"), url=get_employees_url)

        self.loginfo.info("=====发送查询员工api{}，获取响应，获取员工id{}=====".format(get_employees_url, self.employeesid))

        # #############断言#############
        # 预期结果
        expect_data = json.loads(test_data.get("expect"))
        # 响应结果与预期结果判断
        assert response.json().get("code") == expect_data.get("code")
        self.loginfo.info("=====查询员工api{}，响应数据与预期数据做断言，{}=={}=====".format(get_employees_url, response, expect_data))


    def teardown_class(self):
        del_employees_url = ''.join([self.employees_url, '/', self.employeesid])
        self.employeesapi.del_employees(del_employees_url, data={"id": self.employeesid})
        self.loginfo.info("=====发送删除员工api{}，做数据清理，删除员工id{}=====".format(del_employees_url, self.employeesid))




if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])
