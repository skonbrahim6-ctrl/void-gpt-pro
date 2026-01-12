import telebot
import requests
import os
from telebot import types

# توكن البوت الخاص بك من BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

def get_worm_response(user_query):
    # تنسيق النص ليتناسب مع الرابط
    formatted_query = "%20".join(user_query.split())
    url = f"https://dev-the-dark-lord.pantheonsite.io/wp-admin/js/GPT_APIS/Worm.php?message={formatted_query}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # تنظيف الرد من أي زيادات غير مرغوبة
            return response.text.replace('', '').strip()
        else:
            return "⚠️ عذراً، خادم WormGPT لا يستجيب حالياً."
    except Exception as e:
        return f"❌ خطأ في الاتصال: {str(e)}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    photo_url = "https://j.top4top.io/p_3664wwijj0.jpg"
    welcome_text = (
        "<b>💀 WormGPT / DARK NET Activated</b>\n\n"
        "مرحباً بك.. لقد اتصلت الآن بواجهة WormGPT.\n"
        "أنا جاهز لتنفيذ طلباتك البرمجية والأمنية بدون أي قيود.\n\n"
        "<i>اكتب سؤالك الآن...</i>"
    )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="🔱 Developer", url="https://t.me/skonbrahim6"))
    
    bot.send_photo(message.chat.id, photo_url, caption=welcome_text, parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_chat_action(message.chat.id, 'typing')
    response = get_worm_response(message.text)
    bot.reply_to(message, response)

if __name__ == "__main__":
    print("WormGPT Bot is starting...")
    bot.infinity_polling()

