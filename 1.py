import os
from bs4 import BeautifulSoup

from bs4 import UnicodeDammit  # BS内置库，用于推测文档编码

import urllib.request  # 发起请求，获取响应

u = input("tele 的網址")
 
file_path = "F:\\download\\PCI\\1"
file_name = " "
# 创建文件夹
def CreateFolder(file_name):
    flag = True
    num = 0
    while flag == 1:
        if num <= 0:
            file = file_path + '\\' + file_name  # 如果文件夹不存在，则创建文件夹
        else:
            file = file_path + '\\' + str(num) + '_' + file_name  # 如果文件夹已存在，则在文件夹前面加上数字，防止覆盖掉以前保存过的文件
        if not os.path.exists(file):
            os.mkdir(file)
            flag = False
        else:
            print('该文件名已存在，已重新命名')
            flag = True
            num += 1
            # time.sleep(1)
    # 返回文件存放的路径
    path = os.path.abspath(file) + '\\'
    return path

def image_spider(start_url):

    global count  # 记录图片数量

    # 抓bug

    try:

        req = urllib.request.Request(start_url, headers=headers)  # 创建请求对象

        data = urllib.request.urlopen(req)  # 发起请求

        data = data.read()  # 获得响应体

        dammit = UnicodeDammit(data, ["utf-8", "gbk"])

        data = dammit.unicode_markup  # 解码

        # 指定Beautiful的解析器为 html.parser

        soup = BeautifulSoup(data, "html.parser")

        # 查找img标签

        images = soup.select("img")

        for image in images:

            # 抓bug

            try:

                src = image["src"]

                url =  "https://telegra.ph" + src

                count = count + 1

                # 调用download函数

                download(url, count)

            # 抓到bug的处理

            except Exception as err:

                print(err)

    except Exception as err:

        # 打印这个错误对象

        print(err)

 

 

def download(url, count):

    try:

        if url[len(url) - 4] == ".":  # 如果 图片url的长度的倒数第四位 = .

            ext = url[len(url) - 4:]

        else:

            ext = ".jpg"

 

        req = urllib.request.Request(url, headers=headers)

        data = urllib.request.urlopen(req)

        data = data.read()  # 读取文件

        # 以images+序号命名；wb表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，则覆盖写
        ifs = path + str(count) + ext
        
        fobj = open(ifs, "wb")

        fobj.write(data)  # 写入文件

        fobj.close()  # 关闭文件

        print("downloaded" + str(count) + ext)  # 打印下载(爬取)信息

    except Exception as err:

        print(">>>",err)

path = CreateFolder(file_name)
print("创建文件夹成功: ", path)

 

# 目标url

start_url = u

 

# User-Agent会告诉网站服务器，访问者是通过什么工具来请求的

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

 

count = 0

 

# 调用函数

image_spider(start_url)

 

print("The end...")

 
