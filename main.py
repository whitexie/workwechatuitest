import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-q', 'testcase/test_appium/test_xueqiu.py', '--alluredir=./report/xml'])