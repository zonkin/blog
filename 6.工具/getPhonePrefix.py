# -*- coding: UTF-8 -*-
import requests
import re
import math
import sys

'''
从https://www.guisd.com/ss/guangdong/guangzhou/取7位手机号前缀，
生成手机号字典，很大
'''

response = requests.get('https://www.guisd.com/ss/guangdong/guangzhou/')
response.encoding='utf-8'
print(response.text)
html = response.text

pattern = re.compile(r'\d{7}')
if(html):
    res_list = pattern.findall(html)
    print("get web complete")
    resSize_kb = sys.getsizeof(res_list)/1024
    input_str = input("预计将占用" + str(resSize_kb * 10000) + "KB文件空间，是否继续(Y/n)")
    if(input_str.lower() == "y"):
        out_file = open('res.txt', "a+", encoding="utf-8")
        lines_num = len(res_list)
        for index in range(lines_num):
            line = res_list[index]
            for i in range(0,9999):
               suffix = str(i).rjust(4,'0')
               out_file.write(line + suffix + "\n")
            print(str(round(math.floor(index/lines_num*10000)/100,2)) + "% complete...\n")
        print("100% complete!")
        out_file.close()
    else:
        print("退出")
