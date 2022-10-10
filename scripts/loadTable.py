import os

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.dbfs.api import DbfsApi
from databricks_cli.dbfs.dbfs_path import DbfsPath

api_client = ApiClient(
  host  = os.getenv('DATABRICKS_HOST'),
  token = os.getenv('DATABRICKS_TOKEN')
)

dbfs_source_file_path      = 'dbfs:/tmp/covid_19_data_transformed.csv'
local_file_download_path   = '/workspaces/DE-Project-Repo-Durga/data/covid_19_data_transformed.csv'

dbfs_api  = DbfsApi(api_client)
dbfs_path = DbfsPath(dbfs_source_file_path)

dbfs_api.put_file(
  local_file_download_path,
  dbfs_path,
  overwrite = True
)

from databricks import sql

with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                    http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                    access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:
                            
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS covid_19_db1")
            cursor.execute("USE covid_19_db1")
            cursor.execute("CREATE TABLE IF NOT EXISTS covid_19_data1 (_c0 string,_c1 string,_c2 string,_c3 string,_c4 string)")
            
            
            cursor.execute("COPY INTO covid_19_data1 FROM 'dbfs:/tmp/covid_19_data_transformed.csv' FILEFORMAT = CSV")


            cursor.execute("SELECT * FROM covid_19_data1 LIMIT 10")
            for row in cursor:
                print(row)
            result = cursor.fetchall()
            print(result)

