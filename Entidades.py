
class Articulo:
    def __init__(self, codigo, descripcion, stock, costounitario):
        self.Codigo = codigo
        self.Descripcion = descripcion
        self.Stock = stock
        self.CostoUnitario = costounitario
    def AgregarStock(self, cantidad):
        self.Stock += cantidad
    def DescontarStock(self,cantidad):
        self.Stock -= cantidad
        if self.Stock < 0:
            self.Stock += cantidad
            return False
        else:
            return True
    def ComprobarStock(self, cantidad):
        booleano = self.Stock - cantidad 
        return booleano >= 0
    def __str__(self):
        return f"{self.Codigo} - {self.Descripcion}"

class Venta:
    def __init__(self, fecha, codigoarticulo, vendedor, sucursal, cantidad, numerofactura=0):
        if numerofactura == 0:
            self.CalcularNumeroFactura()
        else:
            self.NumeroFactura = numerofactura
        self.Fecha = fecha
        self.CodigoArticulo = codigoarticulo
        self.Vendedor = vendedor
        self.Sucursal = sucursal
        self.Cantidad = cantidad
        self.CalcularTotalVenta(cantidad)
    def CalcularTotalVenta(self,cantidad):
        self.ImporteVendido =  round(self.CodigoArticulo.CostoUnitario * cantidad,2)
    def CalcularNumeroFactura(self):
        try:
            factura = open("NumeroFactura.dat", "r")
            for lines in factura:
                numero = lines.split("-")
                cabecera = numero[0]
                cuerpo = int(numero[1])
                numeracion = int(numero[2])
            if numeracion == 99999:
                cuerpo += 1
                numeracion = 00000;
            else:
                numeracion += 1
            self.NumeroFactura = cabecera + "-" + str(cuerpo).zfill(5) + "-" + str(numeracion).zfill(5)
            factura.close()
        except:
            self.NumeroFactura = "F-00000-00001"
        finally:
            factura = open("NumeroFactura.dat","w")
            factura.write(self.NumeroFactura)
    def __str__(self):
        return f"{self.NumeroFactura} - {self.CodigoArticulo.Descripcion}"






