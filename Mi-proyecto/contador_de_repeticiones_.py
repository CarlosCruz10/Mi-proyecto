string_usuario = input("Di algo: ")
abecedario = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m"]
palabras = []
apariciones_palabras = dict()
word = ""
numero_apariciones = 0
index = 0
indice_actual = len(string_usuario)

while not index > indice_actual:
    for letter in string_usuario:
        if letter in abecedario:
            word += letter
            index += 1
        elif not letter in abecedario:
            palabras.append(word)
            word = ""


for word in palabras:
    if word in apariciones_palabras:
        numero_apariciones += 1
        apariciones_palabras[word] = numero_apariciones
    else:
        numero_apariciones = 1
        apariciones_palabras[word] = numero_apariciones


print(apariciones_palabras)