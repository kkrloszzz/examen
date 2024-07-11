import random, os, time, csv

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
aleatorio = 0
sueldos = []
sueldos_dscto_salud = []
sueldos_dscto_afp = []
sueldos_liquido = []



def opc1():
    os.system('cls')
    print("Asignar sueldos aleatorios")
    time.sleep(1)
    for x in trabajadores:
        aleatorio = random.randint(300000,2500000)
        print(f"\nTRABAJADOR: {x}")
        print(f"SUELDO: : ${aleatorio} Pesos")
        time.sleep(1)
        sueldos.append(aleatorio)
    time.sleep(2)



def opc2():
    if not sueldos:
        os.system('cls')
        print("PRIMERO DESIGNE SUELDOS ANTES DE UTILIZAR LA OPCIÓN")
        time.sleep(2)
    else:

        os.system('cls')
        print("Clasificar sueldos")
        time.sleep(2)

        print("Sueldos menores a $800.000:")
        time.sleep(1)
        for x in sueldos:
            if x < 800000:
                print(f"\n${x}")
                time.sleep(1)
                

        time.sleep(2)
        print("\nSueldos entre $800.000 y $2.000.000:")
        time.sleep(1)
        for x in sueldos:
            if x >= 800000 and x <= 2000000:
                print(f"\n${x}")
                time.sleep(1)
        time.sleep(2)
        print("\nSueldos superiores a $2.000.000:")
        time.sleep(1)
        for x in sueldos:
            if x > 2000000:
                print(f"\n${x}")
                time.sleep(1)
        time.sleep(2)
        total = sum(sueldos)
        print(f"\nTOTAL DE LOS SUELDOS: ${total} Pesos")
        time.sleep(3)
        os.system('cls')



def opc3():

    if not sueldos:
        os.system('cls')
        print("PRIMERO DESIGNE SUELDOS ANTES DE UTILIZAR LA OPCIÓN")
        time.sleep(2)
    
    else:
        os.system('cls')
        print("VER ESTADÍSTICAS")
        time.sleep(2)

        #SUELDO MAS BAJO
        for x in sueldos:
            if x< 1000000 or x<600000 or x < 450000 or x==300000:
                sueldo_bajo = x 
        
        print(f"SUELDO MÁS BAJO: {sueldo_bajo}")      
        time.sleep(2)


        #SUELDO MAS ALTO
        for x in sueldos:
            if x >1500000 or x >1750000 or x>2000000 or x == 2500000:
                sueldo_alto = x
        print(f"SUELDO MÁS ALTO: {sueldo_alto}")
        time.sleep(2)

        #PROMEDIO DE SUELDOS
        prom_sueldos = (sum(sueldos))/10
        print(f"PROMEDIO DE LOS SUELDOS: {prom_sueldos}")
        time.sleep(2)

        #MEDIA GEOMETRICA
        for x in sueldos:
            media=(x*x)**(1/10)

        print(f"MEDIA GEOMÉTRICA {media}")
        time.sleep(2)
            


def opc4():
    if not sueldos:
        os.system('cls')
        print("PRIMERO DESIGNE SUELDOS ANTES DE UTILIZAR LA OPCIÓN")
        time.sleep(2)
    
    
    else:
        os.system('cls')
        print("REPORTE DE SUELDOS")
        time.sleep(2)
        for x in sueldos:
            salud =x * 0.93
            sueldos_dscto_salud.append(salud)
        for x in sueldos:
            afp = x * 0.88
            sueldos_dscto_afp.append(afp)
        

        with open("suelods.csv","w", newline="") as archivo:
            escritor = csv.writer(archivo)
            datos = ['Nombre', 'Sueldo Base', 'Dscto AFP', 'Dscto Salud']
            escritor.writerows(datos)
            print("ARCHIVO CSV EXPORTADO!")
            time.sleep(2)
            
        
            





def opc5():
    
    os.system('cls')
    print("Finalizando Programa.")
    time.sleep(1)
    os.system('cls')
    print("Finalizando Programa..")
    time.sleep(1)
    os.system('cls')
    print("Finalizando Programa...")
    time.sleep(1)
    print("Desarrollado Por Carlos Domke")
    time.sleep(1)
    print("RUT: 21.977.468-0")
    time.sleep(1)