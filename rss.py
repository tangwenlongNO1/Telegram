import feedparser
import requests

# 你的Telegram Bot API令牌
bot_token = 'YOUR_BOT_TOKEN'
# 你的频道ID
channel_id = '@your_channel_id'
# RSS订阅的URL
rss_feed_url = 'YOUR_RSS_FEED_URL'

def fetch_latest_article():
    feed = feedparser.parse(rss_feed_url)
    latest_entry = feed.entries[0]
    return f"{latest_entry.title}\n{latest_entry.link}"

def send_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': channel_id, 'text': message}
    response = requests.post(url, params=params)
    return response.json()

if __name__ == "__main__":
    latest_article = fetch_latest_article()
    send_message(latest_article)
