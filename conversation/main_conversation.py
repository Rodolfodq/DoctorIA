from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='Dr. IA', read_only=True)

small_talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m pybot. ask me a math question, please.']

list_trainer = ListTrainer(my_bot)

for item in (small_talk):
    list_trainer.train(item)

while True:
    phrase = input("Você: ")
    my_bot.get_response(phrase)