from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8115280459:AAHlp3XSwXeI_zuIqS9rP_uJionyCqWgVSk"

# Custom footer to add to each video
APPENDED_HTML = """
\n\n🎓 Join Our Free Course Community 🎓

📲 <a href="https://t.me/PremiumCourse7765">Telegram Channel</a>
📱 <a href="https://whatsapp.com/channel/0029Vai3cmf2v1IvBuU6l21s">WhatsApp Channel</a>
🌐 <a href="https://www.paidcourse-infree.store/">Visit Our Website</a>

🔖 Contact: @yourusername
"""

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        original_caption = update.message.caption or ""
        new_caption = original_caption + APPENDED_HTML

        # Forward video
        await update.message.forward(chat_id=update.effective_chat.id)

        # Edit caption of forwarded message
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id,
            message_id=update.message.message_id + 1,
            caption=new_caption,
            parse_mode=ParseMode.HTML
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

print("Bot is running...")
app.run_polling()
