#!/usr/bin/env python
# -*- coding: latin1 -*-

# < latin1 >  usa a nomcratura portuguesa

#usado em comentario

#Print de Hello World

print("Ol� Mundo")

#Exibi o resultado da multiplica��o 7*3
print (7*3)

for i in [2,4,5,6,7,10]: #for que percorre a lista de inteiros
     
    if i%3 == 0 :   # condi��o que verifica se o resto da divis�o e iguala 0 se for 
         
        print (i, '/ 3 =', i / 3)  #printa o valor e a divisao.

#estrutura de desis�o
temp = int(raw_input('Entre com a temperatura: '))
if temp < 0 :
    print ('Congelando...')
     elif 0<=temp<=20 :
        print ('Frio')
         elif 21<=temp<= 25 :
                print ('Normal')
                elif 26<=temp<= 35 :
                    print ('Quente')
                        else:
                        print ('Muito quente!')
