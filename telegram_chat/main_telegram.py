import telepot
from telepot.loop import MessageLoop
from time import sleep
import conversation
from secrets_token import api_token


bot = telepot.Bot(api_token.token)

def start_bot():
    bot = telepot.Bot(api_token.token)
    MessageLoop(bot, handle).run_as_thread()
    print("Bot iniciado com sucesso!")

    print ('Listening....')
    while 1:
        sleep(10)

def handle(msg):
    try:        
        message = msg['text']
        id_user = msg['chat']['id']        
        response = conversation.main_conversation.start_conversation(message)
        print(response)    
        bot.sendMessage(id_user, str(response))
    except:
        print('Algo deu errado!')