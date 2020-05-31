from googletrans import Translator
translator = Translator()
def translate(word):
    return translator.translate(word).text
