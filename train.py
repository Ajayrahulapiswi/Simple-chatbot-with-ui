from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
def setup():
 bot = ChatBot('Bot')
 trainer = ChatterBotCorpusTrainer(bot)
 trainer.train("chatterbot.corpus.english")
setup()