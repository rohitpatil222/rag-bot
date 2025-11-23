import os
from telegram.ext import ApplicationBuilder, CommandHandler
from modules.rag import answer_query

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def ask(update, context):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Please type: /ask <your question>")
        return

    response = answer_query(query)
    await update.message.reply_text(response)


async def help_command(update, context):
    await update.message.reply_text("Use /ask <query> to get an answer.")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()   # <-- This avoids all asyncio loop issues


if __name__ == "__main__":
    main()
