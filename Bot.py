#Dictionary app
word = input("Hola! Soy un bot de diccionario de palabras interesantes.¿Hay alguna palabra que no entiendes? \n")
word_dict = {
    "LOL":"una respuesta a algo gracioso";
    "CRINGE":"algo raro o embarazoso";
    "ROFL":"una respuesta a una broma";
    "SHEESH":"ligera desaprobación";
    "CREEPY":"aterrador, siniestro";
    "AGGRO":"ponerse agresivo o enojado"
}
if word in word_dict.keys():
    print("significa ",word_dict[word])
else:
    print("lo siento, no conozco esa palabra.")
