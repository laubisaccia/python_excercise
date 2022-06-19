#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from funciones_censo import cantidad_habitantes, nombre_largo, solos,viviendas_solos
from funciones_censo import menores, menor_salario,sin_vehiculo, departamentos
from funciones_censo import covid_positivo, guardar
censo = []



while True:
    while True:
        try:
            
            integrantes = int(input('Ingrese cantidad de integrantes de la familia: '))
            break
        except:
            print('Debes ingresar un numero valido de integrantes')
    
    if integrantes == 0:
        break
       
    nombre_jefe = input('Ingrese el nombre del jefe o jefa de la familia: ')
    
    while nombre_jefe:
        try:
            cantidad_menores = int(input('Ingrese la cantidad de menores de 18 años: '))
            break
        except Exception:
            print('Ingrese una cantidad valida de menores')
          
    while cantidad_menores or cantidad_menores == 0:
        try:
            cantidad_mayores = int(input('ingrese la cantidad de mayores de 65 años: '))
           
            break
        except Exception:
            print('ingrese una cantidad valida de mayores de 65 años')
            
    while cantidad_mayores or cantidad_mayores == 0:
        try:
            edad_joven = int(input('Ingrese la edad de la persona mas joven: '))
            break
        except Exception:
            print('ingrese una edad valida de la persona mas joven')
    while edad_joven:
        try:
            edad_viejo = int(input('Ingrese la edad de la persona mas vieja: '))
            break
        except Exception:
            print('ingrese una edad valida para la persona mas vieja')
    while edad_viejo:
        try:
            ingreso_salarial = int(input('Ingrese el salario familiar: '))
            break
        except Exception:
            print('Ingrese un salario valido numerico')
            
    while ingreso_salarial:
        try:
            vehiculo = input('Posee vehiculo (s/n)?: ')
            if(vehiculo == "S" or vehiculo == 's'):
                cantidad_vehiculo_por_familia= int(input('Ingrese cantidad de vehiculos: '))  
                break
            elif(vehiculo == "N" or vehiculo == 'n'):
                cantidad_vehiculo_por_familia= 0
                break
            else:
                print('Ingrese si posee o no vehiculo')
           
        except Exception:
            print('ingrese si posee o no vehiculo')
          
    while vehiculo:
        try:           
            depto = input('Vive usted en departamento (s/n)?: ')    
            if(depto == "S" or depto == 's'):
                metros_cuadrados = int(input('Ingrese los metros cuadrados: '))
                break
            elif(depto == "N" or depto == 'n'):
                metros_cuadrados = 0
                break
            else:
                print('ingrese si vive o no vive en departamento')
        except Exception:
            print('ingrese si vive o no vive en departamento')
  
    while depto:
        try:
            covid =int(input('Ingrese cantidad de personas que tuvieron covid: '))
            break
        except Exception:
            print('Ingrese la cantidad de personas que tuvieron covid')
            
        
    dato = {
        'integrantes' : '',
        'nombre_jefe' : '',
        'cantidad_menores' : '',
        'cantidad_mayores' : '',
        'edad_joven' : '',
        'edad_viejo' : '',
        'ingreso_salarial' : '',
        'cantidad_vehiculo_por_familia' :'',
        'metros_cuadrados' :'',
        'covid':''
        }
    
    dato['integrantes' ] = integrantes
    dato['nombre_jefe' ] = nombre_jefe
    dato[ 'cantidad_menores'] = cantidad_menores
    dato['cantidad_mayores'] = cantidad_mayores
    dato['edad_joven' ] = edad_joven
    dato['edad_viejo' ] = edad_viejo
    dato['ingreso_salarial'  ] = ingreso_salarial
    dato['cantidad_vehiculo_por_familia' ] = cantidad_vehiculo_por_familia
    dato['metros_cuadrados' ] = metros_cuadrados
    dato['covid'] = covid
    
    censo.append(dato)
   
    
print(censo)

cantidad_habitantes(censo)
nombre_largo(censo)
solos(censo)
viviendas_solos(censo)
menores(censo)
menor_salario(censo)
sin_vehiculo(censo)
departamentos(censo)
covid_positivo(censo)
guardar(censo)
    
    