def scrabble(palabra,**vLetras):
    scrResult = 0
    for i in palabra:
        if i == 'T':
            print('La letra T no tiene puntuación asociada.')
        else: scrResult = vLetras[i] + scrResult
    return (f'La palabra {palabra}, tiene un valor de: {scrResult}')


print(scrabble("PYTHON", P=3, Y=4, H=4, O=1, N=2))