import random
from classes import *

def menu():
    print("=" * 75)
    print("1 - Registrar vehiculos")
    print("2 - Mostrar los vehiculos registrados")
    print("3 - Buscar vehiculo con numero de identificacion especifico")
    print("4 - Calcular impuestos del vehiculo")
    print("0 - Salir")
    op = int(input("Seleccione la opcion deseada: "))
    return op

def validar_mayor(min, mensaje="Ingrese un numero"):
    num = int(input(mensaje))
    while min >= num:
        print("ERROR")
        num = int(input(mensaje))
    return num

def validar_entre(min, may, mensaje="Ingrese un numero"):
    num = int(input(mensaje))
    while (min > num) and (num > may):
        print("ERROR.")
        num = int(input(mensaje))
    return num

def generar_registro(n, vec):
    for i in range(n):
        num_id = random.randint(1, 7000)
        nombre = "Vehiculo " + str(num_id)
        stock = random.randrange(1000)
        pais = random.randrange(20)
        tipo = random.randrange(10)
        modelo = random.randrange(0, 2022)
        new_vehiculo = Vehiculo(num_id, nombre, stock, pais, tipo, modelo)
        vec.append(new_vehiculo)

def mostrar_registro(vec):
    print("-" * 150)
    print("Listado de vehiculos: ")
    for x in vec:
        print(x.to_string())
    print("-" * 150)

def buscar_vehiculo(num, vec):
    for i in range(len(vec)):
        if num == vec[i].numero_identificacion:
            print("-" * 150)
            print("El vehiculo con el N° de identificacion ", num, "es el siguiente: ")
            print(vec[i].to_string)
            print("-" * 150)
            return
    print("*" * 80)
    print("ERROR. No se ha encontrado un vehiculo con el N° de identificacion ", num, ".")
    print("*" * 80)





def main():

    x = Vehiculo(1, 2, 3, 4, 5, 6)
    x.to_string()

    op = -1
    vec = []

    while op != 0:
        op = menu()

        if op == 1:
            n = validar_mayor(0, "Ingrese la cantidad de vehiculos a registrar: ")
            generar_registro(n, vec)
            print("-" * 35)
            print("Vehiculos cargados exitosamente!")
            print("-" * 35)

        if len(vec) > 0:
            if op == 2:
                mostrar_registro(vec)

            elif op == 3:
                num = int(input("Ingrese el numero de identificacion del vehiculo que desea encontrar: "))
                buscar_vehiculo(num, vec)

            elif op == 4:
                print("Los impuestos a pagar son: ")
                for i in vec:
                    print("Para el auto: ", i.to_string())
                    print("$", i.calcular_impuestos(2022))
                    
                

            elif op > 6:
                print("*" * 40)
                print("Ha ingresado una opcion incorrecta.")
                print("*" * 40)
                pass

        else:
            print("*" * 115)
            print("ERROR. No se ha cargado ningun vehiculo todavia, por favor registre los vehiculos deseados utilizando"
                  " la opcion 1.")
            print("*" * 115)



if __name__ == "__main__":
    main()