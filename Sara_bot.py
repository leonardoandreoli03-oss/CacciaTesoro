from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8347359967:AAGSTEg1zfxfSyB4Fo0ShXiuIO88S4lphk4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao... come hai avuto il mio numero?")
    await context.bot.send_voice(chat_id=update.effective_chat.id, voice=open("audio/sara.ogg", "rb"))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Senti Francesco,forse sa qualcosa in più.",
                                   parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
