#Install translate library by Google Translater

from translate import Translator

Translator = Translator(to_lang='pt-br')

text = "Hi, how are you?"

Translation = Translator.translate(text)
print('translated Text:', Translation)