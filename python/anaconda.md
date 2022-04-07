# **anaconda3**
# 安装
- 官网下载：https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
- 终端执行：
```sh
bash Anaconda3-2021.11-Linux-x86_64.sh
# 敲回车，遇到询问yes/no，输入yes
```
- 环境变量：
```sh
vim ~/.bashrc
# 末尾加上
export PATH=$PATH:/home/hs/anaconda3/bin
```
# 常用命令
```sh
# 列出当前anaconda的配置信息
conda info
# 列出所有虚拟环境
conda env list # 也可以用 conda info -e
# 激活虚拟环境
source activate base
source deactivate
# 创建虚拟环境
conda create -n env_name python=version
# 克隆虚拟环境
conda create -n new_env --clone old_env
# 卸载虚拟环境
conda remove -n env_name --all
# 切换虚拟环境
conda activate env
conda deactivate
# 导出requirements.txt
pip freeze > requirements.ext
# 还原requirements.txt,先下载所有包然后再安装
pip install -r requirments.txt
# 卸载requirments.txt安装的插件
pip uninstall -r requirments.txt
```
# 练习：创建虚拟环境djdemo
```sh
# 创建djdemo
conda create -n djdemo
conda activate djdemo
# 安装django
pip install django
# 创建django项目
django-admin startproject demo
# 创建应用
python manager.py startapp App
```