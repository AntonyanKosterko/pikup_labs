import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ConversationHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

STATE1, STATE2, STATE3 = range(3)

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Перейти в состояние 1", callback_data=str(STATE1))],
        [InlineKeyboardButton("Перейти в состояние 2", callback_data=str(STATE2))],
        [InlineKeyboardButton("Перейти в состояние 3", callback_data=str(STATE3))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите состояние:', reply_markup=reply_markup)
    return STATE1

async def state1(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    next_state = int(query.data)
    
    keyboard = [
        [InlineKeyboardButton("Перейти в состояние 2", callback_data=str(STATE2))],
        [InlineKeyboardButton("Перейти в состояние 3", callback_data=str(STATE3))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Вы в состоянии 1. Выберите следующее состояние:", reply_markup=reply_markup)
    
    return next_state

async def state2(update: Update, context):
    query = update.callback_query
    await query.answer()

    current_text = query.message.text
    new_text = "Вы в состоянии 2. Выберите следующее состояние:"

    if current_text != new_text:
        keyboard = [
            [InlineKeyboardButton("Перейти в состояние 1", callback_data=str(STATE1))],
            [InlineKeyboardButton("Перейти в состояние 3", callback_data=str(STATE3))],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=new_text, reply_markup=reply_markup)

    return STATE2


async def state3(update: Update, context):
    query = update.callback_query
    await query.answer()

    next_state = int(query.data)

    keyboard = [
        [InlineKeyboardButton("Перейти в состояние 1", callback_data=str(STATE1))],
        [InlineKeyboardButton("Перейти в состояние 2", callback_data=str(STATE2))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Вы в состоянии 3. Выберите следующее состояние:", reply_markup=reply_markup)
    
    return next_state


async def cancel(update: Update, context):
    await update.message.reply_text("Диалог завершен.")
    return ConversationHandler.END

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE1: [CallbackQueryHandler(state1)],
            STATE2: [CallbackQueryHandler(state2)],
            STATE3: [CallbackQueryHandler(state3)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
