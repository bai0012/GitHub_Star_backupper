# GitHub_Star_backupper

在本地计算机上轻松克隆你在GitHub上Star的仓库

## 程序截图
![](https://github.com/bai0012/GitHub_Star_backupper/demo.png)


## 如何使用

### 使用源代码程序

首先安装python，已在python3.10.11上测试

拉取该repo，并且安装Python依赖项：

```git
git clone https://github.com/bai0012/GitHub_Star_backupper
```

```Powershell
cd GitHub_Star_backupper
```

```python
pip install -r requirements.txt 
```
修改main.py中Github用户名和个人访问令牌及目标地址

如：

```python
# 在这里输入你的Github用户名和个人访问令牌（Personal Access Token）
username = "bai0012"
token = "github_pat_11AMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# 指定下载路径,请使用双斜线而不是斜线
download_path = "D://github"

```


使终端处于项目文件夹的基础上，运行

```Powershell
python main.py
```

等待处理完成。

若需要更新所有储存库，只需要再运行一次即可。


(本程序在GPT 4指导下完成)
