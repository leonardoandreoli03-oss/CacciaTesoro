from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8278198610:AAGw8QrGjv7nX4AnNTEPirVwCCwCIg-nnDc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Il mio finale, del mio gioco, ci siamo quasi.")
    await context.bot.send_voice(chat_id=update.effective_chat.id, voice=open("audio/Chris.ogg", "rb"))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Preparatevi a  guardare oltre il regno dei morti.",
                                   parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("GabrieleBot avviato")
app.run_polling()