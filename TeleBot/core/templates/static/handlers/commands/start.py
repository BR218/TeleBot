"""
Start command to initialize convertiation with bot.
This is the defult command when you start chat with bot
"""
from TeleBot.core.bot.base import Base


class Start(Base):
    """
    Start convertiation class
    """
    NAME = 'start'
    DESC = 'Start convertiation with bot'

    def run(self):
        """
        Logic for/of bot start command
        """
        text = f"Hello, Welcome to the {{bot_name}}\n" \
               f"Please write /help to see the commands available."
        self.update.message.reply_text(text)
