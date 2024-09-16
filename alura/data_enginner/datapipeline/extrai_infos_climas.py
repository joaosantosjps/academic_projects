import os
import pandas as pd
from os.path import join
from datetime import datetime, timedelta

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
key = 'TC63D9RSZEQQQXABW4SK25275'

url = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
           f"{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv")

dados = pd.read_csv(url)
print(dados.head())

file_path = f"/home/joao-santos/Desktop/academic_projects/alura/data_enginner/datapipeline/semana={data_inicio}/"
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')