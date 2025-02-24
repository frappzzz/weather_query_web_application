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
### 5. Configure the Application
Create a .env file in the root directory with the following content:
```commandline
DB_NAME="weather_db"
DB_USER="your_user"
DB_PASSWORD="your_password"
DB_HOST=localhost
DB_PORT=5432
WEATHER_API_KEY="your_key"
APP_HOST_PORT=5000
```
### 6. Run the Application
Start the Flask application:
```commandline
python app.py
```
The application will be running at http://0.0.0.0:5000/.
### 7. Access the Application
Start the Flask application:
- **Home Page**: Open your web browser and navigate to http://localhost:5000/. Enter a city name to query the weather.
- **History Page**: Navigate to http://localhost:5000/history to view the query history.