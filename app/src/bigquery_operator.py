from abc import ABC
from google.cloud import bigquery
from google.cloud import storage
import pandas as pd
import os

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
            #storage_client = storage.Client()
            #bucket = storage_client.get_bucket('globant-jasm-1')
            #blob = bucket.blob('data_csv/'+name_table+'.csv')
            #blob.download_to_filename('/tmp/'+name_table+'.csv')
            location = self.files_location+name_table+'.csv'
            df = pd.read_csv(location, sep=',')
            df.to_gbq(table_name, if_exists='append', chunksize=1000)
   
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