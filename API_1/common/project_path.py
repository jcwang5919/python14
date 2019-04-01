# -*- coding: utf-8 -*-
# @Time    : 2019/3/config 21:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : project_path.py
import os

# 文件的路径 放到这里
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


# 测试用例的路径
case_path = os.path.join(project_path, 'test_cases', 'test_api.xlsx')


# 日志的路径
log_path = os.path.join(project_path, 'test_result', 'test_log', 'test.log')


# 测试结果的路径


if __name__ == '__main__':
    print('项目的路径为: ', project_path)
    print('测试用例的路径为: ', case_path)
    print('日志文件的路径为: ', log_path)
