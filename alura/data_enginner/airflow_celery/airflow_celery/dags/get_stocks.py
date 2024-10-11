import yfinance
import pendulum
from pathlib import Path

from airflow.macros import ds_add
from airflow.decorators import dag, task


TICKERS = [
    "AAPL",
    "MSFT",
    "GOOG",
    "TSLA"
]

@task()

def get_history(ticker, ds=None, ds_nodash=None):
        file_path = f"/home/joao-santos/Desktop/academic_projects/alura/data_enginner/airflow_celery/stocks/{ticker}/{ticker}_{ds_nodash}.csv"
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        yfinance.Ticker(ticker).history(
            period ="1d",
            interval = "1h",
            start = ds_add(ds, -1),
            end = ds,
            prepost = True
                        ).to_csv(file_path)
        

@dag(
    schedule_interval="0 0 * * 2-6",
    start_date=pendulum.datetime(2024, 2, 1, tz="UTC"),
    catchup=True
)

def get_stocks_dag():
        for ticker in TICKERS:
            get_history.override(task_id=ticker)(ticker)

dag = get_stocks_dag() 