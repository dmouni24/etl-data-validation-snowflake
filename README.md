# ETL Testing Framework – Snowflake + Informatica

This project demonstrates ETL validation using:
- **Snowflake**: Data warehouse for storing and querying data
- **Informatica**: ETL pipeline
- **Python + SQL**: For data comparison and validation

## Features
- Validates row count and field-level accuracy
- Compares staging vs target tables using SQL
- Generates test reports using PyTest and Allure

## Technologies Used
- Python, SQL
- Snowflake Connector
- Informatica Cloud
- Jenkins (optional CI)

## Getting Started
1. Clone this repo
2. Add your Snowflake and Informatica credentials to `.env`
3. Run `python etl_validator.py`
<img width="468" height="301" alt="image" src="https://github.com/user-attachments/assets/5fd841d9-4751-4e97-ab0c-a59cc37846af" />
