import json
import os
import psycopg2
import time
from flask import Flask


# Flask app initialization
app = Flask(__name__)

# Database credentials
password = os.environ.get('POSTGRES_PASSWORD', 'default_password')
hostname = 'db' 
username = 'postgres'
database = 'example'

# Function to get the scraped data
@app.route('/')
def get_scraped_data():
    """Endpoint to fetch scraped data.""" 
    with psycopg2.connect(host=hostname, user=username, password=password, database=database) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT title, image_url FROM scraped_data")
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()
    json_data = [dict(zip(row_headers, result)) for result in results]
    return json.dumps(json_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
