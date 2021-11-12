import requests
import allure
from conf import settings


class EmployeesApi:
    @allure.step("setup:调用添加员工api接口")
    def add_employees(self, url, data, method="post", headers=settings.HEADERS):
        """

        :param url: 添加url
        :param data: 添加的数据
        :param method: 请求方式
        :param headers: 请求头，需token认证
        :return: 返回添加成功的响应数据
        """
        return requests.request(method=method, url=url, json=data, proxies=settings.PROXIES, headers=headers)

    @allure.step("setup:调用查询员工api接口")
    def get_employees(self, url, method="get", headers=settings.HEADERS):
        """
        查询员工信息
        :param url: 查询url
        :param method: 请求方式
        :param headers: 请求头，需token认证
        :return: 返回查询的响应数据
        """
        return requests.request(method=method, url=url, proxies=settings.PROXIES, headers=headers)


    @allure.step("setup:调用修改员工api接口")
    def put_employees(self, url, data, method="put", headers=settings.HEADERS):
        """
        修改员工信息
        :param url: 修改url
        :param method: 请求方式
        :param headers: 请求头，需token认证
        :return: 返回修改后的响应数据
        """
        # 拼接修改的url
        return requests.request(method=method, url=url, json=data, proxies=settings.PROXIES, headers=headers)

    @allure.step("setup:调用删除员工api接口")
    def del_employees(self, url, data, method="delete", headers=settings.HEADERS):
        """
        删除员工信息
        :param url: 删除url
        :param method: 请求方式
        :param headers: 请求头，需token认证
        :return: 返回删除的响应数据
        """
        return requests.request(method=method, url=url, json=data, proxies=settings.PROXIES, headers=headers)
