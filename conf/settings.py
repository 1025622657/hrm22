import os

# 设置代理，方便调试
PROXIES={
    'http':'http://localhost:8080'
}

# base路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据保存格式
TYPE = "yml"

# ##############请求参数############
#请求url
BASE_URL = 'http://ihrm-test.itheima.net'

#请求头部信息
HEADERS = {'content-type': 'application/json;charset=utf-8',
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'http://ihrm-test.itheima.net'
            }

#登录用户信息
LOGIN_USERINFO = {'login_url': BASE_URL + '/api/sys/login',
                  'body': {'mobile': '13800000001', 'password': '123456'}
                  }