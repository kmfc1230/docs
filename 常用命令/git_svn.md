# git
- 参考资料：https://www.runoob.com/git/git-tutorial.html

## git配置
- 参考资料：https://blog.csdn.net/qq_43768946/article/details/90411154
```shell
# 查看
git config --global --list
yourname
email@email.com

# 设置全局用户名和邮箱
git config --global user.name "yourname"
git config --global user.email "email@email.com"

# 生成rsa文件
# rsa文件位置：windows在目录/User/用户名/.ssh，ubuntu在目录~/.ssh
ssh-keygen -t rsa -C "email@email.com"
# 到rsa文件目录找到id_rsa.pub，将文件中内容添加到git仓库。
# 打开：settings-》SSH and GPG keys-》New SSH key
# 测试通不通
ssh -T git@github.com
```
## 初始化
```shell
git init
```
## 拉取代码
```shell
# 下载项目
git clone git@github.com:your_name/your_project.git
# 下载远程代码并合并
git pull origin master
```
## 推送代码
```shell
# 切换到项目目录
cd your_project
# 添加到本地仓库
git add .
# 提交
git commit -m "update"
# 推送到远程仓库
git push -u origin master
```


# svn
- 参考资料：https://www.runoob.com/svn/svn-tutorial.html
```shell
# 检出
svn checkout path --username=test  # path 是svn服务器上的目录,以用户test访问;checkout简写co
# 向本地版本库添加文件
svn add file        # .代表当前目录所有文件
# 查看工作副本中的状态，先切换到工作目录
svn status
# 提交文件
svn commit -m "update"
# 解决冲突，使用update，将服务器与本地合并
svn update
# 撤销文件修改
svn revert filename
# 回退版本?
svn merge
```