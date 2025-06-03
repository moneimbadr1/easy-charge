from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("مرحبا! أنا بوتك.")

app = ApplicationBuilder().token('7902964725:AAFqOlXAQLabw3d8jWjs8TULRlFsYOMtBjY').build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
