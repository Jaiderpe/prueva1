import json
import os

PRODUCTOS  = "data/productos.json"

  
def productos(*param):
    with open(PRODUCTOS , "w") as wf:
        json.dump(param[0],wf,indent=4)



def AddData(*param):
    data =list(param)
    with open(PRODUCTOS ,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})

        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def readfile():
    with open(PRODUCTOS ,'r') as rf:
        return json.load(rf)

def checkfileproductos(*param):
    data = list(param)
    if(os.path.isfile(PRODUCTOS )):
        if(len(param)):
            data[0].update(readfile())
    else:
        if(len(param)):
            productos(data[0])







