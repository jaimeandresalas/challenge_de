from abc import ABC
from google.cloud import bigquery
import pandas as pd
import os

"""hired_employees = {"id":int, "name":str,"datetime":str,
                   "department_id":int,"job_id":int}
columns_hired_employees = ['id', 'name', 'datetime', 'department_id', 'job_id']
departments ={ "id": int, "department": str}
columns_departments = ['id', 'department']
jobs ={"id": int, "job": str}
columns_jobs = ['id', 'job']
tables_schema = {"hired_employees" : hired_employees, "jobs" : jobs,
        "departments" : departments}
columns_tables = {"hired_employees" : columns_hired_employees, "jobs" : columns_jobs,
        "departments" : columns_departments}"""

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
            job_config = bigquery.LoadJobConfig(
                    skip_leading_rows=0,
                    source_format=bigquery.SourceFormat.CSV,
                    write_disposition="WRITE_APPEND",
                    autodetect = True,
                    max_bad_records = 1000
                    )
            job = self.client.load_table_from_uri(location=location, 
                                                  table_name = table_name, 
                                                  job_config=job_config)
            job.result()  

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