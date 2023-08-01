from abc import ABC
from google.cloud import bigquery
import pandas as pd
import os

hired_employees = {{"name": "id", 'type': 'INTEGER'},
                        {"name": "name", 'type': 'STRING'},
                        {"name": "datetime", 'type':'STRING'},
                        {"name": "department_id", 'type': 'INTEGER'},
                        {"name": "job_id", 'type': 'INTEGER'}}
departments ={{"name": "id", 'type': 'INTEGER'},
                    {"name": "departments", 'type': 'STRING'},},
jobs ={{"name": "id", 'type': 'INTEGER'},
      {"name": "job", 'type': 'STRING'}}
dict_tables = {'hired_employees': hired_employees,
               'departments': departments,
               'jobs': jobs}
class OperatorBigQuery(ABC):
    def __init__(self, name_tables, files_location:str, project_id:str, dataset:str):
        self.client = bigquery.Client()
        self.name_tables = name_tables
        self.files_location = files_location
        self.project_id = project_id
        self.dataset = dataset
    
    def insert_batch(self):
        for name_table in self.name_tables:
            table_name = self.project_id+'.'+self.dataset+'.'+name_table
            location = self.files_location+name_table+'.csv'
            df = pd.read_csv(location, sep=',',
                             encoding='utf-8',
                             header=None, 
                             on_bad_lines = 'warn',
                             storage_options={"token": "cloud"})
            df.to_gbq(table_name, if_exists='append', 
                      chunksize=1000,
                      table_schema=dict_tables[name_table])
   
    def hired_employees_2021(self):
        with open(os.path.abspath("./src/queries/hired_employees_2021.sql"), "r") as f:
            sql = f.read()
        query_job = self.client.query(sql)
        return query_job.to_json()
    
    def more_hired_2021(self):
        with open(os.path.abspath("./src/queries/more_hired_2021.sql"), "r") as f:
            sql = f.read()
        query_job = self.client.query(sql)
        return query_job.to_json()