"""Practica 1 Construya un diagrama de flujo que resuelva, el problema que tienen en una gasolinera, los sutidores
de la misma, registran lo que surten en galones, pero el precio de la gasolina, esta fijado en litros.
el diagrama de flujo debe pedir el precio por litro de gasolina, clacular e imprimir lo uqe hay que cobrarle al cliente.
consideraciones: cada galon tiene 3.785 litros"""

#Alvarez Carbajal Jonatan

while True: # ciclo para evitar que se introduscan valones negativos al programa
    print("Ingrese la Cantidad de galones despachados")
    galones = float(input())
    print("Ingrese el precio actual de la gasolina por litro")
    precioLitro = float(input())

    if galones<0 or precioLitro<0:
        print("Ni los galones ni el precio puede ser menr a 0")
    else:
        break #si ninguno de los dos es negativo sale dle bucle

print("El total a pagar es de: ",galones*3.785*precioLitro)
