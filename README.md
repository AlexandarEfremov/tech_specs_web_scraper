# Tech Specs Web Scraper

## Overview

Tech Specs Scraper is a web scraper built using Scrapy and a REST API developed with Flask. This project scrapes computer specifications from the `https://desktop.bg/computers-all` website and provides an API to access the data.

## Features

- Scrapes computer specifications such as processor, GPU, motherboard, and RAM.
- Stores scraped data in an SQLite database.
- Provides a REST API to query the data with optional filters.

## Project Structure

![image](https://github.com/AlexandarEfremov/tech_specs_web_scraper/assets/145782693/71058909-f58c-4233-a958-05e95e71ef38)

## Installation

1. Clone the repository:

   git clone https://github.com/AlexandarEfremov/tech_specs_web_scraper.git
   cd desktop_bg

2. Create a virtual environment and activate it:
   
   python -m venv venv
   source venv/bin/activate

4. Install the required dependencies:
   
   pip install scrapy
   pip install jsonschema
   pip install flask

## Running the scraper

1. Navigate to the desktop_bg directory:

   cd desktop_bg
   cd spiders

2. Run the scraper:
   
   scrapy crawl desktop_spider

## Running the Flask API

1. Navigate to the api directory:
   
   cd api

2. Start the Flask server:

   python main.py

3. The API will be available at http://127.0.0.1:5000.


## API Endpoints

Get All Computers

  URL: /computers
  Method: GET

Query Parameters:

  processor (optional),
  gpu (optional),
  motherboard (optional),
  ram (optional)

Response:

  ![image](https://github.com/AlexandarEfremov/tech_specs_web_scraper/assets/145782693/12fd8ea8-af8a-48ef-891a-ca7e84b7c8a9)

## Example requests

  Get all computers: http://127.0.0.1:5000/computers /n
  Filter by processor: http://127.0.0.1:5000/computers?processor=Intel /n
  Filter by GPU: http://127.0.0.1:5000/computers?gpu=NVIDIA /n



Crawling permissions as per https://desktop.bg/robots.txt

![image](https://github.com/AlexandarEfremov/tech_specs_web_scraper/assets/145782693/b46d345e-3b53-4f12-aa6f-8f012910a015)

## License

This project is licensed under the MIT License.

## Acknowledgments

  https://scrapy.org/
  Flask
  SQLite3

