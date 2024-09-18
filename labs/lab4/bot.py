import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

load_dotenv()

async def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data='1'),
            InlineKeyboardButton("Кнопка 2", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Кнопка 3", callback_data='3'),
            InlineKeyboardButton("Кнопка 4", callback_data='4'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

async def button(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Вы нажали кнопку: {query.data}")

def main():
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    
    application.run_polling()

if __name__ == '__main__':
    main()
