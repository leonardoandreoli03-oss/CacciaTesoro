from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8312475415:AAG0dUANuji60XvHiSNO4m8YeLgMOX8-Yaw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Non parlo con i poliziotti.")
    
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("GabrieleBot avviato")
app.run_polling()
