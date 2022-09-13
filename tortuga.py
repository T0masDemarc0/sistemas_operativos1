from pickle import FALSE, NONE, TRUE
import turtle

s = turtle.Screen()
t = turtle.Turtle()

inicio = input('pintamos? ')
probando = NONE
if inicio == 'no' :
    print('entonces para que mierda me iniciaste')
    exit()

"""
while probando != 'si' 'no' :
    if probando != 'si' :
       print('proba poner si o no')
       probando = input('queres que inicie?  ')
    if probando != 'no' :
       print('proba poner si o no')
       probando = input('queres que inicie?  ')
"""

while TRUE :
    if probando == 'no' :
        print('sos un pintor de mierda')
        break
    if probando != 'no' 'si' :
        print('bruh, queres que siga o no')
        probando = 'si'
        probando = input('queres que continue: ')
    t.fd(float(input('cuanto me muevo: ')))
    t.rt(float(input('cuanto a la derecha me muevo: ')))
    t.fd(float(input('cuanto me muevo: ')))
    t.lt(float(input('cuanto a la izquierda: ')))
    t.bk(float(input('cuanto me muevo: ')))
    t.lt(float(input('cuanto hacia algun lado: ')))
    t.fd(float(input('cuanto me muevo: ')))
    probando = input('queres que continue: ')


print('hasta nunca putooo')
turtle.done()
