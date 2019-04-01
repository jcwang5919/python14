from configparser import ConfigParser


class ReadConfig:

    def __init__(self, file_name):  # 配置文件的地址
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding='utf-8')

    def get_int(self, section, option):
        """从配置文件里面获取一个整数"""
        value = self.cf.getint(section, option)  # section  option
        return value

    def get_float(self, section, option):
        """从配置文件里面获取一个浮点数"""
        value = self.cf.getfloat(section, option)  # section  option
        return value

    def get_bool(self, section, option):
        """从配置文件里面获取一个布尔值"""
        value = self.cf.getboolean(section, option)  # section  option
        return value

    def get_str(self, section, option):
        """从配置文件里面获取一个字符串"""
        value = self.cf.get(section, option)  # section  option
        return value

    def get_data(self, section, option):
        """从配置文件里面获取一个元组 字典 列表等类型的数据"""
        value = self.cf.get(section, option)  # section  option
        return eval(value)


if __name__ == '__main__':
    res = ReadConfig('case.conf').get_bool('CASE', 'sex')
    print(type(res))
