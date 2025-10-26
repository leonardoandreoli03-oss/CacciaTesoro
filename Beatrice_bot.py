from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8407382962:AAHccYBciUm8yEiIyHXc8J5_g9d14yuRFxs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Non ti conosco, non ti dirò nulla.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot di Laurea attivo")
app.run_polling()
