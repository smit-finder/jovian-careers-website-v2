import pymysql
from sqlalchemy import create_engine, text
import os

def get_database_engine():
    # Retrieve database connection parameters from environment variables
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    if None in (db_host, db_port, db_user, db_password, db_name):
        raise ValueError("Database environment variables are not set")

    # Database connection parameters
    charset = "utf8mb4"
    timeout = 10

    # Create SQLAlchemy engine
    engine_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(engine_url,
                           connect_args={'connect_timeout': timeout, 'charset': charset},
                           pool_recycle=3600)  # Adjust pool_recycle based on your needs

    return engine
def load_jobs_from_db():

    engine = get_database_engine()

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
        return jobs



