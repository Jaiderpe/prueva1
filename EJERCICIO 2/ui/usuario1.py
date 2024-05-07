import funciones.usuario as fu
import corefiles.corefiles as cc
import funciones.mundo as fm

def productos1(op):
   fm.borrar_pantalla()
   tittle = """
   **********************
   ** CENTRO PRODUCTOS  *
   **********************
   """   
   productos1 = "1. productos \n2. salir" 
   if (op !=2):
      print(tittle)
      print(productos1)
      try:
         opcion = int(input(':) '))
      except ValueError:
         input("Error en la opcion ingresada")  
         fm.pausar_pantalla
         productos1(0)
      else:
         match(opcion):
            case 1:
               fu.productos(0)
            case 2:
               print("hasta luego")
               fm.pausar_pantalla()
            case _:
               print("opcion no valida")
               fm.pausar_pantalla
               productos1(0)
if __name__=='__usuario__':
   cc.checkfileproductos(fm.productosdr)
   cc.PRODUCTOS  = "data/productos.json"
   productos1(0)