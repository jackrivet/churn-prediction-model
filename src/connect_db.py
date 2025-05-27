import pyodbc
def get_connection():
    server = 'tcp:HRICSQLTSTP01.hps.com'
    database = 'Analytics_Data'
    connection_string = (
        r"DRIVER=ODBC Driver 17 for SQL Server;"
        f"SERVER={server};"
        f"DATABASE={database};"
        r"Trusted_Connection=Yes;"
    )
    return pyodbc.connect(connection_string)
