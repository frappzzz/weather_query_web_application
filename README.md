# Weather Query Web Application
This is a simple Flask-based web application that allows users to query weather data for a specific city and view the query history. The application uses the OpenWeatherMap API to fetch weather data and stores the query results in a PostgreSQL database.

## Prerequisites

Before you begin, ensure you have the following installed:
```commandline
Python 3.x
PostgreSQL
pip (Python package manager)
```

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```commandline
git clone https://github.com/your-repository/weather-query-app.git
cd weather-query-app
```
### 2. Set Up a Virtual Environment
Create and activate a virtual environment:
```commandline
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```
### 3. Install Dependencies
Install the required Python packages:
```commandline
pip install -r requirements.txt
```
### 4. Set Up the Database
1. Create a PostgreSQL Database. Log in to PostgreSQL and create a new database:
```commandline
psql -U postgres
CREATE DATABASE weather_db;
\q
```
2. Create the weather_queries Table. Run the following SQL command to create the weather_queries table:
```commandline
CREATE TABLE IF NOT EXISTS weather_queries (id SERIAL PRIMARY KEY,
 city_name TEXT, 
 query_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
 weather_main TEXT, 
 weather_description TEXT, 
 temperature REAL, 
 temperature_feels_like REAL, 
 wind_speed REAL, 
 wind_deg TEXT, 
 sunrise TIME, 
 sunset TIME)
```
