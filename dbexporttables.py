import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=<YOUR_SERVER_ADDRESS>,<PORT>;'
                      'DATABASE=<YOUR_DATABASE_NAME>;'
                      'UID=<YOUR_UID>;PWD=<YOUR_PASSWORD>')
cursor = conn.cursor()
cursor.execute("SELECT * FROM <TABLE_NAME>")

columns = [column[0] for column in cursor.description]

for row in cursor.fetchall():
    values = ", ".join([f"'{str(row[i])}'" if row[i] is not None else "NULL" for i in range(len(columns))])

    print(f"INSERT INTO <TABLE_NAME> ({', '.join(columns)}) VALUES ({values});")


conn.close()