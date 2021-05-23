import telepot

with open("secrets\\api_token.txt", 'r') as token:
    api_token = token.readline()


bot = telepot.Bot(api_token)

def handle(msg):      
    print(msg) 
    #bot.sendMessage(id_user, result)
    