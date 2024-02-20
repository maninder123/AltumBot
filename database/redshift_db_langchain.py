import os
from langchain.sql_database import SQLDatabase
# from .constants_db import port, password, user, host, dbname

# Replace these values with your Redshift connection details
redshift_user = "analytics_read"
redshift_password = "zxLYY86vD,6f"
redshift_host = "altumblack-analytics.c623li0efetw.us-east-1.redshift.amazonaws.com"
redshift_port = "5439"
redshift_dbname = "analytics"
redshift_schema = "bebe"  # Specify your schema here

# Construct the Redshift connection URI
redshift_url = f"redshift+psycopg2://{redshift_user}:{redshift_password}@{redshift_host}:{redshift_port}/{redshift_dbname}"
# Specify the schema and table name
#redshift_schema = "bebe"
TABLE_NAME = "orders"

# Create an instance of SQLDatabase for Redshift
db = SQLDatabase.from_uri(
    redshift_url,
    # include_schemas=[redshift_schema],
    #include_tables=[TABLE_NAME],
    sample_rows_in_table_info=1,
)
print('Maninder ----------db -------', db)