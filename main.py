import os
import requests
from dotenv import load_dotenv,set_key
from github import Github
load_dotenv()

g = Github(os.environ.get("token"))
repo_name = "Telegram"
username = "tangwenlongNO1"
repo = g.get_user(username).get_repo(repo_name)

# 获取当前最新版本的 Clash For Windows Chinese_patch 下载链接和更新日志
response = requests.get("https://api.github.com/repos/BoyceLig/Clash_Chinese_Patch/releases/latest")
print(response.status_code)
data = response.json()
latest_version = data['tag_name']
latest_download_url = data['assets'][0]['browser_download_url']
latest_changelog = data['body']
re = requests.get("https://api.github.com/repos/tangwenlongNO1/Telegram/contents/.env")
dt = re.json()
sha = dt['sha']

# 推送更新通知到 Telegram
telegram_bot_token = os.environ.get('TG_TOKEN')
telegram_chat_id = os.environ.get('TG_CHAT_ID')
current_version = os.getenv('version')
telegram_api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
if latest_version != current_version:

    message_text = f"🎉*Clash For Windows 汉化包 更新至 {latest_version}*\n{latest_download_url}\n[下载链接](https://github.com/BoyceLig/Clash_Chinese_Patch/releases/latest)"
    params = {
        "chat_id":telegram_chat_id,
        "text":message_text,
        "parse_mode":'Markdown',
        "disable_web_page_preview":True

    }
    response = requests.post(telegram_api_url, data=params)
    print(response.status_code)
    with open('.env', 'w') as f:
        f.write(f"version={latest_version}")
    with open('.env', 'r') as f:
        contents = f.read()
    repo.update_file(".env", "update .env", contents, sha, branch="master")
