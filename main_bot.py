
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler,
    ContextTypes, filters
)

# TOKEN DEL BOT PRINCIPALE
TOKEN = "7503928125:AAHxmGu006sFuAn2j_T-qOjiyVhVCCIXCk8"

# CHIAVI
KEY1 = "halloween"
KEY2 = "betty"

# ✅ Gestione messaggi
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    # --- PRIMA KEY ---
    if text == KEY1:
        await update.message.reply_text(
            "🎃 Giusto... allora veramente mi è successo qualcosa.\n"
            "Giuri di essere qui per aiutarmi?",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Sì, lo giuro!", callback_data="giuro_si"),
                 InlineKeyboardButton("No...", callback_data="giuro_no")]
            ])
        )

    # --- SECONDA KEY ---
    elif text == KEY2:
        await update.message.reply_text(
            "🕯️ Mi posso fidare di te...\nEcco il numero di Chris, ma stai attento.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📞 Chiama Chris", url="https://t.me/ChrisHalloweenBot")]
            ])
        )

    else:
        await update.message.reply_text(
            "Non è questo il segnale che aspettavo... 💀\nProva a ricordare bene..."
        )

# ✅ Gestione pulsanti
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "giuro_si":
        await query.edit_message_text(
            "🕯️ Ok... qui avrai le mie *Chat*. 📒\n"
            "Ho nascosto degli indizi che *lui* non può capire...\n"
            "Sta a te arrivarci.\n\nTutto chiaro?",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Sì, tutto chiaro.", callback_data="chiaro_si")]
            ])
        )

    elif query.data == "giuro_no":
        await query.edit_message_text("💀 Allora non posso fidarmi di te...")

    elif query.data == "chiaro_si":
        await query.edit_message_text(
            "🔍 Ecco l'accesso alle chat con i miei amici più stretti:\n\n"
            "📞 *1.* Laura\n"
            "📞 *2.* Sara\n"
            "📞 *3.* Gabriele\n"
            "📞 *4.* Beatrice\n"
            "📞 *5.* Francesco\n\n"
            "_Spero che qualcuno possa essere d'aiuto..._ 👀\n\n"
            "🩸 Se non fossero d’aiuto i miei amici... provate a contattare direttamente *lui*.\n"
            "Per farlo, serve il nome della bambola che mi ha accompagnato per tutta la mia vita",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📞 Chiama Laura", url="https://t.me/LauraHalloweenBot")],
                [InlineKeyboardButton("📞 Chiama Sara", url="https://t.me/SaraHalloweenBot")],
                [InlineKeyboardButton("📞 Chiama Gabriele", url="https://t.me/GabrieleHalloweenBot")],
                [InlineKeyboardButton("📞 Chiama Beatrice", url="https://t.me/BeatriceHalloweenBot")],
                [InlineKeyboardButton("📞 Chiama Francesco", url="https://t.me/FrancescoHalloweenBot")]
            ])
        )

# ✅ /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕸️ Benvenuto... scrivi la parola chiave per iniziare il gioco."
    )

# MAIN
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(CallbackQueryHandler(button_callback))

print("🎃 Bot principale attivo!")
app.run_polling()
