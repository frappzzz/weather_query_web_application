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
git clone https://github.com/frappzzz/weather_query_web_application.git
cd weather_query_web_application
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
Create a PostgreSQL Database. Log in to PostgreSQL and create a new database:
```commandline
psql -U postgres
CREATE DATABASE weather_db;
\q
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
FLASK_APP=app.py
FLASK_ENV=development
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
## Setup with Docker

### 1. Installation Docker
Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
### 2. Clone the Repository
Clone the repository to your local machine:
```commandline
git clone https://github.com/frappzzz/weather_query_web_application.git
cd weather_query_web_application
```
### 3. Configure the Application
Create a .env file in the root directory with the following content:
```commandline
DB_NAME="weather_db"
DB_USER="your_user"
DB_PASSWORD="your_password"
DB_HOST=db
DB_PORT=5432
WEATHER_API_KEY="your_key"
APP_HOST_PORT=5000
FLASK_APP=app.py
FLASK_ENV=development
```
### 4. Start Services
Start services:
```commandline
docker-compose up --build
```
### 5. Access the Application
The application will be running at http://0.0.0.0:5000/.
- **Home Page**: Open your web browser and navigate to http://localhost:5000/. Enter a city name to query the weather.
- **History Page**: Navigate to http://localhost:5000/history to view the query history.