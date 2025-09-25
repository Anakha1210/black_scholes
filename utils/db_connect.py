import mysql.connector

def get_db_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="ARV12@",
        database='black_scholes_db'
    )
    return conn