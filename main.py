from flask import Flask, request
import telegram

app = Flask(__name__)

TOKEN = "7902964725:AAFqOlXAQLabw3d8jWjs8TULRlFsYOMtBjY"
bot = telegram.Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # هنا ترد على رسالة المستخدم
    bot.send_message(chat_id=chat_id, text=f"استلمت رسالتك: {text}")
    return 'OK'

@app.route('/')
def index():
    return "بوت شغال"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
