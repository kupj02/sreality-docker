# Dockerfile for Scrapy project
FROM python:3.12.1-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Scrapy project into the container
COPY . .

# Run the wait script before starting the Scrapy spider
CMD python wait_for_db.py && scrapy crawl sreality_spider
