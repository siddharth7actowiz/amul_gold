from config import *
import mysql.connector

def make_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn
def create_Table(cursor,TAB):
    ddl=f'''CREATE TABLE IF NOT EXISTS {TAB} (
            id  INT AUTO_INCREMENT PRIMARY KEY,
            Product_Name VARCHAR(250),
            Brand_Name  VARCHAR(50),
            Product_Id  VARCHAR(100) UNIQUE,
            Description TEXT,
            Images TEXT,
            Category VARCHAR(500),
            Rating DECIMAL(2,1),
            Review_Count INT,
            Rating_Count INT , 
            Price DECIMAL(10,2),
            Currency VARCHAR(50),
            Avl_Url VARCHAR(500),
            Item_Condition VARCHAR(500),
            Return_Policy TEXT
         
        );'''
    cursor.execute(ddl)

def insert_into_db(data, cursor, con):
    if not data:                          
        print("No data to insert.")
        return
    # handle both single dict and list of dicts
    if isinstance(data, dict):
        data = [data]
    try:
        cols   = ",".join(data[0].keys())
        vals   = ",".join(["%s"] * len(data[0].keys()))
        insert_query = f"INSERT INTO {TABLE_NAME} ({cols}) VALUES ({vals}) ON DUPLICATE KEY UPDATE ID=ID;"
        rows   = [tuple(d.values()) for d in data]
        cursor.executemany(insert_query, rows)
        con.commit()
        print(f"{cursor.rowcount} rows inserted.")
    except Exception as e:
        con.rollback()
        print("Error", insert_into_db.__name__, e)