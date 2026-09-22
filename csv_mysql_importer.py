import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "ecommerce")

# Create the database if it doesn't exist
def run_importer():
    init_conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    init_cursor = init_conn.cursor()
    init_cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
    init_cursor.close()
    init_conn.close()

    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()

    # List of CSV files and their corresponding table names
    csv_files = [
        ('customers.csv', 'customers'),
        ('orders.csv', 'orders'),
        ('sellers.csv', 'sellers'),
        ('products.csv', 'products'),
        ('geolocation.csv', 'geolocation'),
        ('payments.csv', 'payments'),
        ('order_items.csv', 'order_items')
    ]


    # Folder containing the CSV files
    folder_path = 'D:\\My Files\\Project_01\\E-commerce sales'

    def get_sql_type(dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return 'BIGINT'
        elif pd.api.types.is_float_dtype(dtype):
            return 'FLOAT'
        elif pd.api.types.is_bool_dtype(dtype):
            return 'BOOLEAN'
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return 'DATETIME'
        else:
            return 'TEXT'

    for csv_file, table_name in csv_files:
        file_path = os.path.join(folder_path, csv_file)

        if not os.path.exists(file_path):
            print(f"Skipping {csv_file} (File not found at {file_path})")
            continue

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path, encoding='utf-8')

        # Replace NaN with None to handle SQL NULL
        df = df.where(pd.notnull(df), None)

        # Debugging: Check for NaN values
        print(f"Processing {csv_file}")
        print(f"NaN values before replacement:\n{df.isnull().sum()}\n")

        # Clean column names
        df.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df.columns]

        # Drop the table if it exists to avoid conflicts
        cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`")

        # Generate the CREATE TABLE statement with appropriate data types
        columns = ', '.join([f'`{col}` {get_sql_type(df[col].dtype)}' for col in df.columns])
        create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})'
        cursor.execute(create_table_query)

        # Insert DataFrame data into the MySQL table
        cols_str = ', '.join([f'`{col}`' for col in df.columns])
        placeholders = ', '.join(['%s'] * len(df.columns))
        sql = f"INSERT INTO `{table_name}` ({cols_str}) VALUES ({placeholders})"

        # Convert row to tuple and handle NaN/None explicitly
        records = [tuple(None if pd.isna(x) else x for x in row) for row in df.to_numpy()]
        chunk_size = 25000
        for i in range(0, len(records), chunk_size):
            cursor.executemany(sql, records[i:i + chunk_size])

        # Commit the transaction for the current CSV file
        conn.commit()

    # Close the connection
    conn.close()

if __name__ == "__main__":
    run_importer()
    print("Data import completed successfully.")