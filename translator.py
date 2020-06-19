from translate import Translator

translator = Translator(to_lang="ru")
with open(r'C:\Users\Asus\Documents\Python\python\myname.txt', mode='r') as my_file:
  text = my_file.read()
translation = translator.translate(text)
with open (r'C:\Users\Asus\Documents\Python\python\myname2.txt', mode='w') as my_file2:
    my_file2.write(translation)