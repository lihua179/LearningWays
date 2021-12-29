# -*- coding:utf-8 -*-
# @文件名  :mongodb.py
# @时间    :2021/12/29 15:17
# @作者    :jie
# @目的

# mongodb修改端口时的步骤:
# 1.进入mongodb文件夹bin文件:C:\Program Files\MongoDB\Server\5.0\bin
# 2.打开mongod.CFG文件，复制粘贴，在pycharm下创建同名文件，把内容复制粘贴
# 3.在21行的内容为:
# net:
#   port: 27017
# 修改为:
#   port: 27020
# 4.将C:\Program Files\MongoDB\Server\5.0\bin文件下的mongod.CFG删除，用新建的来替换
# 5.cmd cd C:\Program Files\MongoDB\Server\5.0\bin
# 6.mongod  --port 27020
# 7.重启电脑，完成修改
# 8.检查:mongo localhost:port ,返回:
# exception: Database name cannot have reserved characters for mongodb:// URL: mongodb://127.0.0.1:27017/localhost%3Aport
# exiting with code 1
# 修改成功


