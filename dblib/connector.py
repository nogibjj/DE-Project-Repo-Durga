'''Databricks Connect CLI'''
import os
from databricks import sql
def querydb(query="SELECT * FROM default.diamonds LIMIT 2"):
    '''Connect to Databricks and run a query'''
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)
    return result
