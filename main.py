from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ContextTypes, ApplicationBuilder
import sys
TOKEN = sys.argv[1]  # 用你自己的 bot token 替换掉 'TOKEN'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="start notification！")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/start 开始消息推送\n/help 查看帮助")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    application = ApplicationBuilder().token('6255056539:AAGiplqI0cbCx5m2wOtn1niq_LDL7eihD-k').build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)
    application.run_polling()
