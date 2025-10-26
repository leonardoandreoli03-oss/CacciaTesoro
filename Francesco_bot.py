from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8359474020:AAEUf5ahCrTbRZXRTv0_pQkgw4Vs-t4knKA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao, mi avevano avvertito che mi avresti scritto.")
    await context.bot.send_voice(chat_id=update.effective_chat.id, voice=open("audio/francesco.ogg", "rb"))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="🕯️ Ora devo andare, non so altro, buona fortuna",
                                   reply_markup=None)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot di Laurea attivo")
app.run_polling()
