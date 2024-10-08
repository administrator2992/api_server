from db import get_db

# obtain all data cfg
def get_cfg():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT * FROM cfg_table"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #obtain column name
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #convert to dictionary
        
    return result

def get_output():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT * FROM output_table"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #obtain column name
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #convert to dictionary
        
    return result