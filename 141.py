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

def fetch_latest_items():
    url2 = "https://bbs.kv8q4.com/2048/thread.php?fid=27"

    # 发送请求并获取页面内容
    response = requests.get(url2)
    html_content = response.text
    
    # print(html_content)
    
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, "html.parser")
    # print(soup)
    
    # 找到所有图片标签
    # img_tags = soup.find_all("img", class_="preview-img")
    
    read_links = soup.find_all("a", href=lambda href: href and href.startswith("read"))
    # print(read_links)
    
    # 输出找到的链接
    # for link in read_links:
    # print("https://bbs.kv8q4.com/2048/" + link["href"])
    link = read_links[15]
    url = "https://bbs.kv8q4.com/2048/" + link["href"]
    
    response = requests.get(url)
    html_content = response.text
    print(response.status_code)
    
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, "html.parser")
    
    # 找到所有图片标签
    img_tags = soup.find_all("img", class_="preview-img")
    # print(img_tags)
    # res = ""
    for i in range(len(img_tags)):
        response = requests.get(img_tags[i]["src"])
        image_content = response.content
        
        # 使用 PIL 打开图片
        image = Image.open(BytesIO(image_content))
        
        # 获取图片的宽度和高度
        image_width, image_height = image.size
        if image_width + image_height < 10000:
            res = img_tags[i]["src"]
            break
            
    
    return res


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
