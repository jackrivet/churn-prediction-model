import pyodbc
def get_connection():
    server = ''
    database = ''
    connection_string = (
        r"DRIVER=ODBC Driver 17 for SQL Server;"
        f"SERVER={server};"
        f"DATABASE={database};"
        r"Trusted_Connection=Yes;"
    )
    return pyodbc.connect(connection_string)
