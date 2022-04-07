# pip
## 列出已安装的包
`pip freeze`  
`pip list`
## 导出requirements.txt
`pip freeze > requirements.txt`
## 安装包
### 在线安装
`pip install <pkg>`  
`pip install -r requirements.txt`  
通过使用==来指定版本，不写则安装最新版  
requirements.txt内容格式为：
```sh
pymsql==2.12
flask==1.1.0
...
```
### 本地安装
`pip install <pkg>`
### 卸载包
`pip uninstall <pkg>`
`pip uninstall -r requirements.txt`
### 升级包
`pip install -U <pkg>`  
`pip install <pkg> --upgrade`
### 升级pip
`pip install -U pip`
### 显示包所在的目录
`pip show -f <pkg>`
### 搜索包
`pip search <搜索关键字>`
### 查询可升级对包
`pip list -o`
### 下载包而不安装
`pip install <pkg> -d <目录>`  
`pip install -d <目录> -r requirements.txt`
### 打包
`pip wheel <pkg>`
### 国内pypi源
- v2ex：pypi.v2ex.com/simple  
- 豆瓣：http://pypi.douban.com/simple  
- 中国科大：http://pypi.mirrors.ustc.edu.cn/simple/  
#### 指定单次安装源
`pip install <pkg> -i http://pypi.douban.com/simple`
#### 指定全局安装源
- linux和macos，配置文件为（没有则新建）：`$HOME/.pip/pip.conf`
- windows:  
`%HOME%\pip\pip.ini`  
输入以下内容：
```sh
[global]
index-url = http://pypi.douban.com/simple
```
