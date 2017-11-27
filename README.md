# 项目介绍
1. 运行环境：
	python3 + Mysql + django + scrapy + redis

2. 项目文件：
	aynu: 存放scrapy爬虫文件.aynu/aynu/spiders/a51job.py为爬取51job的爬虫，xici为爬取西刺代理的爬虫
	aynu_job: 存放django相关文件
	sql：存放项目相关的mysql数据表

3. 功能简介
	1. 使用scrapy框架对51job就行全站爬取，并将爬取来的数据存入mysql数据库，
	2. 爬取西刺代理只把有效的代理存入数据库中，运行aynu/utils目录下的filter_proxy_thread.py 对数据库中已有的代理进行有效性判断，删除其中无效的代理 
	3. 为了反反爬虫机制使用了fake_useragent随机UserAgent,并使用从西刺代理爬下来的代理


# 运行项目
1. 克隆本项目
```
git clone https://github.com/ngauerh/aynu.git
```

2. 创建并激活虚拟环境

	创建虚拟环境
	```
	virtualenv env  
	```
	激活虚拟环境
	```
	# windows
	env\Scripts\activate
	# linux
	source env/bin/activate
	```
3. 安装依赖
	确保激活并使用了虚拟环境，进入requirements.txt所在目录
	```
	pip install -r requirements.txt
	```
4. 数据库操作

	1. 新建数据库，将sql文件下的ip_proxy.sql和job.sql两张表导入新建的数据库中，其中ip_proxy表用来存放从西刺代理抓取的免费代理，job表用来存放从51job抓取的数据
	2. 进入aynu_job目录进行数据迁移
	```
	python manage.py migrate
	```
5. 配置文件

	1. aynu/settings.py
		REDIS_HOST = '' # redis服务器ip
		REDIS_PORT =    # redis服务器端口
	2. aynu/piplines.py
		17行：pymysql.connect('mysql地址','用户名', '密码', '数据库名',charset="utf-8")
	3. utils/get_proxy.py
		3行: mydb = Mydb('mysql地址','用户名', '密码', '数据库名',charset="utf-8")
	4. utils/filter_proxy_three.py
		57行: mydb = Mydb('mysql地址','用户名', '密码', '数据库名',charset="utf-8")
	5. aynu_job/settings.py
		修改数据库信息

# 效果
![](https://i.imgur.com/9muWPn4.png)
![](https://i.imgur.com/aoswCFm.png)
![](https://i.imgur.com/6FKWC3a.png)
