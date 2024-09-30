import telebot
import random
from io import BytesIO
from PIL import Image, ImageDraw
from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Токен вашего бота
TOKEN = '7583065372:AAEUdSD4RndpP1-n28otgJ7yQwAdeQunWYA'

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Бросить монетку", callback_data='flip')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Нажми кнопку ниже, чтобы бросить монетку.', reply_markup=reply_markup)

def flip_coin(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Создаем анимацию броска монетки
    query.edit_message_text(text="Бросаю монетку...")

    # Создаем изображения для анимации
    '''images = []
    for _ in range(1):
        img = Image.new('RGB', (200, 200), color='yellow')
        d = ImageDraw.Draw(img)
        d.text((160, 90), 'Бросок...', fill='black')
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)
        images.append(img_io)

    # Отправляем кадры анимации
    for img_io in images:
        context.bot.send_photo(chat_id=query.message.chat_id, photo=InputFile(img_io, filename='coin_flip.png'))'''

    # Определяем результат броска
    result = random.choice(['Орёл', 'Решка'])
    query.message.reply_text(f'Результат: {result}')

def main() -> None:
    updater = Updater("7583065372:AAEUdSD4RndpP1-n28otgJ7yQwAdeQunWYA")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(flip_coin, pattern='flip'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()