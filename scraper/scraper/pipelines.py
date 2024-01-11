import psycopg2
import os

class PostgresPipeline(object):
    def open_spider(self, spider):
        # Database connection details
        self.hostname = 'db'  
        self.username = 'postgres' 
        self.password = 'mysecretpassword'
        self.database = 'example' 
        self.connection = psycopg2.connect(host=self.hostname, user=self.username, password=self.password, dbname=self.database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        # SQL command for inserting data
        insert_query = "INSERT INTO scraped_data (title, image_url) VALUES (%s, %s)"
        self.cur.execute(insert_query, (item['title'], item['image_url']))
        self.connection.commit()
        return item
