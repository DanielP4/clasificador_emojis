import random

CompAND=[[1,1,1],
       [1,0,0],
       [0,1,0],
       [0,0,0]]


pesos = [random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)]

aprendiendo = True
salida = 0
iteracion = 0
tasaAprende = 0.3
iteraciones = 0



while(aprendiendo == True):
     iteracion = iteracion + 1
     aprendiendo = False

     for i in range(0,4):
          #formula : s = f(E1 * P1 + E2 * P2 + 1 * P3)
          #E1, E2 = entradas (valores de entrada en al compuerta logica)
          #P1, P2, P3 = pesos (pesos generados aleatoriamente) 
          salidaReal = (CompAND[i][0] * pesos[0] + CompAND[i][1] * pesos[1] + 1 * pesos[2])

          if salidaReal > 0:
               salida = 1
          else:
               salida = 0
          
          #calculamos el errror con la salida prevista de la compuerta
          error = int(CompAND[i][2] - salida)

          if error != 0:
               #Si el error es diferente de 0 debemos calcular nuevos pesos
               pesos[0]  += tasaAprende * error + CompAND[i][0]
               pesos[1]  += tasaAprende * error + CompAND[i][1]
               pesos[2]  += tasaAprende * error * 1

               aprendiendo = True
       
       #si los calculos fueron correctos termina el aprendizaje
     if aprendiendo == False:
          break

#mostramos los ciclos usados para entrenar el percetron
#mostramos los pesos correctos y resulatados
print("Iteraciones: ", iteracion)
print("Peso 1: ", pesos[0])
print("Peso 2: ", pesos[1])
print("Peso 3: ", pesos[2])

for i in range(0,4):
     salidaReal = (CompAND[i][0] * pesos[0] + CompAND[i][1] * pesos[1] + 1 * pesos[2])
     if salidaReal > 0:
          salida = 1
     else:
          salida = 0
     
     print("Entradas: ", CompAND[i][0], " y ", CompAND[i][1], " = ", CompAND[i][2], "perceptron: ", salida)
     