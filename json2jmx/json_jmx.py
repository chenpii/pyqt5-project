# -*- coding: utf-8 -*-
import glob, os
from swaggerjmx.convert import conversion
from swaggerjmx.settings import Settings as ST

#  swagger_url_json_path
#  swaggerApi.json 是从yapi导出的文件
# ST.swagger_url_json_path = 'swaggerApi4.json'

try:

    print(
        "使用说明：此程序可将.json格式接口文件转换成.jmx格式，方便接口自动化。\n"
        "1.在yapi上选择导出接口的导出方式为'swaggerjson'导出，或在swagger平台选择OpenAPI导出;\n"
        "2.导出的.json文件与json_jmx.exe放在同一个目录;\n"
        "3.执行json_jmx.exe脚本;\n"
        "4.转换成功的.jmx文件存放在jmx文件夹中;\n")

    # Files = glob.glob("*.json")
    Files = glob.glob(r"I:\接口自动化\00.json转jmx格式工具\*.json")
    print("读取到待转换的文件列表为：" + str(Files))
    ST.swagger_url_json_path = ''
    ST.report_path = 'jmx'
    for jsonFile in Files:
        try:
            ST.swagger_url_json_path = (str(jsonFile))
            conversion()
            print("{} 文件格式转换完成!".format(jsonFile))
        except Exception as e:
            # os.system("pause")
            print("{} 文件格式转换 异常!只支持swaggerjson转换为jmx文件喔！不支持yapi上的json格式".format(jsonFile))

except Exception as e:
    print(e.__traceback__.tb_frame.f_globals["__file__"])
    print("异常所在行数：" + str(e.__traceback__.tb_lineno))
    print(e)
    os.system("pause")
