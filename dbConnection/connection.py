import mysql.connector

class DbConnect:
    def __init__(self, mysql_config):
        self.mysql_config = mysql_config

    def establish_connection(self):
        try:
            # Establish connection
            self.conn = mysql.connector.connect(**self.mysql_config)
            self.cursor = self.conn.cursor()
            print('Connection successful!')
        except mysql.connector.Error as error:
            print('Error:', error)

    def execute_query(self, query):
        # Execute SQL queries using the 'cursor' object
        if hasattr(self, 'cursor') and self.cursor:
            try:
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                for row in rows:
                    print(row)
            except mysql.connector.Error as error:
                print('Error:', error)
        else:
            print('No active connection available.')

# Example usage
mysql_config = {
    'host': 'localhost',
    'user': 'sqluser',
    'password': 'password',
    'database': 'smartpermit'
}

test_instance = DbConnect(mysql_config)
test_instance.establish_connection()

# Example query execution
# query = "SELECT * FROM users"
# test_instance.execute_query(query)
