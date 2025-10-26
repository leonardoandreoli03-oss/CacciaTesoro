from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8326130023:AAHtqxpdyxjoaX9raz2dXqkBnPjwte1Thqo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👩‍🦰 Ciao sono Laura. Miriam mi aveva avvisato che qualcuno mi avrebbe contattato in caso fosse scomparsa.")
    await context.bot.send_voice(chat_id=update.effective_chat.id, voice=open("audio/laura.ogg", "rb"))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="È tutto, buona fortuna.",
                                   reply_markup=None)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot di Laurea attivo")
app.run_polling()
