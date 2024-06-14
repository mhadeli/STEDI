# AWS-Data-Lakehouse

This repository contains the STEDI project for Udacity's Data Engineering with AWS Nanodegree Program. The project focuses on building an ELT pipeline using various AWS services to create a data lakehouse architecture.

## Project Overview

The STEDI project involves creating a data lakehouse to process and analyze user balance and step data. The data pipeline leverages AWS services such as S3, Redshift, and Glue to extract, transform, and load data into a Redshift data warehouse for analysis.

## Architecture

- **AWS S3**: Used as a data lake to store raw and processed data.
- **AWS Glue**: Utilized for ETL operations, including data transformation and loading into Redshift.
- **AWS Redshift**: Serves as the data warehouse for storing processed data and running analytical queries.
- **AWS IAM**: Manages access control and permissions for AWS resources.

## Features

- **Data Ingestion**: Raw data is ingested into S3 buckets.
- **Data Transformation**: AWS Glue jobs are used to clean and transform the data.
- **Data Loading**: Transformed data is loaded into Redshift tables.
- **Data Analysis**: Redshift is used to run queries and analyze the processed data.

## Getting Started

### Prerequisites

- AWS account with necessary permissions for S3, Redshift, and Glue.
- IAM roles and policies configured for access control.

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mhadeli/STEDI.git
    cd STEDI
    ```

2. **Configure AWS CLI**:
    ```bash
    aws configure
    ```

3. **Create S3 Buckets**:
    - Create S3 buckets for raw and processed data.

4. **Deploy Glue Jobs**:
    - Set up and deploy AWS Glue jobs for data transformation.

5. **Create Redshift Cluster**:
    - Set up a Redshift cluster and create necessary tables.

### Running the Pipeline

1. **Ingest Data**:
    - Upload raw data files to the S3 bucket.

2. **Run Glue Jobs**:
    - Execute AWS Glue jobs to transform and load data into Redshift.

3. **Query Data**:
    - Use SQL queries to analyze data in the Redshift data warehouse.

## Repository Structure

- `scripts/`: Contains Python scripts for data transformation and loading.
- `config/`: Configuration files for AWS resources.
- `data/`: Sample data files used for testing.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## Acknowledgments

- Udacity for providing the Data Engineering with AWS Nanodegree Program.
- AWS for the cloud infrastructure and services used in this project.

