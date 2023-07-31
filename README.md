# Globant’s Data Engineering Coding Challenge [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]
## Authors
- [@jaimeandresalas](https://github.com/jaimeandresalas)

## Table of Contents
1. [General Info](#general-info)
2. [Section 1: API](#api)
3. [Section 2: SQL](#sql)
4. [Bonus Track](#bonus-track)
5. [Contribution Guidelines](#contribution-guidelines)

### General Info
Welcome to the repository for the programming challenge as a Sr. Data Engineer! In this project, we have addressed various sections related to software development and data management. Below, you will find a detailed explanation of the repository's contents and how to navigate through it.

### Section 1: API
In the context of a database migration involving three different tables (departments, jobs, employees), we have developed a local REST API that fulfills the following requirements:

 1. Receives historical data from CSV files.
 2. Uploads these files to the new database.
 3. Allows the insertion of batch transactions, supporting one request to insert 1 up to 1000 rows.

#### Configuration and Execution
 1. Ensure you have Python 3.x installed on your system.
 2. Create a virtual environment using virtualenv or conda.
 3. Install the necessary dependencies by executing pip install -r requirements.txt.
 4. Run the API using the command python api.py.
 5. The API will be available at http://localhost:8000.

#### Endpoints Available
- POST /upload: Receives historical data files in CSV format and uploads them to the new database.
- POST /batch_insert: Allows the insertion of batch transactions with 1 to 1000 rows in a single request.

### Section 2: SQL
In this section, we explore the data that was inserted in the previous section. We have created specific endpoints to fulfill the stakeholders' requests for various metrics.

#### Endpoints Available

- `GET /metrics/department`: Retrieves metrics related to departments.
- `GET /metrics/job`: Retrieves metrics related to jobs.
- `GET /metrics/employee`: Retrieves metrics related to employees.

### Bonus Track
In this section, we have added enhancements to make the solution more robust and scalable.
#### Cloud

- `cloud_deployment.md`: Documentation on how to deploy the API and database in a public cloud environment using services deemed appropriate for the task.

#### Testing

- `tests/`: This directory contains automated tests for the API. We have utilized various testing libraries to ensure the functionality and reliability of the API.

#### Containers

- `Dockerfile`: A configuration file to create a Docker container that encapsulates the API and its dependencies. This containerized application can be deployed seamlessly in different environments.

### Contribution Guidelines

If you wish to contribute to this project, we welcome your contributions! Follow these steps to get started:

1. Fork this repository and clone it to your local machine.
2. Create a new branch for your work: `git checkout -b feature/your-new-feature`.
3. Make your changes and improvements in the branch.
4. Ensure that the tests pass successfully.
5. Commit your changes: `git commit -m "Add your descriptive message"`.
6. Push your changes to your repository: `git push origin feature/your-new-feature`.
7. Open a pull request for us to review your changes and incorporate them into the main project.

Thank you for contributing, and we hope you enjoy solving this challenge!