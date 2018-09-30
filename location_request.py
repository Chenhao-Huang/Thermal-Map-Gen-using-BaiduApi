
# coding: utf-8

# In[22]:


import json
from urllib.request import urlopen, quote
import requests,csv
import pandas as pd #导入这些库后边都要用到

url = 'http://api.map.baidu.com/geocoder/v2/'
output = 'json'
ak = '您的密钥'

dict = {'上海市静安区': 10, '上海市普陀区': 7, '上海市黄浦区': 12, '上海市长宁区': 5};
for d,x in dict.items():
    add = quote(d)
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    lng = temp['result']['location']['lng']
    lat = temp['result']['location']['lat']
    str_temp = '{"lng":' + str(lng) + ',"lat":' + str(lat) + ',"count":' + str(x) +'},'
    print(str_temp)



# In[23]:


import base64
f=open('1.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(ls_f)

