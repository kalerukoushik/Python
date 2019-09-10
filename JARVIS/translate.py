from googletrans import Translator
translator = Translator()
text = input()
to_lang = input()
after = translator.translate(text, dest=to_lang)
print("This is "+ after.src +" language")
print("It says:" +after.text)
