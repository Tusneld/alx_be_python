import mysql.connector
seed = __import__('seed')

def stream_users_in_batches(batch_size):
    """Generator that yields rows in batches."""
    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
            
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)