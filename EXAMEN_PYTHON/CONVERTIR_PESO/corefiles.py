import sys
from os import system 

def borrarPant():
    if sys.platform == "linux" or sys.platform == "darwin" :
        system("clear")
    else:
        system("cls")

def paussPant():
    if sys.platform == "linux" or sys.platform == "darwin":
        input('Enter para continuar...')
    else: system("pause")


yen = 26.30
dolar = 3944 
euro = 4279 
pesos = 4279

def convertir():
    while (True):
        borrarPant()
        print("""
            +++++++++++++++++++++++++++++
            |        CONVERTIR          |
            +++++++++++++++++++++++++++++ 
        Elija una opcion segun lo que desee hacer
            
        1. Convertir de pesos a dolares.
        2. Convertir de pesos a euros.
        3. Convertir de euros a pesos.
        4. Convertir de pesos a yenes.
        5. Salir 
            """)
        op = input(":> ")
        valor = int(input("Ingrese el valor que desea convertir. \n :> "))
        if (op == '1'):
            total = valor // dolar
            print(valor,' pesos equivalen a ',total ,' dolares. ')
        elif (op == '2'):
            total = valor // euro
            print(valor,' pesos equivalen a ',total, ' euros. ')
        elif (op == '3'):
            total = valor * euro
            print(valor,' euros equivalen a ',total, ' pesos. ')
        elif (op == '4'):
            total = valor // yen
            print(valor,' pesos equivalen a ',total, ' yenes. ')
        opcion = input("¿Desea convertir otro valor ? Si(s) / No(Enter): ").lower()
        if opcion.lower() != "s":
            break

    



