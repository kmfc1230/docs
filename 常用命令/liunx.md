# Linux命令大全
- 参考资料：https://www.runoob.com/linux/linux-command-manual.html
## 文件管理
|命令|说明|
|---|---|
|cat|连接文件并打印到标准输出设备上|
|chattr||
|chgrp||
|chmod||
|chown||
|cksum||
|cmp||
|diff||
|diffstat||
|file||
|find||
|git||
|gitview||
|indent||
|cut||
|ln||
|less||
|locate||
|lsattr||
|mattrib||
|mc||
|mdel||
|mdir||
|mktemp||
|more||
|mmove||
|mread||
|mren||
|mtools||
|mtoolstest||
|mv||
|od||
|paste||
|patch||
|rcp||
|rm||
|slocate||
|split||
|tee||
|tmpwatch||
|touch||
|umask||
|which||
|cp||
|whereis||
|mcopy||
|mshowfat||
|rhmask||
|scp||
|awk||
|read||
|updatedb||
## 文件编辑
|命令|说明|
|---|---|
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||
|||

```shell
# dpkg
# 安装
sudo dpkg -i xx.deb
# 查询包名方便卸载
sudo dpkg -l 'xx'
# 卸载
sudo dpkg -r xx
# 卸载配置信息
sudo dpkg -P xx
```

sudo docker run --detach \
  --hostname localhost \
  --publish 10443:443 --publish 1080:80 --publish 1022:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ee:latest