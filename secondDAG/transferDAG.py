from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from secondDAG.exporter import export_raw
from secondDAG.importer import importToTxt

dag = DAG("transferDAG", start_date=datetime(2023, 2, 23, 12), description='Перевод csv в txt с форматированием запятых',
             schedule_interval="0 * * * *", catchup=False
)

filePathExport = '/home/dgsoroka/Documents/VSWorkSpaces/AirflowTest/DAGs/secondDAG/used_car_dataset.csv'
dataArray = export_raw(filePathExport)


task_1 = PythonOperator(
  task_id='task_1',
  python_callable=export_raw,
  op_kwargs={'filePathExport': filePathExport},
  dag=dag
)

task_2 = PythonOperator(
  task_id='task_2',
  python_callable=importToTxt,
  op_kwargs={'dataArray': dataArray, 'txtFileName': 'output.txt'},
  provide_context=True,
  dag=dag
)


task_1 >> task_2
