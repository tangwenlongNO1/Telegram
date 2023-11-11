import feedparser
import requests
import os

# 你的Telegram Bot API令牌
telegram_bot_token = os.environ.get('TG_TOKEN')
telegram_chat_id = os.environ.get('TG_CHAT_ID')
# RSS订阅的URL
rss_feed_url = 'https://rsshub.app/3dmgame/news'

def fetch_latest_article():
    feed = feedparser.parse(rss_feed_url)
    latest_entry = feed.entries[0]
    return f"{latest_entry.title}\n{latest_entry.link}"

def send_message(message):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    params = {'chat_id': telegram_chat_id, 'text': message}
    response = requests.post(url, params=params)
    return response.json()

if __name__ == "__main__":
    latest_article = fetch_latest_article()
    send_message(latest_article)
