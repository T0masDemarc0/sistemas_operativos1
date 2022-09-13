from ctypes.wintypes import PUSHORT
from pickle import TRUE
from re import A
'''
este programa funciona para saber el reintegro recibido con la billetera santa fe luego de una compra
 y si sos tan especial de poner una letra te putea
'''
importe = input("ingrese un importe: ")            #detecta el numero que sea puesto y es seleccionado como el valor de la variable
esnumero=importe.isnumeric()                       #isnumeric solo funca para que detecte numeros enteros, osea 2a te lo toma conmo numero pero a no
cantidad_de_Chances = 5
palabras_escritas = 0
bandera = False         

if esnumero:
    importe=float(importe)
while not(esnumero) :                                    #es un pequeño programa que se repite si no pones un numero
    if cantidad_de_Chances > palabras_escritas :
        print('no ingresaste un numero pelotudo')
        importe = input("ingrese un importe: ")
    palabras_escritas +=1                             #es lo mismo que palabras_escritas = palabras_escritas + 1
    esnumero=importe.isnumeric()                      
    if cantidad_de_Chances < palabras_escritas:       #acumulador que permite que tenga una cantidad e chances o que ponga una cantidad de numeros automatica
        print("te dije que pongas un numero idiota")
        bandera = True                                           #detecta si pusiste mas palabras aunque te pidio un numero
        break                                                    #cagaste tu chance por  poner demaciadas palabras idiota
    if esnumero:                                                 
        importe=float(importe)                                  #si detecta que pusiste un numero continuea con lo normal

if not(bandera) :
    porcentaje_descuento = 70
    importe_de_descuento = importe * porcentaje_descuento / 100                 #calcula cuanto seria el reintegro del 30%
    importe_con_reintegro = importe - importe_de_descuento   #calcula el 30% restando el total con el 70% y poniendolo en otra variable
    print("el reintegro es de: " ,importe_con_reintegro)                        #te dice cuanto te da e reintegro