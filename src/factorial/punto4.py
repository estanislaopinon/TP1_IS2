# Implemente una clase “factura” que tenga un importe correspondiente
# al total de la factura pero de acuerdo a la condición impositiva del
# cliente (IVA Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal condición.

class Factura:
    def __init__(self, importe):
        self.importe = importe

    def generar_factura(self):
        pass


class IVA_Responsable(Factura):
    def generar_factura(self):
        print(
            f"Su condicion: IVA Responsable. Factura por un importe de: {self.importe}")


class IVA_No_Inscripto(Factura):
    def generar_factura(self):
        print(
            f"Su condicion: IVA No Inscripto. Factura por un importe de: {self.importe}")


class IVA_Excento(Factura):
    def generar_factura(self):
        print(
            f"Su condicion: IVA Excento.Factura por importe de:{self.importe}")


class Factura_Factory:
    def generar_factura(self, condicion, importe):
        if condicion == "responsable":
            return IVA_Responsable(importe)
        elif condicion == "no inscripto":
            return IVA_No_Inscripto(importe)
        elif condicion == "excento":
            return IVA_Excento(importe)
        else:
            ValueError("Condicion no valida")


factura = Factura_Factory()

factura_responsable = factura.generar_factura("responsable", 500)
factura_responsable.generar_factura()

factura_no_inscripto = factura.generar_factura("no inscripto", 1200)
factura_no_inscripto.generar_factura()

factura_excento = factura.generar_factura("excento", 5000)
factura_excento.generar_factura()
