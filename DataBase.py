import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
load_dotenv()
def get_DB_connection():
    conn = psycopg2.connect(dbname=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),
                            host=os.getenv('DB_HOST'),
                            port=os.getenv('DB_PORT'))
    return conn
def create_table():
    conn = get_DB_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_queries (
            id SERIAL PRIMARY KEY,
            city_name TEXT,
            query_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            weather_main TEXT,
            weather_description TEXT,
            temperature REAL,
            temperature_feels_like REAL,
            humidity INTEGER,
            pressure INTEGER,
            wind_speed REAL,
            wind_direction TEXT,
            sunrise TIME,
            sunset TIME,
            data_calculation TIME,
            weather_json JSONB
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_weather_query(city_name, weather_main, weather_description,temperature, temperature_feels_like,
                       humidity, pressure,wind_speed, wind_direction, sunrise,sunset,data_calculation,weather_json):
    conn = get_DB_connection()
    cur = conn.cursor()
    cur.execute(
        sql.SQL("INSERT INTO weather_queries "
                "(city_name, weather_main, weather_description,temperature, temperature_feels_like, "
                "humidity, pressure,wind_speed, wind_direction, sunrise,sunset,data_calculation,weather_json) "
                "VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s,%s,%s)"),
        (city_name, weather_main, weather_description,temperature, temperature_feels_like,
         humidity,pressure,wind_speed, wind_direction, sunrise,sunset,data_calculation,weather_json)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_weather_history():
    conn = get_DB_connection()
    cur = conn.cursor()
    cur.execute("SELECT "
                "query_timestamp, city_name, weather_main, weather_description,temperature, temperature_feels_like, "
                "humidity,pressure, wind_speed, wind_direction, sunrise,sunset,data_calculation "
                "FROM weather_queries "
                "ORDER BY query_timestamp DESC")
    history = cur.fetchall()
    cur.close()
    conn.close()
    return history
