# ubuntu上环境准备

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



