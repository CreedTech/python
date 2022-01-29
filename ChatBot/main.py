from urllib import request

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot('CreedBot', read_only=True,
                 logic_adapters=
                 ['chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.BestMatch'])

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


def get_bot_response():
    usertext = request.args.get('msg')
    return str(my_bot.get_response(usertext))


