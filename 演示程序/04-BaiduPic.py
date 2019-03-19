import re  # 导入正则表达式模块
import requests  # python HTTP客户端 编写爬虫和测试服务器经常用到的模块
import random  # 随机生成一个数，范围[0,1]


# 定义函数方法
def spiderPic(html, keyword):
    print('正在查找 ' + keyword + ' 对应的图片,下载中，请稍后......')
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    for addr in re.findall('"objURL":"(.*?)"', html, re.S):  # 查找URL
        print('正在爬取URL地址：' + str(addr)[0:30] + '...')  # 爬取的地址长度超过30时，用'...'代替后面的内容
        try:
            pics = requests.get(addr, headers=headers, timeout=10)  # 请求URL时间（最大10秒）
            fq = open('D:\\img\\' + (keyword + '_' + str(random.randrange(0, 1000, 4)) + '.jpg'), 'wb')  # 下载图片，并保存和命名
            fq.write(pics.content)
            fq.close()
        except requests.exceptions.ConnectionError:
            print('您当前请求的URL地址出现错误')
            continue
        


# python的主方法
if __name__ == '__main__':
    word = input('请输入你要搜索的图片关键字：')
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    # 调用函数
    spiderPic(result.text, word)
