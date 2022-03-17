#Calculo del area debajo de la curva
#Suma de Riemann
#Escritura y creación de fichero.


areas = open('areas.txt','w')
#intervalo de [2,5]
#f=((x **(1/2) ) + 1 ) 

for i in range (1,5001):
    area = 0
    dx = 3/i
    
    for k in range (0,i):
        x = 2 + ( dx * k )
        ancho = dx
        alto = (x**0.5) + 1
        
        area= area + ( ancho * alto)
    
    print(f'{i} {area:.4f}  \n')
    areas.write(f'{i} {area:.4f}  \n')
areas.close()




    



    