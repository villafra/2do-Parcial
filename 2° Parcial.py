from fileinput import close
import re
import sys
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
           raise SystemExit
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
    print("4-Listar Ventas")
    print("5-Ir Al Menu Principal")
    try:
        menu2= int(input())
    except ValueError:
            MenuVentas()
    while menu2 < 6:
        if menu2 == 1:
            ImprimirArticulos()
            NuevaVenta()
            break
        elif menu2 == 2:
            ModificarVenta()
            break
        elif menu2 == 3:
            EliminarVenta()
            break
        elif menu2 == 4:
            ImprimirVentas()
            break
        elif menu2 == 5:
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
        opcion1 = int(input())
        if opcion1 == 1:
            RegistrarArticulo.write(f"{NuevoArticulo.Codigo},{NuevoArticulo.Descripcion},{NuevoArticulo.Stock},{NuevoArticulo.CostoUnitario}\n")
            RegistrarArticulo.close()
            print(f"Se registrado: {NuevoArticulo}")
        elif opcion1 == 2:
            RegistrarArticulo.close()
            print("Se ha cancelado la operacion.")
        else:
            print("Solo puede elegir entre 1 o 2")
    except:
        print("Formato de opcion incorrecto, se cancela la operacion.")
    finally:
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
        return False
   
def ImprimirArticulos():
    imprimir = ListarArticulos()
    if imprimir:
        print("+---------------------+-----------------------------------------------+----------------------+-----------------------+")
        print("|       Codigo        |                  Descripcion                  |         Stock        |     Costo Unitario    |")
        print("+---------------------+-----------------------------------------------+----------------------+-----------------------+")
        for articulos in imprimir:
            Codigo = articulos.Codigo
            Descripcion = articulos.Descripcion
            Stock = articulos.Stock
            CostoUnitario = articulos.CostoUnitario
            cadena = "| {:<20}| {:<46}| {:<21}| ${:<21}|".format(Codigo, Descripcion, Stock, CostoUnitario)
            print(cadena)
        print("+---------------------+-----------------------------------------------+----------------------+-----------------------+\n")

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
            opcion2 = int(input())
            if opcion2 == 1:
                indice = ListadoArticulos.index(killArticulo)
                ListadoArticulos.pop(indice)
                if ModificarListaArticulos():
                    print(f"El articulo {killArticulo} ha sido borrado de la base de datos.")
                    MenuArticulos()
                else:
                    print(f"No se pudo borrar el articulo {killArticulo}. Por favor, intente nuevamente")
                    EliminarArticulo()
            elif opcion2 == 2:
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
def ValidarSucursal(Sucursal):
    formato = re.compile(r"[A-Z]{3}[0-9]{3}")
    if re.fullmatch(formato, Sucursal):
        return True
    else:
        return False
def ValidarFormatoFecha(fecha):
    formato = re.compile(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})")
    if re.fullmatch(formato, fecha):
        separar = fecha.split("/")
        if VerificarFecha(int(separar[0]),int(separar[1]),int(separar[2])):
            return True
        else:
            return False
    else:
        return False
def VerificarFecha(dia, mes, anio):
    Meses = {4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
    diasxmes = Meses.get(mes, 31)
    if diasxmes == 28:
        if anio % 4 == 0:
            if anio % 100 == 0:
                if anio % 400 == 0:
                    diasxmes = 29
            else:
                diasxmes = 29
    if dia <= diasxmes:
        return True
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
            opcion3 = int(input())
            if opcion3 == 1:
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
            elif opcion3 == 2:
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
    print("Ingrese Codigo de articulo vendido:")
    codigo = input()
    articulo = BuscarArticulo(codigo)
    if not articulo:
        print("El codigo de articulo no existe en la base de datos. Por favor intente nuevamente.")
        NuevaVenta()
    print("Ingrese Cantidad:")
    try:
        cantidad = int(input())
    except ValueError:
        print("Por favor ingrese cantidad en numeros solamente. Operacion Cancelada.")
        NuevaVenta()
    print("Ingrese Nombre de Vendedor:")
    vendedor = input()
    print("Ingrese sucursal:")
    sucursal = input()
    if not ValidarSucursal(sucursal):
        print("El formato de sucursal no es correcto.Intente nuevamente.")
        NuevaVenta()
    print("Ingrese Fecha de Venta (formato dd/mm/yyyy):")
    fecha = input()
    if not ValidarFormatoFecha(fecha):
        print("El formato de fecha no es correcto.Intente nuevamente.")
        NuevaVenta()
    RegistrarVenta = open("ListadoVentas.txt","a")
    venta = Venta(fecha, articulo, vendedor, sucursal, cantidad)
    print(f"Se va a registrar: {venta} por un importe de: {round(venta.ImporteVendido,2)}, desea continuar?")
    print("1-SI")
    print("2-NO")
    try:
        opcion4 = int(input())
        if opcion4 == 1:
            RegistrarVenta.write(f"{venta.NumeroFactura},{venta.Fecha},{venta.CodigoArticulo.Codigo},{venta.Vendedor},{venta.Sucursal},{venta.Cantidad},{venta.ImporteVendido}\n")
            RegistrarVenta.close()
            print(f"Se ha registrado: {venta}")
        elif opcion4 == 2:
            print("Se ha cancelado la operacion.")
            RegistrarVenta.close()
    except:
        print("Formato de opcion incorrecto, se cancela la operacion")
    finally:
        MenuVentas()

def ModificarListaVentas():
    try:
        aux = open("auxVentas.dat","a")
        for venta in ListadoVentas:
            aux.write(f"{venta.NumeroFactura},{venta.Fecha},{venta.CodigoArticulo.Codigo},{venta.Vendedor},{venta.Sucursal},{venta.Cantidad},{venta.ImporteVendido}\n")
        aux.close()
        os.remove("ListadoVentas.txt")
        os.rename("auxVentas.dat","ListadoVentas.txt")
        return True
    except:
        return False
def ModificarVenta():
    print("Ingrese Numero de Factura a Modificar:")
    numfac = input()
    ListadoVentas = ListarVentas()
    modVenta = BuscarVenta(numfac)
    if modVenta:
        print("Ingrese el nuevo dato cuando sea requerido, campo en blanco para mantener el dato actual.")
        print(f"Numero de factura actual: {modVenta.NumeroFactura}. Ingrese Nuevo Codigo:")
        nuevonumero = input()
        if nuevonumero == "":
            nuevonumero = modVenta.NumeroFactura
        print(f"Fecha actual: {modVenta.Fecha}. Ingrese Nueva Fecha:")
        nuevafecha = input()
        if nuevafecha == "":
            nuevafecha = modVenta.Fecha
        print(f"Codigo Articulo actual: {modVenta.CodigoArticulo.Codigo}. Ingrese Nuevo Codigo Articulo:")
        nuevocodigo = input()
        if nuevocodigo == "":
            nuevocodigo = BuscarArticulo(modVenta.CodigoArticulo.Codigo)
        elif ValidarCodigoArticulo(nuevocodigo):
            nuevocodigo = BuscarArticulo(nuevocodigo)
            if not nuevocodigo:
                print("El Articulo es inexistente.Operacion Cancelada.")
                ModificarVenta()
        else:
            print("El nuevo codigo de articulo no tiene el formato correcto.Operacion cancelada.")
            ModificarVenta()
        print(f"Vendedor Actual : {modVenta.Vendedor}. Ingrese nuevo Vendedor:")
        nuevovendedor = input()
        if nuevovendedor == "":
            nuevovendedor = modVenta.Vendedor
        print(f"Sucursal Actual : {modVenta.Sucursal}. Ingrese nueva Sucursal:")
        nuevasucursal = input()
        if nuevasucursal == "":
            nuevasucursal = modVenta.Sucursal
        elif not ValidarSucursal(nuevasucursal):
            print ("La sucursal agregada, no tiene el formato correcto. Operacion Cancelada.")
            NuevaVenta()
        print(f"Cantidad actual: {modVenta.Cantidad}. Ingrese nueva cantidad:")
        try:
            nuevacantidad = int(input())
            modVenta.CalcularTotalVenta(nuevacantidad)
        except:
            nuevacantidad = modVenta.Cantidad
        indice = ListadoVentas.index(modVenta)
        ListadoVentas[indice].NumeroFactura = nuevonumero
        ListadoVentas[indice].Fecha = nuevafecha
        ListadoVentas[indice].CodigoArticulo = nuevocodigo
        ListadoVentas[indice].Vendedor = nuevovendedor
        ListadoVentas[indice].Sucursal = nuevasucursal
        ListadoVentas[indice].Cantidad = nuevacantidad
        if ModificarListaVentas():
            print("La venta se ha modificado correctamente.")
            MenuVentas()
        else:
            print("La venta no pudo modificarse, por favor intente nuevamente.")
            ModificarListaVentas()
    else:
        "La factura no existe en la base de datos."
    MenuVentas()

def BuscarVenta(Numero):
    DevolverVenta = False
    Listado = ListarVentas()
    for venta in Listado:
        if Numero == venta.NumeroFactura:
            DevolverVenta = venta
    return DevolverVenta

def ListarVentas():
    try:
        Listado = open("ListadoVentas.txt", "r")
        ListadoVentas.clear()
        for venta in Listado:
            armaventa = venta.split(",")
            AgregarVenta = Venta(armaventa[1],BuscarArticulo(armaventa[2]),armaventa[3],armaventa[4],int(armaventa[5]),armaventa[0])
            ListadoVentas.append(AgregarVenta)
        return ListadoVentas
    except:
        return False
    finally:
        Listado.close()
def ImprimirVentas():
    imprimir = ListarVentas()
    if imprimir:
        print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
        print("|   Nro Factura   |    Fecha    | Cod. Articulo |        Vendedor        |  Sucursal  |   Cantidad   |    Importe    |")
        print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
        for ventas in imprimir:
            numfac = ventas.NumeroFactura
            fecha = ventas.Fecha
            codigo = ventas.CodigoArticulo.Codigo
            vendedor = ventas.Vendedor
            sucursal = ventas.Sucursal
            cantidad = ventas.Cantidad
            importe = ventas.ImporteVendido
            cadena = "| {:<16}| {:<12}| {:<14}| {:<23}| {:<11}| {:<13}| ${:<13}|".format(numfac, fecha, codigo, vendedor,sucursal,cantidad,importe)
            print(cadena)
        print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
        
def EliminarVenta():
    print("Ingrese numero de Factura a Eliminar:")
    factura = input()
    ListadoVentas = ListarVentas()
    killfactura = BuscarVenta(factura)
    if killfactura:
        print(f"Esta seguro de borrar {killfactura}?")
        print("1-SI")
        print("2-NO")
        try:
            opcion5 = int(input())
        except:
            print("Formato de opcion incorrecto. Se cancela la operacion.")
            EliminarVenta()
            if opcion5 == 1:
                indice = ListadoVentas.index(killfactura)
                ListadoVentas.pop(indice)
                if ModificarListaVentas():
                    print(f"La venta {killfactura} ha sido borrada de la base de datos.")
                    MenuVentas()
                else:
                    print(f"No se pudo borrar la venta {killfactura}. Por favor, intente nuevamente")
                    EliminarVenta()
            elif opcion5 == 2:
                print("Eliminar venta, cancelado.")
                MenuVentas()
            else:
                print("Solo puede elegir entre 1 o 2")
                EliminarVenta()
def OrdenarVentas(lista):
    tamanio = len(lista)
    for i in range(0,tamanio):
        min = i
        for j in range(i + 1 ,tamanio):
            if lista[min].Sucursal > lista[j].Sucursal:
                min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    criterio = lista[0].Sucursal
    fin = 0
    for i in range(0,tamanio):
        if lista[i].Sucursal == criterio:
            fin = i
    for i in range(0,fin):
        min = i
        for j in range (i + 1,fin+1):
            if lista[min].CodigoArticulo.Codigo > lista[j].CodigoArticulo.Codigo:
                if lista[j].Sucursal == criterio:
                    min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
    print("|   Nro Factura   |    Fecha    | Cod. Articulo |        Vendedor        |  Sucursal  |   Cantidad   |    Importe    |")
    print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
    for ventas in lista:
            numfac = ventas.NumeroFactura
            fecha = ventas.Fecha
            codigo = ventas.CodigoArticulo.Codigo
            vendedor = ventas.Vendedor
            sucursal = ventas.Sucursal
            cantidad = ventas.Cantidad
            importe = ventas.ImporteVendido
            cadena = "| {:<16}| {:<12}| {:<14}| {:<23}| {:<11}| {:<13}| ${:<13}|".format(numfac, fecha, codigo, vendedor,sucursal,cantidad,importe)
            print(cadena)
    print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
    criterio = lista[fin+1].Sucursal
    for i in range(fin+1, tamanio):
        min = i
        for j in range (i + 1,tamanio):
            if lista[min].CodigoArticulo.Codigo > lista[j].CodigoArticulo.Codigo:
                if lista[j].Sucursal == criterio:
                    min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    criterio = lista[0].Sucursal
    criterio1 = lista[0].CodigoArticulo.Codigo
    for i in range(0,tamanio):
        min = i
        if lista[i].Sucursal and lista[i].CodigoArticulo.Codigo == criterio1:
            for j in range (i + 1,tamanio):
                if lista[min].Vendedor > lista[j].Vendedor:
                    if lista[j].Sucursal == criterio and lista[j].CodigoArticulo.Codigo == criterio1:
                        min = j
            aux = lista[i]
            lista[i] = lista[min]
            lista[min] = aux
        else:
            criterio = lista[i].Sucursal
            criterio1 = lista[i].CodigoArticulo.Codigo
            if lista[j-1].Vendedor > lista[j].Vendedor:
                    if lista[j].Sucursal == criterio and lista[j].CodigoArticulo.Codigo == criterio1:
                        min = j
            aux = lista[i]
            lista[i] = lista[min]
            lista[min] = aux
    print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
    print("|   Nro Factura   |    Fecha    | Cod. Articulo |        Vendedor        |  Sucursal  |   Cantidad   |    Importe    |")
    print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
    for ventas in lista:
            numfac = ventas.NumeroFactura
            fecha = ventas.Fecha
            codigo = ventas.CodigoArticulo.Codigo
            vendedor = ventas.Vendedor
            sucursal = ventas.Sucursal
            cantidad = ventas.Cantidad
            importe = ventas.ImporteVendido
            cadena = "| {:<16}| {:<12}| {:<14}| {:<23}| {:<11}| {:<13}| ${:<13}|".format(numfac, fecha, codigo, vendedor,sucursal,cantidad,importe)
            print(cadena)
    print("+-----------------+-------------+---------------+------------------------+------------+--------------+---------------+")
    return lista
ImprimirVentas()
ImprimirArticulos()
OrdenarVentas(ListarVentas())

MenuPrincipal()