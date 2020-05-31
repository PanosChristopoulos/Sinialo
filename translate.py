from googletrans import Translator
translator = Translator()
def translate(word):
    print(translator.translate(word).text)

translate("athina")