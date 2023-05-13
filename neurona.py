import random
datos = [[1,1,1,],[1,0,0],[0,1,0],[0,0,0]]

pesos = [random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)]

aprendiendo = True
salidaEntera = 0
iteracion = 0
tasaAprende = 0.3


while(aprendiendo==True):
    
    iteracion = iteracion +1
    aprendiendo = False

    for cont in range(4):
        #Formula x1 * P1 + x2 * P2 + 1 * P3
        salidaReal = (datos[cont][0] * pesos[0] + datos[cont][1] * pesos[1] + 1 * pesos[2])
        if salidaReal > 0:
            salidaEntera = 1
        else:
            salidaEntera = 0

        error = int(datos[cont][2]-salidaEntera)

        if (error != 0):
            #formula = tasaAprende * error * x
            pesos[0] += tasaAprende * error * datos[cont][0]
            pesos[1] += tasaAprende * error * datos[cont][1]
            pesos[2] += tasaAprende * error * 1
            aprendiendo = True

    if aprendiendo == False:
        break


print("Iteraciones: ", iteracion)
print("Peso 1: ", pesos[0])
print("Peso 2: ", pesos[1])
print("Peso 3: ", pesos[2])

for cont in range(4):
        salidaReal = datos[cont][0] * pesos[0] + datos[cont][1] * pesos[1] + pesos[2]
        if salidaReal > 0:
            salidaEntera = 1
        else:
            salidaEntera = 0

        print("entradas: ", datos[cont][0], " y ", datos[cont][1]," = ", datos[cont][2], " perceptron ", salidaEntera)
