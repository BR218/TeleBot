"""
{{datetime}}
Auto generated script with TeleBot
Version: {{version}}
Added help class here
"""
from TeleBot.core.bot.base import Base


class Help(Base):
    """
    Help menu created
    """
    NAME = 'help'
    DESC = 'Print the help text'
    TEXT = None

    def run(self):
        """
        Rest of the logic for help applied in bot
        """
        self.update.message.reply_text(self.TEXT)
