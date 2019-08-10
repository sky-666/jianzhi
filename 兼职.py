import requests
# json解析库,对应到lxml
import json
# json的解析语法，对应到xpath
import jsonpath

proxies = {
    'http': '120.83.106.8:9999',
    # 'https': '175.148.71.202:9999'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER',
        }
response = requests.get(url = "请输入json网站", headers=headers,proxies=proxies)

lottery_message=json.dumps(response.json(), ensure_ascii=False)

# # 读取reponse
html = response.text

# 把json格式字符串转换成python对象
html = json.loads(html)
# 获取score节点下的数据
qq = jsonpath.jsonpath(html, '$..content')
for i in qq:
    print(i)
