import telebot
import sqlite3
import time
from datetime import datetime, timedelta
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8944104317:AAGmrrhy1itDy3H-n9643jPLHz3zhNab4NQ"
bot = telebot.TeleBot(TOKEN)

# ========== БАЗА ДАННЫХ ==========
def init_db():
    conn = sqlite3.connect('imperia.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            login TEXT UNIQUE,
            nickname TEXT,
            status TEXT DEFAULT 'user',
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ========== ПРИВЕТСТВИЕ ==========
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    btn_register = InlineKeyboardButton("📝 Зарегистрироваться", callback_data="register")
    btn_guest = InlineKeyboardButton("👁 Гостевой доступ", callback_data="guest")
    markup.add(btn_register, btn_guest)
    
    bot.send_message(message.chat.id, 
        "Приветствую, гражданин! Добро пожаловать в IMPERNET — зону заботы Империи.\n\nВыберите режим доступа:",
        reply_markup=markup)

# ========== ОБРАБОТЧИКИ КНОПОК ==========
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "register":
        bot.send_message(call.message.chat.id, "✅ В разработке: регистрация скоро появится.")
    elif call.data == "guest":
        bot.send_message(call.message.chat.id, "👁 Гостевой режим в разработке.")
    bot.answer_callback_query(call.id)

# ========== ЗАПУСК ==========
if __name__ == "__main__":
    print("Бот запущен")
    bot.infinity_polling()
