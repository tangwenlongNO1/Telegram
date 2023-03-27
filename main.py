#########################
#####   tg机器人   ######
#########################
import logging

import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ContextTypes, ApplicationBuilder
import sys

# TOKEN = sys.argv[1]  # 用你自己的 bot token 替换掉 'TOKEN'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def weather():
    r = requests.get('http://www.weather.com.cn/data/sk/101250101.html')
    r.encoding = 'utf-8'
    # print(r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'])
    return r.json()['weatherinfo']['city'] + "今天天气" + r.json()['weatherinfo']['WD'] + "  温度" + r.json()['weatherinfo'][
        'temp']


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="start notification！")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/start 开始消息推送\n/help 查看帮助\n/weather 查看天气")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def getweather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=weather())


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    application = ApplicationBuilder().token('6255056539:AAGiplqI0cbCx5m2wOtn1niq_LDL7eihD-k').get_updates_http_version('1.1').http_version('1.1').build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    weather_handler = CommandHandler('weather', getweather)  # 命令写在过滤器上面
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(weather_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)
    application.run_polling()
