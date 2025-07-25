from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "ใส่โทเคนของบอทพี่ตรงนี้"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("สวัสดี! บอทของพี่มารายงานตัวแล้วครับ!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
