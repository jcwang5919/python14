import unittest
import HTMLTestRunnerNew
from API_2.common import project_path
from API_2.test_cases.test_cases import TestCases

# 新建一个测试集
suite = unittest.TestSuite()

# 添加用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCases))

# 执行用例 生成测试报告
with open(project_path.report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='py14 0313测试报告',
                                              description='py14 0313测试报告',
                                              tester='测试界的一个小学生')
    runner.run(suite)  # 执行用例  传入suite suite里面是我们收集的测试用例
