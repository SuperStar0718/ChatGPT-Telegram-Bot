from telegram import ChatAction
from telegram.ext import Updater, CommandHandler

def get_chat_history(update, context):
    # Send a "typing" status to the user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    
    # Get the chat history
    chat_history = context.bot.get_chat_history(chat_id=update.message.chat_id, limit=100)
    
    # Loop through the chat messsages and print them
    for message in chat_history:
        message_text = message.text if message.text else '<No text message>'
        print(f'{message_text} - sent by {message.from_user.username} at {message.date}')
    
# Set up the Telegram bot with a command handler for the "getchathistory" command
updater = Updater('YOUR_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher
get_chat_history_handler = CommandHandler('getchathistory', get_chat_history)
dispatcher.add_handler(get_chat_history_handler)

# Start the bot
updater.start_polling()
updater.idle()
