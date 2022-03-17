#Calculadora de estatura por estadistica
#Calculo de desviasión tipica de un grupo de datos
#Uso de ficheros

estaturasTXT = open('Estaturas.txt','r') 

# listEst = estaturasTXT.readline()
# print(listEst)
# estaturasTXT.close()
estaturas=[]
for estatura in estaturasTXT:
    estaturas.append(float(estatura[:4]))
#print(estaturas)
print('la muestra tiene: ', len(estaturas), ' mediciones')
media=sum(estaturas)/len(estaturas)
print('La estatura mínima es de {0} metros. y la máxima es de {1} metros'.format(min(estaturas),max(estaturas)))


while True:
    estaturaIn= input('Introduce tu estatura: ')
    try:
        if  float(estaturaIn) < media:
            print('con una estatura de {0} metros, te encuentras por debajo de la media de {1:.3} metros'.format(estaturaIn, media))
            break
        elif float(estaturaIn) > media:
            print('con una estatura de {0} metros, te encuentras por encima de la media de {1:.3} metros'.format(estaturaIn, media))
            break
        else:
            print('con una estatura de {0} metros, te encuentras la media de {1:.23} metros'.format(estaturaIn, media))
            break
    except:
        print('Solo se permiten valores numéricos')

estaturasTXT.close()    
