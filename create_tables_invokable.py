
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2 import sql
from sqlalchemy import text, String, Integer, ForeignKey, ARRAY, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.dialects.postgresql import JSON, UUID, ARRAY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://login:pass@localhost/flask_app'
db = SQLAlchemy(app)

def initialize_tables(connection):
    cursor = connection.cursor()
    class Base(DeclarativeBase):
        id = mapped_column(
            UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
        )

    class HarvestSource(Base):
        __tablename__ = 'harvest_source'
        
        name = mapped_column(String)
        notification_emails = mapped_column(ARRAY(String))
        organization_name = mapped_column(String)
        frequency = mapped_column(String)
        config = mapped_column(JSON) 

    class HarvestJob(Base):
        __tablename__ = 'harvest_job'
        
        harvest_source_id = mapped_column(UUID(as_uuid=True), ForeignKey('harvest_source.id'), nullable=False)
        date_created = mapped_column(DateTime)
        date_finished = mapped_column(DateTime)
        records_added = mapped_column(Integer)
        records_updated = mapped_column(Integer)
        records_deleted = mapped_column(Integer)
        records_errored = mapped_column(Integer)
        records_ignored = mapped_column(Integer)
    

    class HarvestError(Base):
        __tablename__ = 'harvest_error'
        
        harvest_job_id = mapped_column(UUID(as_uuid=True), ForeignKey('harvest_job.id'), nullable=False)
        record_id = mapped_column(String, nullable=True)
        record_reported_id = mapped_column(String)
        date_created = mapped_column(DateTime)
        type = mapped_column(String)
        severity = mapped_column(String)
        message = mapped_column(String)



if __name__ == "__main__":
    # Modify the connection parameters according to your database configuration
    db_params = {
     connection_details
    }

    try:
        connection = psycopg2.connect(**db_params)
        initialize_tables(connection)
        print("Tables initialized successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

