# Thermal-Map-Gen-using-BaiduApi
##### Note: Apologise, this work is Chinese-based.
### 解决的问题
利用百度地图API生成热力地图
### 应用的场景  
假设某事件在上海如下4个区县出现的数量为：  
    上海市静安区 10，上海市普陀区 7，上海市黄浦区 12，上海市长宁区 5.  
    目标生成如下图片：  
    ![avatar](/demo.png)

### 步骤
0. 申请百度API调用的key  
&nbsp;&nbsp;http://lbsyun.baidu.com/apiconsole/key?application=key
1. 利用百度API计算出上述4个区县的经纬度, 见 location_request.py.  
2. 把步骤一的运行结果复制到网页中，在网页上生成热力图，见thermal_map.html.  
* 注意: 上述两个文件中“您的密钥”，需要替换成步骤0中所生成的密钥。
More reference:  
百度api live demo: http://lbsyun.baidu.com/index.php?title=jspopular  
https://www.jianshu.com/p/773ff5f08a2c
