from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
  'owner': 'Admin',
  'depends_on_past': False,
  'start_date': datetime(2023, 2, 23)
}


dag = DAG('firstDAG', default_args=default_args)

t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
        dag=dag
)

t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
        dag=dag
    )

t1 >> t2
