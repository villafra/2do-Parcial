import re
from Entidades import *
import os

ListadoArticulos = []
ListadoVentas = []

def MenuPrincipal():
   print ("\nAltaPlastica")
   print ("Por favor elija un item del menu:")
   print ("1-Articulos")
   print ("2-Ventas")
   print ("3-Salir")

   try:
    opcion = int(input())
   except ValueError:
       MenuPrincipal()
    
   while opcion < 4:
       if opcion == 1:
           MenuArticulos()
           break
       elif opcion == 2:
           MenuVentas()
           break
       elif opcion == 3:
           print("El programa ha finalizado correctamente.")
           exit()
   else:
        MenuPrincipal() 

def MenuArticulos():
    print("Por favor elija un item del menu:")
    print("1-Alta Articulo")
    print("2-Modificar Articulo")
    print("3-Eliminar Articulo")
    print("4-Agregar Stock Articulo")
    print("5-Listar Articulos")
    print("6-Ir Al Menu Principal")
    try:
        menu1= int(input())
    except ValueError:
            MenuArticulos()
    while menu1 < 7:
        if menu1 == 1:
            AltaArticulo()
            break
        elif menu1 == 2:
            ModificarArticulo()
            break
        elif menu1 == 3:
            EliminarArticulo()
            break
        elif menu1 == 4:
            AgregarStock()
            break
        elif menu1 == 5:
            ImprimirArticulos()
            MenuArticulos()
            break
        elif menu1 == 6:
            MenuPrincipal()
            break
    else:
        MenuArticulos()

def MenuVentas():
    print("Por favor elija un item del menu:")
    print("1-Nueva Venta")
    print("2-Modificar Venta")
    print("3-Eliminar Venta")
    print("4-Salir")
    try:
        menu2= int(input())
    except ValueError:
            MenuVentas()
    while menu2 < 5:
        if menu2 == 1:
            NuevaVenta()
            break
        elif menu2 == 2:
            ModificarVenta()
            break
        elif menu2 == 3:
            EliminarVenta()
            break
        elif menu2 == 4:
            MenuPrincipal()
            break
    else:
        MenuVentas()

def AltaArticulo():
    print("Ingrese Codigo del nuevo Articulo:")
    codigo = input()
    if not ValidarCodigoArticulo(codigo):
        print("El formato no es correcto. Por favor ingrese nuevamente en formato X000-")
        AltaArticulo()
    if BuscarArticulo(codigo):
        print("El codigo de articulo ya existe en la base de datos. Por favor intente nuevamente.")
        AltaArticulo()
    print ("Ingrese descripcion del nuevo Articulo:")
    descripcion = input()
    print ("Ingrese Stock Inicial:")
    try:
        stock = int(input())
    except ValueError:
        print("Por favor ingrese cantidad en numeros solamente. Operacion Cancelada")
        AltaArticulo()
    print ("Ingrese Costo Unitario:")
    try:
        costo = float(input())
    except ValueError:
        print("Por favor ingrese Costo en numeros solamente. Operacion Cancelada")
        AltaArticulo()
    RegistrarArticulo = open("ListadoArticulos.txt", "a")
    NuevoArticulo = Articulo(codigo, descripcion, stock, costo)
    print(f"Se va a registrar: {NuevoArticulo.Codigo},{NuevoArticulo.Descripcion},{NuevoArticulo.Stock},{NuevoArticulo.CostoUnitario}.\n Desea continuar?")
    print("1-SI")
    print("2-NO")
    try:
        opcion = int(input())
        if opcion == 1:
            RegistrarArticulo.write(f"{NuevoArticulo.Codigo},{NuevoArticulo.Descripcion},{NuevoArticulo.Stock},{NuevoArticulo.CostoUnitario}\n")
            RegistrarArticulo.close()
            print(f"Se registrado: {NuevoArticulo}")
            MenuArticulos()
        elif opcion == 2:
            print("Se ha cancelado la operacion.")
            MenuArticulos()
        else:
            print("Solo puede elegir entre 1 o 2")
            MenuArticulos()
    except:
        print("Formato de opcion incorrecto, se cancela la operacion.")
        MenuArticulos()

def ModificarArticulo():
    print("Ingrese Codigo de Articulo a Modificar:")
    codigo = input()
    ListadoArticulos = ListarArticulos()
    modArticulo = BuscarArticulo(codigo)
    if modArticulo:
        print("Ingrese el nuevo dato cuando sea requerido, campo en blanco para mantener el dato actual.")
        print(f"Codigo actual: {modArticulo.Codigo}. Ingrese Nuevo Codigo:")
        nuevocodigo = input()
        if nuevocodigo == "":
            nuevocodigo = modArticulo.Codigo
        print(f"Descripcion actual: {modArticulo.Descripcion}. Ingrese Nueva Descripcion:")
        nuevadescripcion = input()
        if nuevadescripcion == "":
            nuevadescripcion = modArticulo.Descripcion
        print(f"Costo Unitario Actual: {modArticulo.CostoUnitario}. Ingrese Nuevo Costo:")
        try:
            nuevocosto = float(input())
        except:
            nuevocosto = modArticulo.CostoUnitario
        indice = ListadoArticulos.index(modArticulo)
        ListadoArticulos[indice].Codigo = nuevocodigo
        ListadoArticulos[indice].Descripcion = nuevadescripcion
        ListadoArticulos[indice].CostoUnitario = nuevocosto
        if ModificarListaArticulos():
            print("El Articulo se ha modificado correctamente.")
            MenuArticulos()
        else:
            print("El Articulo no pudo modificarse, por favor intente nuevamente.")
            ModificarArticulo()
    else:
        "El articulo no existe en la base de datos."
    MenuArticulos()
    
def ModificarListaArticulos():
    try:
        aux = open("auxArticulos.dat","a")
        for articulo in ListadoArticulos:
            aux.write(f"{articulo.Codigo},{articulo.Descripcion},{articulo.Stock},{articulo.CostoUnitario}\n")
        aux.close()
        os.remove("ListadoArticulos.txt")
        os.rename("auxArticulos.dat","ListadoArticulos.txt")
        return True
    except:
        return false
   
def ImprimirArticulos():
    imprimir = ListarArticulos()
    if imprimir:
        print("+---------------------+-----------------------------------------+----------------------+----------------------+")
        print("|       Codigo        |               Descripcion               |         Stock        |     Costo Unitario   |")
        print("+---------------------+-----------------------------------------+----------------------+----------------------+")
        for articulos in imprimir:
            Codigo = articulos.Codigo
            Descripcion = articulos.Descripcion
            Stock = articulos.Stock
            CostoUnitario = articulos.CostoUnitario
            cadena = "| {:<20}| {:<40}| {:<21}| ${:<20}|".format(Codigo, Descripcion, Stock, CostoUnitario)
            print(cadena)
        print("+---------------------+-----------------------------------------+----------------------+----------------------+\n")

def BuscarArticulo(Codigo):
    DevolverArticulo = False
    Listado = ListarArticulos()
    for articulo in Listado:
        if Codigo == articulo.Codigo:
            DevolverArticulo = articulo
    return DevolverArticulo

def ListarArticulos():
    try:
        Listado = open("ListadoArticulos.txt", "r")
        ListadoArticulos.clear()
        for articulo in Listado:
            armaarticulo = articulo.split(",")
            AgregarArticulo = Articulo(armaarticulo[0], armaarticulo[1], int(armaarticulo[2]),float(armaarticulo[3]))
            ListadoArticulos.append(AgregarArticulo)
        return ListadoArticulos
    except:
        return False
    finally:
        Listado.close()
    
def EliminarArticulo():
    print("Ingrese Codigo de Articulo a Eliminar:")
    codigo = input()
    ListadoArticulos = ListarArticulos()
    killArticulo = BuscarArticulo(codigo)
    if killArticulo:
        print(f"Esta seguro de borrar {killArticulo}?")
        print("1-SI")
        print("2-NO")
        try:
            opcion = int(input())
            if opcion == 1:
                indice = ListadoArticulos.index(killArticulo)
                ListadoArticulos.pop(indice)
                if ModificarListaArticulos():
                    print(f"El articulo {killArticulo} ha sido borrado de la base de datos.")
                    MenuArticulos()
                else:
                    print(f"No se pudo borrar el articulo {killArticulo}. Por favor, intente nuevamente")
                    EliminarArticulo()
            elif opcion == 2:
                print("Eliminar articulo, cancelado.")
                MenuArticulos()
            else:
                print("Solo puede elegir entre 1 o 2")
                EliminarArticulo()
        except:
            EliminarArticulo()

def ValidarCodigoArticulo(Codigo):
    formato = re.compile(r"[A-Z]{1}[0-9]{3}")
    if re.fullmatch(formato,Codigo):
        return True
    else:
        return False

def AgregarStock():
    print("Ingrese Codigo de Articulo para agregar Stock:")
    codigo = input()
    ListadoArticulos = ListarArticulos()
    agregarstock = BuscarArticulo(codigo)
    if agregarstock:
        print(f"Agregar stock a {agregarstock}?")
        print("1-SI")
        print("2-NO")
        try:
            opcion = int(input())
            if opcion == 1:
                print("Ingrese cantidad:")
                cantidad = int(input())
                agregarstock.AgregarStock(cantidad)
                indice = ListadoArticulos.index(agregarstock)
                ListadoArticulos[indice].Stock = agregarstock.Stock
                if ModificarListaArticulos():
                    print("Se ha actualizado correctamente el stock.")
                    MenuArticulos()
                else:
                    print("No se pudo actualizar el stock, por favor intente nuevamente.")
                    AgregarStock()
            elif opcion == 2:
                print("Se ha cancelado la operacion.")
                MenuArticulos()
            else:
                print("Solo puede elegir entre 1 o 2")
                MenuArticulos()
        except:
            print("Solo puede elegir entre 1 o 2")
            AgregarStock()
    else:
        print("El codigo ingresado es inexistente.")
        MenuArticulos()

def NuevaVenta():
    pass
def ModificarVenta():
    pass
def EliminarVenta():
    pass

MenuPrincipal()