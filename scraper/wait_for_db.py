import psycopg2
import os
import time

def wait_for_db():
    """Wait for the database to become available."""
    retries = 5
    while retries:
        try:
            with psycopg2.connect(host="db",
                                  dbname=os.environ.get("POSTGRES_DB", "example"),
                                  user=os.environ.get("POSTGRES_USER", "postgres"),
                                  password=os.environ.get("POSTGRES_PASSWORD", "mysecretpassword")):
                print("Database is ready!")
                break
        except psycopg2.OperationalError:
            print("Database is not ready. Waiting...")
            time.sleep(5)
            retries -= 1

if __name__ == "__main__":
    wait_for_db()
