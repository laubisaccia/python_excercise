#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 13:41:55 2022

@author: laubisaccia
"""
import csv

def cantidad_habitantes(censo):
    habitantes = 0
    for item in censo:
        habitantes = item['integrantes'] + habitantes
        
    print('la cantidad de personas censadas es de : {}'.format(habitantes))
    return
       
    
def nombre_largo(censo):
    largo = 0
    for item in censo:
        if len(item['nombre_jefe']) > largo:
            largo = len(item['nombre_jefe'])
            nombre = item['nombre_jefe']
            
            
    print('El nombre de jefe/a mas largo es el de: {}'.format(nombre))
    return
  
def solos(censo):
    solos = 0
    for item in censo:
        if item['integrantes'] == 1:
            solos = solos + 1
            
    print('La cantidad de personas que viven solas es de: {}'.format(solos))
    return
    
def viviendas_solos(censo):
    viviendas=0
    solos = 0
    for item in censo:
        viviendas = viviendas + 1
        if item['integrantes'] == 1:
            solos = solos + 1
    
    porcentaje_viviendas_solos = (solos * 100) /viviendas
    
    print('El porcentaje de viviendas donde viven personas solas es de: {} %'.format(porcentaje_viviendas_solos))
    return

def menores(censo):
    menores = 0
    for item in censo:
        menores = menores + item['cantidad_menores']
        
    print('La cantidad de menores censados es de {}'.format(menores))
    return

def menor_salario(censo):
     salario = censo[0]['ingreso_salarial']
     for item in censo:
         if item['ingreso_salarial'] <= salario:
             salario = item['ingreso_salarial']
             
     print('El salario mas bajo es de : ${}'.format(salario))
     return
     
def sin_vehiculo(censo):
    sin_vehiculo = 0
    for item in censo:
        if item['cantidad_vehiculo_por_familia'] == 0:
            sin_vehiculo = sin_vehiculo + 1
    print('La cantidad de familias sin vehiculo es de: {}'.format(sin_vehiculo))
            
def departamentos(censo):
    
    deptos = 0
    metros = 0
    for item in censo:
        if item['metros_cuadrados'] != 0:
            deptos = deptos + 1
            metros = metros + item['metros_cuadrados']
            
    print('La cantidad de familias que viven en departamentos es de: {}'.format(deptos))
    print('El promedio de metros cuadrados es de: {:.2f}'.format(metros/deptos))
    return
            
def covid_positivo(censo):
    covid = 0
    for item in censo:
        covid = covid + item['covid']
        
    print('La cantidad de personas que tuvieron covid es de: {}'.format(covid))
    return
        
def guardar(censo):
    
    fieldnames=['integrantes' , 'nombre_jefe', 'cantidad_menores', 'cantidad_mayores', 'edad_joven', 'edad_viejo','ingreso_salarial','cantidad_vehiculo_por_familia', 'metros_cuadrados', 'covid' ]
    with open('censo.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows(censo) 
    return
        
  
        