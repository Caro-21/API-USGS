#Dinora Carolina Salazar Viera
#Cliente que consulta la api de Terremotos de USGS

import requests
from datetime import datetime, timedelta

def get_earthquakes(starttime, endtime, min_magnitude=5.0, max_magnitude=10.0):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",           #formato de la respuesta
        "starttime": starttime,        #fecha de inicio
        "endtime": endtime,            #fecha fin
        "minmagnitude": min_magnitude, #magnitud minima
        "maxmagnitude": max_magnitude  #magnitud máxima
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['features'] #lista de eventos
    else:
        print(f"Error: {response.status_code}")
        return None

#busca los terremotos de los ultimos 5 días
end_date = datetime.now()
start_date = end_date - timedelta(days=5)
earthquakes = get_earthquakes(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

if earthquakes:
    print(f"{'Lugar':<50} {'Magnitud':<10} {'Fecha'}")
    print("=" * 70)
    #muestra los primeros 10 terremotos
    for quake in earthquakes[:10]:
        place = quake['properties']['place']
        magnitude = quake['properties']['mag']
        time = datetime.fromtimestamp(quake['properties']['time'] / 1000)
        print(f"{place:<50} {magnitude:<10} {time.strftime('%Y-%m-%d %H:%M:%S')}")
