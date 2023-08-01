from abc import ABC
from google.cloud import bigquery
import pandas as pd
import os

class OperatorBigQuery(ABC):
    def __init__(self, name_tables:dir, files_location:str, project_id:str, dataset:str, **kwargs):
        self.client = bigquery.Client()
        self.name_tables = name_tables
        self.files_location = files_location
        self.project_id = project_id
        self.dataset = dataset
    
    @name_tables.setter
    def name_tables(self,name_tables):
        self._name_tables = name_tables
    
    @files_location.setter
    def files_location(self,files_location):
        self._files_location = files_location
    
    @project_id.setter
    def project_id(self,project_id):
        self._project_id = project_id
    
    @dataset.setter
    def dataset(self,dataset):
        self._dataset = dataset

    def insert_batch(self):
        for name_table in self._name_tables:
            table_name = self._project_id+'.'+self._dataset+'.'+name_table
            df = pd.read_csv(self._files_location+name_table+'.csv')
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