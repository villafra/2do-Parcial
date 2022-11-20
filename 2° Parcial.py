from curses import init_pair
from Entidades import *

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
           quit()
   else:
        MenuPrincipal() 

def MenuArticulos():
    print("Por favor elija un item del menu:")
    print("1-Alta Articulo")
    print("2-Modificar Articulo")
    print("3-Eliminar Articulo")
    print("4-Agregar Stock Articulo")
    print("5-Salir")
    try:
        menu1= int(input())
    except ValueError:
            MenuArticulos()
    while menu1 < 6:
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
        menu1= int(input())
    except ValueError:
            MenuVentas()
    while menu1 < 5:
        if menu1 == 1:
            NuevaVenta()
            break
        elif menu1 == 2:
            ModificarVenta()
            break
        elif menu1 == 3:
            EliminarVenta()
            break
        elif menu1 == 4:
           MenuPrincipal()
            break
    else:
        MenuVentas()

def AltaArticulo():
    CrearArchivo = open("ListadoArticulos.txt", "a")
    print("Ingrese Código del nuevo Artículo:")
    codigo = input()
    print ("Ingrese descripción del nuevo Artículo:")
    descripcion = input()
    print ("Ingrese Stock Inicial:")
    stock = int(input())
