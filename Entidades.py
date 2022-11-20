


class Articulo:
    def __init__(self, codigo, descripcion, stock, costounitario):
        self.Codigo = codigo
        self.Descripcion = descripcion
        self.Stock = stock
        self.CostoUnitario = costounitario
    def __str__(self):
        return f"{self.Codigo} - {self.Descripcion}"

class Venta:
    def __init__(self, fecha, codigoarticulo, vendedor, sucursal, cantidad, importevendido):
        self.Fecha = fecha
        self.CodigoArticulo = codigoarticulo
        self.Vendedor = vendedor
        self.Sucursal = sucursal
        self.Cantidad = cantidad
        self.ImporteVendido = CalcularTotalVenta()
    def CalcularTotalVenta(self):
        return self.CodigoArticulo.CostoUnitario * cantidad
    def __str__(self) -> str:
        return f"{self.Fecha} - {self.CodigoArticulo} - {self.ImporteVendido}






