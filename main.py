from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("مرحبا! أنا بوتك.")

app = ApplicationBuilder().token('').build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
