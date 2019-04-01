import re

Param = {"no_reg_tel": "18688773467", "member_id": '9507', "regtime": "888888"}
# 字符串
str_1 = "{'code': '10001', " \
        "'status': 1," \
        " 'data': {'regtime': '${regtime}', " \
        "'pwd': 'E10ADC3949BA59ABBE56E057F20F883E', " \
        "'regname': '小蜜蜂', " \
        "'leaveamount': '9000.00', " \
        "'mobilephone': '${no_reg_tel}', " \
        "'type': '1'," \
        " 'id': ${member_id}}," \
        " 'msg': '取现成功'}"

while re.findall("\$\{(.*?)\}", str_1):  # 用的就是新的字符串
    result = re.search("\$\{(.*?)\}", str_1)  # ${no_reg_tel}  ${member_id}}
    print(result)
    arg1 = result.group(0)  # 你所找到的匹配内容所在的字符串 ${regtime}
    print('这里是arg1:', arg1)  # ${regtime} arg1
    key = result.group(1)  # 你所匹配的内容  （.*?）匹配到的内容
    print('这里是key：', key)  # regtime
    # 字符串的替换  后面的while循环 用的是最新的str_1
    str_1 = str_1.replace(arg1, Param[key])  # 保存新的值到str_1 继续循环
    print(str_1)
