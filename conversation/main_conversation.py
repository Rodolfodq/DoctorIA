from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


my_bot = ChatBot(name='Dr. IA')

def configure_conversation(my_bot):   

    small_talk = ['Olá',
        'Olá, tudo bem?',
        'Como vai?',
        'Vou bem e você?',
        'Bom dia',
        'Oi, bom dia',
        'Boa tarde',
        'Olá, boa tarde',
        'Boa noite',
        'Olá, boa noite',
        'Estou bem',
        'Que bom ouvir isso']

    sintomas1 = []    
    sintomas2 = []
    sintomas3 = []
    sintomas4 = []

    list_trainer = ListTrainer(my_bot)

    for item in (small_talk, sintomas1, sintomas2, sintomas3, sintomas4):
        list_trainer.train(item)

    corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    corpus_trainer.train('chatterbot.corpus.portuguese')

def start_conversation(phrase):
    try:        
        response = my_bot.get_response(phrase)        
        return response
    except:
        pass
    
