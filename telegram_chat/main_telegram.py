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


flag_agenda = False
def handle(msg):
    if len(msg) == 6:
        comand = msg['text']        
        id_user = msg['chat']['id']
        name = msg['chat']['first_name']
        if comand == '/start':
            print(f"Olá, {name}. Eu sou o Doctor IA e posso te auxiliar no pré-atendimento médico.")
            bot.sendMessage(id_user, f"Olá, {name}. Eu sou o Doctor IA e posso te auxiliar no pré-atendimento médico.")
        elif comand == '/agendar':            
            bot.sendMessage(id_user, f"{name}, informe a data e hora para realizarmos seu agendamento.")
            global flag_agenda 
            flag_agenda = True
    elif len(msg) == 5:
        name = msg['chat']['first_name']
        id_user = msg['chat']['id']
        message = msg['text']        
        try:            
            if(flag_agenda):
                bot.sendMessage(id_user, f"Ok, {name}. Irei passar estas informações para a secretária do Dr. IA. Em breve você será notificado(a) sobre a confirmação da consulta no dia {message}.")
                flag_agenda = False
            else:                
                print(f"Usuário: {message}")                       
                response = conversation.main_conversation.start_conversation(message)
                print(f"Bot: {response}")    
                bot.sendMessage(id_user, str(response))
        except:
            print('Algo deu errado!')