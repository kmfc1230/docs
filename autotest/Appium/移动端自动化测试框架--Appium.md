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
# 设置元素等待的时长timeout，单位秒，超时抛出NoSuchElementException异常
driver.implicitly_wait(timeout)
```
- 显式等待
```shell
# 针对所有定位元素超时时间不同的时候
# 使用显式等待，在20s内，每隔3s查找一次，id为xxx的元素
WebDriverWait(driver ,20 ,3).until(lambda x: x.find_element_by_id("xxx"))
```
- 区别：显式等待为单个元素有效，隐式等待为全局元素

## 元素操作API
- 点击元素
```shell
element.click()
```
- 输入和清空输入框内容
```shell
# 输入
# 默认输入中文有问题，需要加入参数
desired.caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# value 要输入的内容
element.send_keys(value)
# 清空
element.clear()
```
- 获取文本内容
```shell
element.text
```
- 获取元素的属性值
```shell
element.get_attribute(value)
```

## 滑动和拖拽事件
- swipe 滑动事件
```shell
# 从一个坐标滑动到另一个坐标，只能是两个点之间的滑动
# duration: 滑动操作持续的时间，单位：ms
driver.swipe(start_x, start_y, end_x, end_y, duration=None)
```
- scroll 滑动事件
```shell
# 惯性大
# origin_e1         滑动开始的元素
# destination_el    滑动结束的元素
driver.scroll(origin_e1, destination_el)
```
- drag_and_drop 拖拽事件
```shell
# 没有惯性
driver.drag_and_drop(origin_e1, destination_el)
```
- 总结
  - swipe
    - 参数是坐标点
    - 持续时间短，惯性大，持续时间长，惯性小
  - scroll
    - 参数是元素
    - 没有持续时间，有惯性
  - drag_and_drop
    - 参数是元素
    - 没有持续时间，没有惯性
- 滑动和拖拽事件选择
  - 考虑是否有“惯性”，传递的参数是“坐标”还是“元素”

## 高级手势TouchAction
- 概念和作用
  - 高级手势，可以将小的动作组合成复杂的动作
- 步骤
  - 创建TouchAction对象
  - 调用执行的动作
  - perform()执行
- 轻敲操作
  - 方法
    - `TouchAction(driver).tap(el=None, x=None, y=None).perform()`
  - 参数：元素(el)或坐标(x, y)
  - 多次点击
    - 使用count参数
- 按下/抬起操作
  - 方法
    - 按下：`TouchAction(driver).press(el=None, x=None, y=None).perfrom`
    - 抬起：`TouchAction(driver).release().perform()`
  - 参数：元素(el)或坐标(x, y)
  - 模拟轻敲
    - `TouchAction(driver).press(x=650, y=650).release().perform()`
- 等待操作
  - 方法
    - `TouchAction(driver).wait(1000)`
    - 参数
      - 等待时间，单位ms
- 长按操作
  - 方法
    - `TouchAction(driver).long_press(e1=None, x=None, y=None, duration=1000).perform()`
    - 参数
      - 元素(el)或坐标(x, y)
      - 持续时间duration，单位ms
- 移动操作
  - 方法
    - `TouchAction(driver).move_to(el=None, x=None, y=None).perform`
    - 参数：元素(el)或坐标(x, y)

## 手机操作API
- 获取手机分辨率
  - `driver.get_window_size()`
- 获取手机截图
  - `driver.get_screenshot_as_file("filepath")`
- 获取和设置网络状态
  - 获取手机网络
    - `driver.network_connection`
  - 设置手机网络
    - `driver.set_network_connection(connectionType)`
- 发送键到设备
  - `driver.press_keycode(keycode, metastate=None)`
  - android_keycode
    - http://www.temblast.com/ref/akeyscode.htm
- 打开和关闭通知栏
  - 打开通知栏
    - `driver.open_notifications()`
  - 关闭通知栏
    - 使用返回键
      - press_keycode(4)