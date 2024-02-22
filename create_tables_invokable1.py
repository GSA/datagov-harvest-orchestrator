import psycopg2
from psycopg2 import sql

def initialize_tables(connection):
  
    cursor = connection.cursor()

    # Add your table creation SQL statements here
    table_creation_queries = [
        """
        CREATE TABLE IF NOT EXISTS harvest_source (
        name varchar(100),
        notification_emails varchar(100),
        organization_name varchar(100),
        frequency varchar(100),
        config json
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS harvest_job(
        harvest_source_id UUID,
        date_created timestamp,
        date_finished timestamp,
        records_added Integer,
        records_updated Integer,
        records_deleted Integer,
        records_errored Integer,
        records_ignored Integer);
        """,
         """
        CREATE TABLE IF NOT EXISTS harvest_error(
        harvest_job_id UUID,
        record_id varchar(100),
        record_reported_id varchar(100),
        date_created timestamp,
        type varchar(100),
        severity varchar(100),
        message varchar(100));
        """
        # Add more table creation statements as needed
    ]

    for query in table_creation_queries:
        cursor.execute(sql.SQL(query))

    connection.commit()
    cursor.close()

if __name__ == "__main__":
    # Modify the connection parameters according to your database configuration
    try:
        connection = psycopg2.connect(
        port="5432",
        dbname="postgres",
        user="postgres",
        host="localhost",
        password="Shanu123")
        initialize_tables(connection)
        print("Tables initialized successfully.")
    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()