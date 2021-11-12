import requests
import allure
from conf import settings


class LoginApi:
    @allure.step("setup:调用登录api接口")
    def login(self, url, data, method="post", headers=settings.HEADERS):
        return requests.request(method=method, url=url, json=data, proxies=settings.PROXIES, headers=headers)

