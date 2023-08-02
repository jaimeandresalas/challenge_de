from abc import ABC
from google.cloud import bigquery
import pandas as pd
import os

schema_hired_employees = [bigquery.SchemaField("id", "INTEGER"),
                          bigquery.SchemaField("name", "STRING"), 
                          bigquery.SchemaField("datetime", "STRING"), 
                          bigquery.SchemaField("department_id", "INTEGER"),
                          bigquery.SchemaField("job_id", "INTEGER")]

schema_departments = [bigquery.SchemaField("id", "INTEGER"),
                      bigquery.SchemaField("department", "STRING")]

schema_jobs = [bigquery.SchemaField("id", "INTEGER"),
               bigquery.SchemaField("job", "STRING")]

schemas = {'hired_employees': schema_hired_employees,
              'departments': schema_departments,
                'jobs': schema_jobs}

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
                    schema=schemas[name_table],
                    max_bad_records = 1000
                    )
            job = self.client.load_table_from_uri(location, 
                                                  table_name, 
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