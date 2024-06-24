import json

with open("crime_history.json","r") as archivo:
    datos_leidos = json.load(archivo)


archivo_json = "crime_history.json"

def read_data():
    try:
        with open(archivo_json,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

read_data()
contador_tipo = 0

for i in read_data():

    if i['tipo'] == "Robo con violencia o intimidacion":
        contador_tipo += 1

    if i['tipo'] == "Hurto":
        contador_tipo += 1

    if i['tipo'] == "Estafa":
        contador_tipo += 1  
        print("Total de tipo: ", contador_tipo)  
          

        
        

