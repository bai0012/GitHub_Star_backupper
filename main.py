import os
import subprocess
from github import Github

# 在这里输入你的Github用户名和个人访问令牌（Personal Access Token）
username = "your_username"
token = "your_personal_access_token"

# 指定下载路径,请使用双斜线而不是斜线
download_path = "your_download_path"

# 初始化Github对象
g = Github(token)

# 获取用户对象
user = g.get_user()

# 获取用户的所有star的仓库
starred_repos = user.get_starred()

# 如果下载路径不存在，则创建该路径
if not os.path.exists(download_path):
    os.makedirs(download_path)

# 更改当前工作目录到下载路径
os.chdir(download_path)

# 遍历每个star的仓库
for repo in starred_repos:
    repo_name = repo.name
    print("Processing repo:", repo_name)
    clone_url = repo.clone_url

    # 使用你的Github用户名和个人访问令牌来替换url中的用户名
    auth_clone_url = clone_url.replace("https://", f"https://{username}:{token}@")

    # 检查仓库是否已经存在于当前目录中
    if os.path.exists(repo_name):
        # 如果存在，执行git pull操作
        os.chdir(repo_name)
        subprocess.run(["git", "pull"])
        os.chdir("..")
    else:
        # 否则，执行git clone操作
        subprocess.run(["git", "clone", auth_clone_url])
