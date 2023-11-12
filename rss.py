import feedparser
import requests
import os

# 你的Telegram Bot API令牌
telegram_bot_token = os.environ.get('TG_TOKEN')
telegram_chat_id = os.environ.get('TG_CHAT_ID')
# RSS订阅的URL
rss_feed_url = 'https://www.141jav.com/feeds/'

# def fetch_latest_article():
#     feed = feedparser.parse(rss_feed_url)
#     latest_entry = feed.entries[0]
#     return f"{latest_entry.title}\n{latest_entry.description}\n{latest_entry.link}"

# def send_message(message):
#     url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
#     params = {'chat_id': telegram_chat_id, 'text': message}
#     response = requests.post(url, params=params)
#     return response.json()

def fetch_latest_items():
    feed = feedparser.parse(rss_feed_url)
    items = feed.entries[:3]
    return items

def send_message(items):
    message = ""
    for item in items:
        item_title = item.title
        item_link = item.link
        item_description = item.description # if hasattr(item, 'description') else ""
        
        # 将每个项的标题、链接和描述添加到消息中
        message += f"*{item_title}*\n\n🧩 {item_description}\n[Read more]({item_link})\n\n"

    # 发送合并的消息
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    params = {'chat_id': telegram_chat_id, 'text': message, 'parse_mode': 'Markdown', 'disable_web_page_preview': False}
    response = requests.post(url, params=params)
    return response.json()

if __name__ == "__main__":
    latest_article = fetch_latest_items()
    send_message(latest_article)
