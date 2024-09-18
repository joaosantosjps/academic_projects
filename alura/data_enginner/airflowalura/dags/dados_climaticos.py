import pendulum
import pandas as pd
from os.path import join
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.macros import ds_add


with DAG(
    "dados_climaticos",
    start_date=pendulum.datetime(2022, 8, 22, tz="UTC"),
    schedule_interval="0 0 * * 1", #execultar toda segunda feria
) as dag:
    
    tarefa_1 = BashOperator(
        task_id="cria_pasta",
        bash_command="mkdir -p '/home/joao-santos/Desktop/academic_projects/alura/data_enginner/airflowalura/semana={{data_interval_end.strftime('%Y-%m-%d')}}'"
    )

    def extrai_dados(data_interval_end):
        city = 'Boston'
        key = 'TC63D9RSZEQQQXABW4SK25275'

        url = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
                f"{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv")

        dados = pd.read_csv(url)

        file_path = f"/home/joao-santos/Desktop/academic_projects/alura/data_enginner/airflowalura/semana={data_interval_end}/"

        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

    tarefa_2 = PythonOperator(
        task_id="extrai_dados",
        python_callable=extrai_dados,
        op_kwargs={"data_interval_end": "{{data_interval_end.strftime('%Y-%m-%d')}}"}
    )
    
    tarefa_1 >> tarefa_2
