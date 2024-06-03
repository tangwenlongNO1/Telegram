import feedparser
import requests
import os
from bs4 import BeautifulSoup
import random
from io import BytesIO
from PIL import Image

# 你的Telegram Bot API令牌
telegram_bot_token = os.environ.get('TG_TOKEN')
telegram_chat_id = os.environ.get('TG_CHAT_ID')
# RSS订阅的URL

rss_feed_url2 = "https://rsshub.app/2048/27"

def fetch_latest_items():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    feed = feedparser.parse(rss_feed_url2, request_headers=headers)
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
    print(response.json())
    print(response.status_code)
    return response.json()

if __name__ == "__main__":
    latest_article = fetch_latest_items()
    print(latest_article)
    send_message(latest_article)
