def pesosdolar(pesos):
    return pesos/ 3944
def pesoseuro(pesos):
    return pesos/ 4279
def pesoyen(pesos):
    return pesos/ 26.30
def europeso(pesos):
    return pesos/ 26.30

def main():
    print("1 ingrese valor de pesos a dolar :")
    print("2 ingrese valor de pesos a euros :")
    print("3 ingrese valor de euros a pesos :")
    print("4 ingrese valor de pesos a yenes :")

    opcion = int(input('ingrese opcion que desea :'))

    if opcion ==1:
        pesos = float(input('ingrese peso a convertir en dolar :'))
        print('el equivalente ','el dolar es :',pesosdolar(pesos))
    elif opcion ==2:
        pesos = float(input('ingrese peso a convertir en euro :'))
        print('el equivalente','el euro es :',pesoseuro(pesos))
    elif opcion ==3:
        pesos = float(input('ingrese peso a convertir en yen :'))
        print('el equivalente','en yen es :',pesoyen(pesos))
    elif opcion ==4:
        pesos = float(input('ingrese euro a convertir en peso :'))
        print('el equivalente','en peso es :',europeso(pesos))

if __name__=='__main__':
  main()