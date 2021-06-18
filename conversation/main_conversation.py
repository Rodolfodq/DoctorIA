from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


my_bot = ChatBot(name='Dr. IA')

def configure_conversation(my_bot):   

    small_talk = [
        'Olá',
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
        'Que bom ouvir isso',
        'Estou mal',
        'Sinto muito, como posso te ajudar?'
    ]

    sintomas1 = [
        'Estou com gripe',
        'Quais são seus sintomas?',
        'Estou com febre',
        'Você pode realizar uma compressa fria com um pano úmido na sua testa',
        'Estou com coriza',
        'Você pode fazer uma lavagem com soro nazal',
        'Estou com dor de garganta',
        'Recomendo que você tome uma colher de mel natural para aliviar a dor',
        'Estou com todos os sintomas de gripe',
        'Recomendo que você procure um médico'
    ]

    sintomas2 = [
        'Estou com a uma crise de ansidade',
        'A psicoterapia ou acompanhamento psicológico pode ajudar numa melhor compreensão do problema e na forma como este é encarado.',
        'Estou com ansiedade',
        'Procure se acalmar e caso os sintomas persistam, procure ajuda médica.'
    ]

    sintomas3 = [
        'Estou com enxaqueca',
        'A enxaqueca possui tratamento. Um médico neurologista poderia te ajudar.',
        'Minha dor de cabeça não passa' 
        'A enxaqueca pode ser previnida com hábitos saudáveis. Procure orientação médica e siga as orientações',
        'Estou com dor de cabeça muito forte',
        'Este é um sintoma de enxaqueca. Você deveria procurar a orientação de um médico especialista.'
    ]

    sintomas4 = [
        'Estou com insonia',
        'A insônia pode ser causada por estresse, depressão, ansiedade, dentre outras. A orientação médica pode te ajudar a identificar a causa da sua insônia.',
        'Não consigo dormir',
        'A dificuldade para pegar no sono pode ser causada pela falta de uma rotina de sono, cafeína, nicotina, álcool. Você deveria evitar estes maus habitos.'
    ]

    sintomas5 = [
        'Estou com sinusite',
        'Quando se avalia a sinusite pelas suas causas, ela pode ser conhecida como sinusite viral, se for provocada por vírus; como sinusite bacteriana, se for causada por bactérias, ou como sinusite alérgica, se for causada por uma alergia.',
        'Como trato minha sinusite?',
        'O tratamento para sinusite geralmente é feito com o uso de remédios como: Sprays nasais, Remédios antigripais ou Antibióticos orais. Todas medicações devem ser prescristas por um médico.'
    ]

    agendar = [
        'Quero agendar uma consulta',
        'Para agendar uma consulta, envie /agendar.',
        'Agendar consulta',
        'Para agendar uma consulta, envie /agendar.'

    ]

    list_trainer = ListTrainer(my_bot)

    for item in (small_talk, sintomas1, sintomas2, sintomas3, sintomas4, sintomas5, agendar):
        list_trainer.train(item)

    #corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    #corpus_trainer.train('chatterbot.corpus.portuguese')

def start_conversation(phrase):
    try:        
        response = my_bot.get_response(phrase)        
        return response
    except:
        return "Não consegui encontrar uma resposta para isso."
    
