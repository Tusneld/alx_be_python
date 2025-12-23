import mysql.connector
seed = __import__('seed')

def stream_user_ages():
    """Generator that yields user ages one by one."""
    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        
        for (age,) in cursor:
            yield age
            
        cursor.close()
        connection.close()

def calculate_average_age():
    """Calculates average age using a generator."""
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count == 0:
        print("Average age of users: 0")
    else:
        average = total_age / count
        print(f"Average age of users: {average}")

if __name__ == "__main__":
    calculate_average_age()