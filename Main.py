##Vincen Andres Cabrera Yuco
##Sistema de control de un robot movil diferencial
#Ingenieria Mecatronica
import threading
import math as m
import numpy as np
#Clase de velovidad angular aplicada
class Velcanfapl:

    def __init__(self):
        self.t=0
        self.theta=0
        self.v=0
        self.w=0
    
    def vcart(self,v):#Variables de velocidad cartesiana
        
        mat1 = np.array([[m.cos(self.theta),m.sin(self.theta)],
              [-m.sin(self.theta), m.cos(self.theta)],
              [0, 1]])
        mat2=np.array([[v], 
              [self.w]])
        return np.dot(mat1, mat2)

    def vmov(self,mvcart):#Vector de movimiento en el marco local
        mat1 = np.array([[m.cos(self.theta), -m.sin(self.theta), 0],
              [-m.sin(self.theta), m.cos(self.theta), 0],
              [0, 0, 1]])
        return np.dot(mat1, mvcart)
    
    def vang(self,mvmov,l):#Vector de velocidad angular aplicada 
        j1= np.array([[m.sin((m.pi/2)+(m.pi)), -m.cos((m.pi/2)+(m.pi)), -l*m.cos(m.pi)],
              [m.sin((-(m.pi/2))), -m.cos(-(m.pi/2)), -l*m.cos(0)]])
        j2inv= np.array([[1/35, 0],
              [0, 1/35]])
        mat1=np.dot(j2inv, j1)
        return np.dot(mat1,mvmov)

    def restxt(self,mvang):#Funcion de registro de resultados 
        datos = np.column_stack((self.t, mvang[0], mvang[1]))
    # Guardar el arreglo en un archivo txt
        with open('resultado.txt', 'a', encoding='utf-8') as archivo:
            for fila in datos:
                # Convertir cada fila a una cadena de texto sin llaves
                linea = ','.join(map(str, fila))
                archivo.write(linea + '\n')

        
velcanfapl= Velcanfapl()
with open('resultado.txt', 'a', encoding='utf-8') as archivo:
    # Escribir el encabezado
    archivo.write('t,𝜑Iz,𝜑De\n')
# Read the txt file
with open('datos.txt', 'r') as archivo:
    archivo.readline()
    for linea in archivo:
        # Eliminar espacios en blanco al principio y al final de la línea
        linea = linea.strip()
        # Separar la línea por comas y convertir los elementos a enteros
        numeros = [float(num) for num in linea.split(',')]
        # Hacer algo con los números, por ejemplo, imprimirlos
        velcanfapl.t=numeros[0]
        velcanfapl.theta=numeros[1]
        velcanfapl.v=numeros[2]
        velcanfapl.w=numeros[3]
        mvcart=velcanfapl.vcart(10)
        mvmov=velcanfapl.vmov(mvcart)
        mvang=velcanfapl.vang(mvmov,80)
        velcanfapl.restxt(mvang)
        
    
    

