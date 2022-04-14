# ubuntu上环境准备
- 课程：https://www.bilibili.com/video/BV1B441197rZ?p=24&spm_id_from=pageDriver

## 安卓环境配置

```shell
# ubuntu 21.10
# JDK环境
# 安装openjdk
sudo apt-get install openjdk-8-jdk
# AndroidSDK环境
sudo snap install android-studio --classic
# SDK环境变量配置，例安装目录为：/home/Android/Sdk
vim ~/.bashrc
# 末尾添加以下内容
export ANDROID_HOME=/home/Android/Sdk
# ADB环境
sudo apt-get install adb
```

## Appium环境搭建

```shell
# 下载appium linux版本Appium-Server-GUI-linux-1.22.2.AppImage：https://github.com/appium/appium-desktop/releases
# 赋权
sudo chmod +x Appium-Server-GUI-linux-1.22.2.AppImage
# 重命名
mv Appium-Server-GUI-linux-1.22.2.AppImage appium
# 启动啊appium
./appium

# 安装Appium-Python-Client库
pip install Appium-Python-Client
```

## 快速体验appium

1、启动appium

`./appium`

2、在pycharm中新建项目hello_appium，新建demo.py。输入以下内容（填入测试设备实际的参数）

```python
# demo.py
from appium import webdriver

desired_caps = dict()
# 平台的名字
desired_caps['platformName'] = 'Android'
# 平台的版本
desired_caps['platformVersion'] = '9'
# 设备的名字
desired_caps['deviceName'] = 'R4CBB19B25602280'
# 要打开的应用
desired_caps['appPackage'] = 'com.android.settings'
# 要打开的界面
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.quit()
```

## Appium基础API
```python
# 启动activity
driver.start_activity('pkg_name','activity_name')
# 获取app的包名和activity
driver.current_package
drivier.current_activity
# 关闭app
driver.close_app()
# 关闭驱动对象
driver.quit()
# 安装app
driver.install_app(path)
# 卸载app,app_id也可以用app包名
driver.remove_app(app_id)
# 判断app是否安装
driver.is_app_installed(app_id)
# 将应用置于后台一定时间后返回前台，模拟热启动
driver.backgroud_app(seconds)
```

## UIAutomatorViewer
- 使用uiautomatorviewer定位元素
- 元素定位操作API
```shell
# 定位一个元素
driver.find_element_by_id(id_value)
driver.find_element_by_class_name(class_name)
driver.find_element_by_xpath(xpath_value)
# 定位一组元素
driver.find_elements_by_id(id_value)
driver.find_elements_by_class_name(class_name)
driver.find_elements_by_xpath(xpath_value)
# 定位元素的注意点
# 1、若使用find_element_by_xx方法，传入一个没有的特征，会报NoSuchElementException的错误
# 2、若使用find_elements_by_xx方法，传入一个没有的特征，不会报错，返回一个空列表
```
## 元素等待
由于一些原因（网络、服务器、设备配置等），我们想找的元素没有立刻出来，此时如果直接定位可能会报错。  
概念：找元素的时候，通过一个时间的设置，进行等待元素，防止报错。  
- 隐式等待
```shell
# 设置元素等待的时长t，超时抛出NoSuchElementException异常
driver.implicitly_wait(t)
```
- 显式等待


