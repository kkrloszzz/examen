import os, time
from funciones import *

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
aleatorio = 0
sueldos = []




os.system('cls')
print("BIENVENIDO!")
time.sleep(1)
while True:
    while True:
        print("\nElija Una Opción a Realizar")
        print("\n1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        try:
            opc = int(input("\nDESEO EJECUTAR LA OPCIÓN: "))
            if opc in (1,2,3,4,5):
                break
            else:
                os.system('cls')
                print("ERROR! REINTENTE CON OPCIONES DISPONIBLES")
                time.sleep(2)
        except:
            os.system('cls')
            print("ERROR! OPCIÓN INVÁLIDA")
            time.sleep(2)
        

    if opc==1:
        opc1()

    elif opc ==2:
      opc2()


    elif opc==3:
        opc3()


    elif opc==4:
        opc4()

    elif opc==5:
        opc5()
        break

    

