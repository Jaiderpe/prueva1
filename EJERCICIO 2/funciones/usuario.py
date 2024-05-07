import json
import corefiles.corefiles as cc
import os
import funciones.mundo as fm
import ui.usuario1 as uu


def productos():

    id = input("ingrese la id del producto :")
    nombre = input("ingrese el nombre del producto :")
    produ = input("ingrese valor de unidad del producto :")
    stokma = input("ingrese stokmmain :")
    stok = input("ingrse stokmax :")

    usuario={
        'id': id,
        'nombre' : nombre,
        'produ' : produ,
        'stokma': stokma,
        'stok': stok
    }
    cc.AddData('dataproductos',id,usuario)
    fm.productosdr.get('dataproductos')
    if(bool(input('desea ingresar otro producto s(si) o (no)enter :'))):
        productos(0)
    else :
        uu.usuario1(0)

    
   
 
