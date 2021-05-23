import conversation.main_conversation
import telegram_chat.main_telegram
from chatterbot import ChatBot
import os

my_bot = ChatBot(name='Dr. IA')

try:
    conversation.main_conversation.configure_conversation(my_bot)
    os.system('clear')
    print('Configuração da conversa iniciada com sucesso.')
except:
    print('Erro ao iniciar configuração da conversa.')


try:
    telegram_chat.main_telegram.start_bot()
    print("Bot iniciado com sucesso.")
except (KeyboardInterrupt):
    print("Bot encerrado com sucesso.")
