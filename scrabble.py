#Scrabble Juego
puntuaciones = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'L': 1,
    'M': 3,
    'N': 1,
    'Ñ': 8,
    'O': 1,
    'P': 3,
    'Q': 5,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'X': 8,
    'Y': 4,
    'Z': 10,
}
cond = True
puntuacion= 0
while cond is True:

    palabra = input('Introduce la palabra: ')

    if len(palabra) > 7:
        print('Ha ocurrido un error, la palabra no puede tener más de   7 carácteres\n')
    elif 'K'  in palabra is True or 'W' in palabra is True or palabra.isalpha() is False or palabra.isspace is True or palabra.isupper is False:
        print('Ha ocurrido un error, solo se admiten letras mayusculas sin incluir la K ni la W.\n ')
    else:
        cond = False #no vuelvas a preguntar por la palabra
for i in palabra:
    puntuacion= puntuacion + puntuaciones[i]
    print(i, 'es igual a:', puntuaciones[i])


print(f'Por jugar la palabra {palabra} has obtenido una puntuacion es de {puntuacion} puntos')