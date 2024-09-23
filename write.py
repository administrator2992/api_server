from db import get_db

# Add data to cfg_table
def insert_cfg(cfg):
    db = get_db()
    cursor = db.cursor()
    
    # The correct SQL query
    query = "INSERT INTO cfg_table(cpu_cores, cpu_freq, gpu_freq, mem_freq, cl) VALUES (?, ?, ?, ?, ?)"
    
    # Unpack the values of cfg into a list or tuple to match the query placeholders
    cursor.execute(query, [cfg['cpu_cores'], cfg['cpu_freq'], cfg['gpu_freq'], cfg['mem_freq'], cfg['cl']])
    
    db.commit()
    return True

def insert_output(output):
    db = get_db()
    cursor = db.cursor()
    
    # The correct SQL query
    query = "INSERT INTO output_table(throughput, power_cons) VALUES (?, ?)"
    
    # Unpack the values of output into a list or tuple to match the query placeholders
    cursor.execute(query, [output['throughput'], output['power']])
    
    db.commit()
    return True