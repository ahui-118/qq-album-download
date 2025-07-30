import os
from github import Github

# ✅ 请替换为你自己的 GitHub Token
GITHUB_TOKEN = "ghp_your_token_here"  # ← 你需要手动替换为自己的有效 Token

# 📦 ZIP 文件名自动基于 QQ 号
QQ_NUMBER = "75333521"
ZIP_FILE = f"{QQ_NUMBER}_album.zip"
REPO_NAME = f"qq-album-{QQ_NUMBER}"

def upload_to_github():
    if not os.path.exists(ZIP_FILE):
        print(f"❌ 未找到文件: {ZIP_FILE}")
        return

    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    try:
        repo = user.create_repo(REPO_NAME, private=False)
    except Exception as e:
        print(f"⚠️ 仓库创建失败，尝试获取已有仓库: {e}")
        repo = g.get_user().get_repo(REPO_NAME)

    with open(ZIP_FILE, "rb") as f:
        content = f.read()

    try:
        repo.create_file(ZIP_FILE, "initial commit", content)
        print(f"✅ 上传成功！地址：https://github.com/{user.login}/{REPO_NAME}")
    except Exception as e:
        print(f"⚠️ 上传失败: {e}")

if __name__ == "__main__":
    upload_to_github()
