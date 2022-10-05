import serial
import time
from tabulate import tabulate
from datetime import datetime
from turtle import clear
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

try:
    puerto = serial.Serial('COM7',9600)
    puerto.close()
    puerto.open()
    print ("Port is open")
except:
    print("Problem open the port")

class definir_datos:
    def __init__(self,temp,fecha):
        self.temp = temp
        self.fecha = fecha

    def save(self):
        file = open('Databases\ArchivoDatos.csv','w')
        for i in range (0, len(self.temp)):
            t = str(self.temp[i])
            f = str(self.fecha[i])
            file = open('Databases\ArchivoDatos.csv','a')
            linea = ";".join([t,f])
            file.write(linea+"\n")
            file.close()

def Parametros():
    file = open('ArchivoParametros.csv','w')
    mn_H = int(input("Valor mínimo Hipotermia: "))
    mx_H = int(input("Valor máximo Hipotermia: "))
    mn_N = int(input("Valor mínimo normal: "))
    mx_N = int(input("Valor máximo normal: "))
    mn_F = int(input("Valor mínimo fiebre: "))
    mx_F = int(input("Valor máximo fiebre: "))
    
    hipotermia = ";".join([str(mn_H),str(mx_H),"H"])
    normal = ";".join([str(mn_N), str(mx_N),"N"])
    fiebre = ";".join([str(mn_F),str(mx_F),"F"])

    #Guardar en archivo
    file.write(hipotermia+"\n")
    file.write(normal+"\n")
    file.write(fiebre+"\n")
    file.close()

def lect_Parametros():
    h = []
    n = []
    f =[]
    p = open('Databases\ArchivoParametros.csv','r')
    paramet = p.readlines()

    for i in range (0,3):
        par = paramet[i]
        par = par.split(';')

        if i == 0:
            h.append(int(par[0]))
            h.append(int(par[1]))

        elif i == 1:
            n.append(int(par[0]))
            n.append(int(par[1]))

        elif i == 2:
            f.append(int(par[0]))
            f.append(int(par[1]))
        else:
            continue
        
    return h,n,f

def LED(dato):
    h,n,f = lect_Parametros()
    #Derecha 
    if dato >= h[0] and dato <= h[1]:
        temp = "H"
    #Centro
    elif dato >= n[0] and dato <= n[1]:
        temp = "N"
    #Izquierda
    elif dato >= f[0] and dato <= f[1]:
        temp = "F"
            
    puerto.write(temp.encode())

''' CAPTURA DE DATOS'''
#POR CANTIDAD
def Capturar_Datos(temp, fecha):

    dato = int(puerto.readline().decode().strip())
    temp.append(dato)
    fecha.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
    LED(dato)
    return temp, fecha

def datosCant():
    t = []
    f = []
    cant = int(input ("Cantidad de datos: "))
    for i in range (0, cant):
        t, f= Capturar_Datos(t, f)
        i = i+1

    d = definir_datos(t,f)
    return d

#POR GRÁFICA
def onclick(event):
    global pausa
    print ("pausa")
    pausa = True
pausa = False
def captura_grafica():
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event',onclick)
    temp=[]
    fecha = []
    def update_data(frames):
        if not pausa:
            punto = puerto.readline().decode().strip()
            temp.append(punto)
            f = datetime.now().strftime("%c")
            fecha.append(f)
            ax.clear()
            ax.plot(temp) 
            LED(int(punto))

        return(temp, fecha)

    ani = animation.FuncAnimation(fig,update_data)
    plt.show()
    dato = definir_datos(temp,fecha)
    return dato

'''REPORTES'''
def grafico():
    df = pd.read_csv('Databases\ArchivoDatos.csv', sep= ';')
    df.columns = ['Temperatura','Fecha']
    plt.plot(df['Fecha'],df['Temperatura'])
    plt.show()

def valor_max_min_prom():
    df = pd.read_csv('Databases\ArchivoDatos.csv', sep= ';')
    df.columns = ['Temperatura','Fecha']

    max_t = df['Temperatura'].max() 
    fech_max = str(df['Fecha'][df['Temperatura'].idxmax()])

    min_t = df['Temperatura'].min() 
    fech_min = str(df['Fecha'][df['Temperatura'].idxmin()])

    prom_t = df['Temperatura'].mean()

    print("Maxima temperatura : ",max_t,"en",fech_max)  
    print("Mínima temperatura : ",min_t,"en",fech_min)  
    print("Promedio temperatura: ",prom_t)  