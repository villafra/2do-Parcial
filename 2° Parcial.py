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
   print ("3-Corte de Control")
   print ("4-Salir")

   try:
    opcion = int(input())
   except ValueError:
       MenuPrincipal()
    
   while opcion < 5:
       if opcion == 1:
           MenuArticulos()
           break
       elif opcion == 2:
           MenuVentas()
           break
       elif opcion == 3:
           ImprimirReporte()
           break
       elif opcion == 4:
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
    print("Ingrese Codigo del nuevo Articulo (presione 0, para salir):")
    codigo = input()
    if codigo ==str(0):
        MenuArticulos()
    else:
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
            AgregarArticulo = Articulo(armaarticulo[0], armaarticulo[1], int(armaarticulo[2]),round(float(armaarticulo[3]),2))
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
    else:
        print("El codigo de Articulo seleccionado es inexistente. Por favor, intente nuevamente.")
        MenuArticulos()

def ValidarCodigoArticulo(Codigo):
    formato = re.compile(r"[A-Z]{1}[0-9]{3}")
    if re.fullmatch(formato,Codigo):
        return True
    else:
        return False

def ValidarSucursal(Sucursal):
    formato = re.compile(r"SUC[0-9]{3}")
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

def DescontarStock(articulo, cantidad):
    if articulo.DescontarStock(cantidad):
        indice = ListadoArticulos.index(articulo)
        ListadoArticulos[indice].Stock = articulo.Stock
        ModificarListaArticulos()
        return True
    else:
        return False

def DevolverStock(articulo, cantidad):
    articulo.AgregarStock(cantidad)
    indice = ListadoArticulos.index(articulo)
    ListadoArticulos[indice].Stock = articulo.Stock
    ModificarListaArticulos()

def ComprobarStock(articulo, cantidad):
    return articulo.ComprobarStock(cantidad)

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
    print("Ingrese Codigo de articulo vendido (presione 0 para salir):")
    codigo = input()
    if codigo == str(0):
            MenuVentas()
    else:
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
                if ComprobarStock(articulo, cantidad):
                    if DescontarStock(articulo, cantidad):
                        RegistrarVenta.write(f"{venta.NumeroFactura},{venta.Fecha},{venta.CodigoArticulo.Codigo},{venta.Vendedor},{venta.Sucursal},{venta.Cantidad},{venta.ImporteVendido}\n")
                        RegistrarVenta.close()
                        print(f"Se ha registrado: {venta}")
                    else:
                        print("No se pudo completar la operacion. Por favor, intente nuevamente.")
                        NuevaVenta()
                else:
                    print("El stock disponible no alcanza para completar la transaccion. Intente nuevamente.")
                    NuevaVenta()
            elif opcion4 == 2:
                print("Se ha cancelado la operacion.")
                RegistrarVenta.close()
        except Exception as e:
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
    devolvercantidad = False
    cantadevolver = 0
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
            devolvercantidad = True
            cantadevolver = modVenta.Cantidad
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
            if devolvercantidad:
                DevolverStock(modVenta.CodigoArticulo,cantadevolver)
                DescontarStock(nuevocodigo,nuevacantidad)
            print("La venta se ha modificado correctamente.")
            MenuVentas()
        else:
            print("La venta no pudo modificarse, por favor intente nuevamente.")
            ModificarListaVentas()
    else:
        print("La factura no existe en la base de datos.")
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
    MenuVentas()
    
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
              DevolverStock(killfactura.CodigoArticulo, killfactura.Cantidad)
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
    else:
        print("El Nro de factura ingresado es inexiste. Por favor, intente nuevamente.")
        MenuVentas()
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
    inicio = 0
    fin = 0
    enlazarSucur = []
    for i in range(0,tamanio):
        if lista[i].Sucursal == criterio:
            fin += 1
        else:
            criterio = lista[i].Sucursal
            enlazarSucur.append(fin)
            fin+=1
    enlazarSucur.append(tamanio)
    control = len(enlazarSucur)
    contador = 2
    criterio = lista[0].Sucursal
    for x in enlazarSucur:
        for i in range(inicio, x):
            min = i
            for j in range (i + 1,x):
                if lista[min].CodigoArticulo.Codigo > lista[j].CodigoArticulo.Codigo:
                    if lista[j].Sucursal == criterio:
                        min = j
            if i + 1 == tamanio:
                if lista[min].CodigoArticulo.Codigo > lista[j].CodigoArticulo.Codigo:
                    if lista[j].Sucursal == criterio:
                        min = j
            aux = lista[i]
            lista[i] = lista[min]
            lista[min] = aux
        if contador < control:
            inicio = x
        else:
            inicio = x
        if x+1 < fin:
            criterio = lista[x+1].Sucursal
            contador +=1
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
def ImprimirReporte():
    TotalGral = 0
    ListaOrdenada = OrdenarVentas(ListarVentas())
    subtotalvendedor = 0
    subtotalarticulo = 0
    subtotalsucursal = 0
    criterio1 = ListaOrdenada[0].Sucursal
    criterio2 = ListaOrdenada[0].CodigoArticulo.Codigo
    criterio3 = ListaOrdenada[0].Vendedor
    imprimirSucursal = criterio1
    imprimirArticulo = criterio2
    imprimirVendedor = criterio3
    i = 0
    print("+----------+------------------------+----------------------+---------------+---------------+---------------+----------+")
    print("| Sucursal |  Articulo Descripcion  |       Vendedor       | Subt Vendedor | Subt Articulo | Subt Sucursal |  Total   |")
    print("+----------+------------------------+----------------------+---------------+---------------+---------------+----------+")
    cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| {:<14}| {:<14}| {:<9}|".format(imprimirSucursal,"","","","","","")
    print(cadena)
    while i < len(ListaOrdenada):
        while ListaOrdenada[i].Sucursal == criterio1:
            if imprimirSucursal != criterio1:
                imprimirSucursal = criterio1
                cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| {:<14}| {:<14}| {:<9}|".format(imprimirSucursal,"","","","","","")
                print(cadena)
            if i+1 <len(ListaOrdenada):
               if ListaOrdenada[i+1].Sucursal != imprimirArticulo:
                        cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| {:<14}| {:<14}| {:<9}|".format("",BuscarArticulo(imprimirArticulo).Descripcion,"","","","","")
                        print(cadena) 
            while ListaOrdenada[i].CodigoArticulo.Codigo == criterio2:              
                while ListaOrdenada[i].Vendedor == criterio3:
                    subtotalvendedor += ListaOrdenada[i].ImporteVendido
                    if i+1 < len(ListaOrdenada):
                        i=i+1
                    else:
                        break
                imprimirVendedor = criterio3
                criterio3 = ListaOrdenada[i].Vendedor
                subtotalarticulo += subtotalvendedor
                cadena = "| {:<9}| {:<23}| {:<21}| ${:<13}| {:<14}| {:<14}| {:<9}|".format("","",imprimirVendedor,round(subtotalvendedor,2),"","","")
                print(cadena)
                subtotalvendedor = 0
                if i+1 == len(ListaOrdenada):
                    if criterio2 != ListaOrdenada[i].CodigoArticulo.Codigo:
                        if criterio1 != ListaOrdenada[i].Sucursal:
                            criterio1 = ListaOrdenada[i].Sucursal
                            imprimirSucursal = criterio1
                            cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| {:<14}| {:<14}| {:<9}|".format(imprimirSucursal,"","","","","","")
                            print(cadena)
                        subtotalsucursal += subtotalarticulo
                        cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| ${:<13}| {:<14}| {:<9}|".format("","","","",round(subtotalarticulo,2),"","")
                        print(cadena)
                        subtotalarticulo = 0
                        criterio2 = ListaOrdenada[i].CodigoArticulo.Codigo
                        imprimirArticulo = criterio2
                        cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| {:<14}| {:<14}| {:<9}|".format("",BuscarArticulo(imprimirArticulo).Descripcion,"","","","","")
                        print(cadena) 
                    imprimirVendedor = criterio3
                    subtotalvendedor = ListaOrdenada[i].ImporteVendido
                    cadena = "| {:<9}| {:<23}| {:<21}| ${:<13}| {:<14}| {:<14}| {:<9}|".format("","",imprimirVendedor,round(subtotalvendedor,2),"","","")
                    print(cadena)
                    subtotalarticulo += subtotalvendedor
                    subtotalvendedor = 0
                    break
            criterio2 = ListaOrdenada[i].CodigoArticulo.Codigo
            subtotalsucursal += subtotalarticulo
            imprimirArticulo = criterio2
            cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| ${:<13}| {:<14}| {:<9}|".format("","","","",round(subtotalarticulo,2),"","")
            print(cadena)
            subtotalarticulo = 0
            if i+1 == len(ListaOrdenada):
                break
        cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| {:<14}| ${:<13}| {:<9}|".format("","","","","",round(subtotalsucursal,2),"")
        print(cadena)
        if imprimirSucursal == criterio1:
            criterio1 = ListaOrdenada[i].Sucursal
        TotalGral += subtotalsucursal
        subtotalsucursal = 0
        if i+1 == len(ListaOrdenada):
            break
    cadena = "| {:<9}| {:<23}| {:<21}| {:<14}| {:<14}| {:<14}|${:<9}|".format("Total","","","","","",round(TotalGral,2))
    print(cadena)
    print("+----------+------------------------+----------------------+---------------+---------------+---------------+----------+")
    MenuPrincipal()

MenuPrincipal()