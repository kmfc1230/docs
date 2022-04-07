参考地址：https://developer.android.google.cn/studio?hl=zh-cn

常用adb命令：  
1、通过IP地址连接到设备  
`adb connect device_ip:5555`  
2、查看设备  
`adb devices`  
3、启动或停止server  
`adb kill-server`  
`adb start-kill`  
4、安装/卸载apk  
`adb install path_to_apk`  
`adb uninstall apk_name`  
5、从设备中复制文件到本地  
`adb pull remote local`  
6、从本地负责文件到设备中  
`adb push local remote`  
7、发出adb命令  
`adb [-d | -e | -s serial_number] command`  
8、发出shell命令  
`adb [-d |-e | -s serial_number] shell shell_command`  
9、启动交互式shell  
`adb [-d | -e | -s serial_number] shell`  
10、调用activity管理器（am）  
`adb shell am start -a android.intent.action.VIEW`  
11、调用软件包管理器（pm）  
`adb shell pm uninstall com.example.MyApp`  
12、调用政策管理器（dpm） 
`adb shell dpm command`  
13、截屏  
`adb shell screencap /sdcard/screen.png`  
14、录屏  
`adb shell screenrecord /sdcard/demo.mp4`  
15、获取apk包名  
`adb -s serial_number shell dumpsys window w | findstr \/ | findstr name=`  
