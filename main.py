from Clases.menu import *
from Clases.datos import *
import serial

try:
    puerto = serial.Serial('COM7',9600)
    puerto.close()
    puerto.open()
    print ("Port is open")
except:
    print("Problem open the port")
    
def main():
    menu = Menu("Paciente")
    op=menu.ver()

    if op == "1":
        Parametros()

    elif op == "2":
        #Captura de datos
        menu2 = MenuCapturaDeDatos()
        op2 = menu2.ver()

        if op2 == "1":
            dato = datosCant()
            dato.save()

        elif op2 == "2":
            dato = captura_grafica()
            dato.save()
        else:
            main()

    elif op == "3":
        # Reportes
        menu3= MenuReportes()
        op2 = menu3.ver()
    
        if op2 == "1":
            grafico()

        elif op2 == "2":

            valor_max_min_prom()
        else:
            main()
            
    main()

if __name__=='__main__':
    main()
