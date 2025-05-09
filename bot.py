from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")


BOT_TOKEN = "8115280459:AAHlp3XSwXeI_zuIqS9rP_uJionyCqWgVSk"  # Replace securely
BOT_TOKEN = "8115280459:AAHlp3XSwXeI_zuIqS9rP_uJionyCqWgVSk"

# Footer to append
APPENDED_HTML = """
\n\n🎓 Join Our Free Course Community 🎓

📲 <a href="https://t.me/PremiumCourse7765">Telegram Channel</a>
📱 <a href="https://whatsapp.com/channel/0029Vai3cmf2v1IvBuU6l21s">WhatsApp Channel</a>
🌐 <a href="https://www.paidcourse-infree.store/">Visit Our Website</a>

🔖 Contact: @Piyushyoutuber11
"""

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.video:
        video_file_id = update.message.video.file_id
        original_caption = update.message.caption or ""
        new_caption = original_caption + APPENDED_HTML

        # Re-send video with updated caption
        await update.message.reply_video(
            video=video_file_id,
            caption=new_caption,
            parse_mode=ParseMode.HTML
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

print("Bot is running...")
app.run_polling()
