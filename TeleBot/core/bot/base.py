"""
{{datetime}}
Auto generated script with TeleBot
Version: {{version}}
Base file for all handlers
"""
import json
from abc import ABC, abstractmethod
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext


class Base(ABC):
    """
    Abstract class for handlers
    NAME: name of command Eg. 'start' in bot /start
    DESC: set description for command in bot
    """
    NAME = None
    DESC = None

    def __init__(self, debug_mode=False):
        """
        Initializing all variables
        """
        self.update = None
        self.context = None
        self.debug_mode = debug_mode

    def __call__(self, update: Update, context: CallbackContext):
        self.update = update
        self.context = context
        if self.debug_mode:
            self.debug()
        return self.run()

    @abstractmethod
    def run(self):
        """
        This is the main function to put the logic, Called by __init__
        :return:
        """

    def debug(self):
        """
        This class is for printing/sending debug info
        :return:
        """
        debug_text = json.dumps(self.update, indent=4)
        print(f"BOT debug_mode: \n{debug_text}")
