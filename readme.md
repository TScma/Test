# GitHub 
[Git下载](https://git-scm.com/downloads)
## 远程连接
* 设置用户名
```
git config --global user.name ''
```

* 设置邮箱
```
git config --global user.email ''
```
* 初始化Git仓库
```
git init
```
* 连接到远程库
```
git remote add origin git@github.com:account/name.git
```
----------------------------------------
## 文件操作
1. 创建文件
```
touch HelloGitHub.py
```
2. 添加到暂存区
```
git add HelloGitHub.py
```
3. 从暂存区提交到仓库
```
git commit -m 'submit HelloGitHub'
```
4. 第一次提交到GitHub仓库
```
git push -u origin master
```
5. 再次提交
```
git push origin master
```
6. 删除文件
```
git rm HelloGitHub.py
```
> 跳到3,4,5
## tables
