# Docker-Sreality Project
A Dockerized web scraping project using Python, Scrapy, and Flask. It scrapes sreality.cz and displays first 500 items on a web interface. 

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites
Before you begin, ensure you have the following installed:

Git
Docker

# Installation
Follow these steps to get your development environment running:

## Clone the Repository

First, clone the project repository to your local machine:

git clone https://github.com/Honzakupka18/docker-sreality.git
cd docker-sreality

## Start Docker Daemon

Ensure that the Docker daemon is running on your machine. You can start Docker through your system's usual method.

##  Run Docker Compose

To start all services defined in the Docker Compose file, run the following command in the root directory of the project:

docker-compose up

This command builds and starts all the necessary containers for the web scraping application. It may take a few minutes to complete.

# Accessing the Application

Once all services are up and running, you can access the Flask web interface by navigating to http://127.0.0.1:8080 in your web browser.

Here, you should see the scraped 500 first items.

# Usage
The Flask application will display the data scraped by the Scrapy spider.
The PostgreSQL database stores the scraped data and is managed by Docker Compose.
To stop the application, press Ctrl+C in the terminal where Docker Compose is running.

# Stopping the Application
To stop the application and remove the containers, networks, volumes, and images created by docker-compose up, run:

docker-compose down -v


