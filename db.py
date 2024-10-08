import sqlite3

DATABASE_NAME = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table_readkey():
    tables = [
            """CREATE TABLE IF NOT EXISTS
                readkey_table(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT NOT NULL)"""
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)

def create_table_account():
    tables = [
            """CREATE TABLE IF NOT EXISTS
                account(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)"""
        ]

    db = get_db()
    cursor = db.cursor()

    for table in tables:
        cursor.execute(table)

def create_table_writekey():
    tables = [
           """CREATE TABLE IF NOT EXISTS
                writekey_table(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT NOT NULL)"""
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)
    
def create_table_cfg():
    tables = [
           """CREATE TABLE IF NOT EXISTS
                cfg_table(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpu_cores INTEGER NOT NULL,
                    cpu_freq INTEGER NOT NULL,
                    gpu_freq INTEGER NOT NULL,
                    mem_freq INTEGER NOT NULL,
                    cl INTEGER NOT NULL
                    )"""
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)

def create_table_output():
    tables = [
           """CREATE TABLE IF NOT EXISTS
                output_table(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    throughput INTEGER NOT NULL,
                    power_cons INTEGER NOT NULL
                    )"""
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)

def delete_all_api():
    db = get_db()
    cursor = db.cursor()
    # DELETE
    queryread = "DELETE FROM readkey_table"
    cursor.execute(queryread)
    querywrite = "DELETE FROM writekey_table"
    cursor.execute(querywrite)
    db.commit()

def delete_all_cfg():
    db = get_db()
    cursor = db.cursor()
    # DELETE
    query = "DELETE FROM cfg_table"
    cursor.execute(query)
    db.commit()

def delete_all_output():
    db = get_db()
    cursor = db.cursor()
    # DELETE
    query = "DELETE FROM output_table"
    cursor.execute(query)
    db.commit()
