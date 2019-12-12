from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def get_response(usr):
 bot = ChatBot('Bot',storage_adapter='chatterbot.storage.SQLStorageAdapter',
 logic_adapter=[
     {
         'import path':'chatterbot.logic.BestMatch'
     },
     {
         'import path':'chatterbot.logic.LowConfidenceAdapter',
         'threshold':0.70,
         'default_response':'I am sorry'
     }
 ]
 )
 trainer = ChatterBotCorpusTrainer(bot)
 #trainer.train("chatterbot.corpus.english")
 while True:
     if usr.strip()!='bye':
         result=bot.get_response(usr)
         reply=str(result)
         return(reply)
     if usr.strip()=='bye':
         return('bye')
         break

