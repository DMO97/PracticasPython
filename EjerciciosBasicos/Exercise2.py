cadena = "Escribe un programa que tome una cadena de texto y cuente el número de veces que aparece cada palabra en la cadena."

listapalabras = cadena.split()

frecuenciaPalbra = []

for i in listapalabras:
    frecuenciaPalbra.append(listapalabras.count(i))

print("Palabras: " + str(list(zip(listapalabras, frecuenciaPalbra))))


