import psycopg2
from psycopg2 import sql

def initialize_tables(connection):
    cursor = connection.cursor()

    # Add your table creation SQL statements here
    table_creation_queries = [
        """
        CREATE TABLE IF NOT EXISTS harvest_source (
        name String,
        notification_emails String,
        organization_name String,
        frequency String,
        config json
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS harvest_job(
        harvest_source_id UUID,
        date_created DateTime,
        date_finished DateTime,
        records_added Integer,
        records_updated Integer,
        records_deleted Integer,
        records_errored Integer,
        records_ignored Integer);
        """,
         """
        CREATE TABLE IF NOT EXISTS harvest_error(
        harvest_job_id UUID,
        record_id String,
        record_reported_id String,
        date_created DateTime,
        type String,
        severity String,
        message String);
        """
        # Add more table creation statements as needed
    ]

    for query in table_creation_queries:
        cursor.execute(sql.SQL(query))

    connection.commit()
    cursor.close()

if __name__ == "__main__":
    # Modify the connection parameters according to your database configuration

    connection_details="postgresql+psycopg2://login:pass@localhost/test"
    try:
        connection = psycopg2.connect(connection_details)
        initialize_tables(connection)
        print("Tables initialized successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()