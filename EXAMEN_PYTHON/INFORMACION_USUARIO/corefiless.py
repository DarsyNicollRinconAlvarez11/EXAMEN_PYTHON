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




      
def informacion():
    id = ('Ingrese el numero de identificacion de la persona')    
    #if (persona["id"] == id):
        #      print("Ese id ya se encuentra registrado en zonas")
    
    
    nombre =input('Ingrese el nombre de la persona \n :> ')
    apellidos =input('Ingrese los apellidos de la persona \n :>' )
    direccion =input('Ingrese ingrese la direccion \n :>')
    ciudad =input('Ingrese ingrese la ciudad \n :>')
    longitud =input('Ingrese ingrese la longitud \n :>')
    latitud =input('Ingrese ingrese la latitud \n :>')
    email =input('Ingrese el email \n :>')
    edad =input('Ingrese la edad \n :>')
    ocupacion =input('Ingrese la ocupacion \n :>')
    nueva_persona = {
            'id': id,
            'nombre':nombre,
            'apellidos':apellidos,
            'ubicacion':{
                'direccion':direccion,
                'ciudad':ciudad,
                'longitud':longitud,
                'latitud':latitud   
            },
            'email':email,
            'edad':edad,
            'ocupacion':ocupacion,
        }
    informacion(persona)