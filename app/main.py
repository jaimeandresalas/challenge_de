"""This script execute a simple web server with FastAPI process data with
    - Cloud functions (read and write data in big query) 
    - Dataflow with Beam (write historical data in big query)
Endpoints:
    - /upload: Receives historical data files in CSV format and uploads them to the new database.
    - /batch_insert: Allows the insertion of batch transactions with 1 to 1000 rows in a single request
    - /metrics/hired_employes_2021 : Retrieves metrics related to hired employees in 2021.
    - /metrics/more_hired_2021 : Retrieves metrics related to the most hired employees for deparment in 2021.
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from google.cloud import bigquery
from src.bigquery_operator import OperatorBigQuery

names_tables = {'hired_employees','departments','jobs'}
file_location = 'gs://globant-jasm-1/data_csv/'
project_id = 'de-jasm-globant'
dataset = 'globant_dataset'
app = FastAPI()
Operator = OperatorBigQuery(name_tables= names_tables, 
                            files_location= file_location, 
                            project_id=project_id, 
                            dataset=dataset)

"""Create a api for use Operator BigQuery class and execute the methods insert_batch and hired_employees_2021"""
@app.get("/")
def read_root():
    return JSONResponse({"Hello": "World"})
@app.post("/batch_insert")
async def create_upload_file():
    Operator.insert_batch()
    return JSONResponse({"message": "Files uploaded successfully"})