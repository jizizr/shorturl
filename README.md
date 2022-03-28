# shorturl
A simple shorturl website powered by python
# 使用Python实现的简单短网站
----------------------------------------------
## 项目简介:
URL(统一资源定位器)是访问网站资源所必须的，但为了精确定位资源，URL不可避免的会变长，不利于记忆、分享和在页面显示。所以就出现了短链服务，如：B站的 b23.tv，和微博的 t.cn。本项目就是构建了类似服务，供个人使用。

## 环境准备：
1. python (含pip)
2.Nginx (可选)

## 安装环境：
### Windows
```
1.安装python
2.pip install -r requirements.txt
```
### Ubuntu
```
1.sudo apt install python3
2.pip install -r requirements.txt
```
### 运行(先转到文件目录):
```
python main.py      	 //Windows
python3 main.py    	//Ubuntu
```
### 访问:
http://127.0.0.1:81/
-------------------------------------------
本项目已部属至公网
demo: https://s.z-r.cc
## 后台管理：
User: admin
Password: 123
采用pywsgi编写wsgi网关，并使用Nginx反向代理
-------------------------------------------------
## 本项目已测试环境：
```
1. Ubuntu 20.04 + Python 3.8.10 + Nginx 1.19.8
2. Ubuntu 21.10 + python 3.9.7
3.Windows LTSC + python 3.10.0
4.Windows Server 2016 + python 3.8.6
5.Windows Server 2019 + python 3.8.6
```
本项目所用到的前端模板来自于 bootstrap
