from credentials import *
import mysql.connector

def get_work():
    cnx = mysql.connector.connect(user=username, password=password, host=hostname, database='trvmssdb')
    cnx.start_transaction(isolation_level='SERIALIZABLE')
    cursor = cnx.cursor()
    
    num_rows = 30
    
    select_query = '''
    SELECT row_index, column_index, status, best_match_index FROM work WHERE status="todo" ORDER BY row_index, column_index ASC LIMIT 60;
    '''
    
    update_query = '''
    UPDATE work SET status="working" WHERE status="todo" ORDER BY row_index, column_index ASC LIMIT 60;
    '''
    
    cursor.execute(select_query)
    ret = []
    for row in cursor:
        ret.append(row)
        
    cursor.execute(update_query)
        
    cnx.commit()
    cursor.close()
    cnx.close()

    return ret
        
