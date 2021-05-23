import telepot
from handle_msg import handle
from telepot.loop import MessageLoop
from time import sleep
import os

os.system("cls")

with open("secrets\\api_token.txt", 'r', encoding='utf-8') as token:
    api_token = token.readline()

   
bot = telepot.Bot(api_token)
MessageLoop(bot, handle).run_as_thread()
print("Bot iniciado com sucesso!")

print ('Listening....')
while 1:
    sleep(10)