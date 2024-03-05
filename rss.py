import feedparser
import requests
import os
from bs4 import BeautifulSoup
import random

# 你的Telegram Bot API令牌
telegram_bot_token = os.environ.get('TG_TOKEN')
telegram_chat_id = os.environ.get('TG_CHAT_ID')
# RSS订阅的URL
rss_feed_url = 'https://www.141jav.com/feeds/'
rss_feed_url1 = 'https://rsshub.app/1x/latest'
rss_feed_url2 = 'https://rsshub.app/wallhaven/search/q=black+silk&categories=001&purity=010&sorting=relevance&order=desc&ai_art_filter=1'

def fetch_latest_items():
    feed = feedparser.parse(rss_feed_url2)
    latest_entry = feed.entries[random.randint(0, len(feed.entries) - 1)]
    soup = BeautifulSoup(latest_entry.description, 'html.parser')
    first_image = soup.find_all('img')

    
    
    # 获取第一张图片链接
    image_urls = [img['src'] for img in first_image]
    
    # 随机选择一张图片链接
    if image_urls:
        random_image_url = random.choice(image_urls)
        print(random_image_url)
        return random_image_url
    else:
        return None
    # return f"{latest_entry.description[10:-4]}"

def send_message(message):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendPhoto'
    params = {'chat_id': telegram_chat_id, 'photo': message}
    response = requests.post(url, params=params)
    # print(response.json())
    # print(response.status_code)
    return response.json()

# def fetch_latest_items():
#     feed = feedparser.parse(rss_feed_url)
#     items = feed.entries[:3]
#     return items

# def send_message(items):
#     message = ""
#     for item in items:
#         item_title = item.title
#         item_link = item.link
#         item_description = item.description # if hasattr(item, 'description') else ""
        
#         # 将每个项的标题、链接和描述添加到消息中
#         message += f"*{item_title}*\n\n🧩 {item_description}\n[Read more]({item_link})\n\n"

#     # 发送合并的消息
#     url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
#     params = {'chat_id': telegram_chat_id, 'text': message, 'parse_mode': 'Markdown', 'disable_web_page_preview': False}
#     response = requests.post(url, params=params)
#     return response.json()

if __name__ == "__main__":
    latest_article = fetch_latest_items()
    print(latest_article)
    send_message(latest_article)
