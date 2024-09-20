"""Practica 2 costruya un diagrama de flujo que calcule e imprima el numero de segundos que hay en un determinado 
numero de dias"""
#Alvarez Carbajal Jonatan

while True:
    print("Ingrese la cantidad de dias que queire convertir en segundos:")
    dias = int(input())
    if dias<0:
        print("Los dias no pudn ser negativos")
    else:
        break
print("La cantidad de segundo en ",dias,"es: ",dias*60*60*23)
