#!/bin/bash
echo "Running ETL validations..."

snowsql -f snowflake/validation/validate_row_count.sql
snowsql -f snowflake/validation/validate_null_check.sql
