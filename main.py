from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.environ['TOKEN']
CA = "iRfSifQQbhh2YsAKZwpp5AfzKJVja2CQ9ucKXYWpump"
DEX = f"https://dexscreener.com/solana/{CA}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*$67 IS SENDING*\n\n"
        f"CA: `{CA}`\n\n"
        "Use @Pummp67Bot raid for shill message",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("BUY $67", url=DEX)]])
    )

async def raid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "COPY & PASTE EVERYWHERE\n\n"
        "$67 $67 $67 LFG\n"
        "Still early — going 100×\n\n"
        f"CA: `{CA}`\n"
        f"Buy: {DEX}"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("raid", raid))
print("$67 BOT IS LIVE @Pummp67Bot")
app.run_polling()
