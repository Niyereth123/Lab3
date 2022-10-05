class Menu:    
    def __init__(self,p):
        self.p = p
    def ver(self):
        print("SISTEMA DE MONITOREO DE TEMPERATURA ")
        print("1. Configuración de parámetros")
        print("2. Captura de datos")
        print("3. Reportes")
        op=input(">>>")
        return op

class MenuCapturaDeDatos():
    def ver(self):
        print("CAPTURA DE DATOS")
        print("1. Cantidad de datos ")
        print("2. Gráfica en tiempo real")
        op=input(">>>")
        return op

class MenuReportes():
    def ver(self):
        print("MENU REPORTES".center(20,"*"))
        print("1. Gráfica de los datos capturados")
        print("2. Valores máximo, mínimo y promedio de temperatura")
        op=input(">>>")
        return op


if __name__=='__main__':
    m = Menu("P")
    m.ver()