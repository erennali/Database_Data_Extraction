# 📄 **Database Table Exporter Script**  
## 📚 **Description (Açıklama)**  
**English:** This Python script connects to a SQL Server database, retrieves data from a specified table, and processes it for export. It's useful for database backups, data migrations, or analytics.  
**Türkçe:** Bu Python betiği, bir SQL Server veritabanına bağlanır, belirtilen tablodan verileri alır ve dışa aktarmak için işler. Veritabanı yedeklemeleri, veri taşıma veya analiz işlemleri için kullanışlıdır.  

## ⚙️ **Requirements (Gereksinimler)**  
- Python 3.x  
- pyodbc library  
Install dependencies: `pip install pyodbc`  

## 🚀 **Usage (Kullanım)**  
1. Clone this repository: `git clone <REPO_URL> && cd <REPO_FOLDER>`  
2. Update connection settings:  
```python  
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'  
                      'SERVER=<YOUR_SERVER_ADDRESS>,<PORT>;'  
                      'DATABASE=<YOUR_DATABASE_NAME>;'  
                      'UID=<YOUR_UID>;PWD=<YOUR_PASSWORD>')  
