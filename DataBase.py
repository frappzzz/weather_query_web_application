import psycopg2
from psycopg2 import sql
from datetime import datetime
import config

def get_DB_connection():
    conn = psycopg2.connect(dbname=config.DB_NAME, user=config.DB_USER, password=config.DB_PASSWORD, host=config.DB_HOST, port=config.DB_PORT)
    return conn
def save_weather_query(city_name, weather_main, weather_description,temperature, temperature_feels_like,wind_speed, wind_deg, sunrise,sunset):
    conn = get_DB_connection()
    cur = conn.cursor()
    cur.execute(
        sql.SQL("INSERT INTO weather_queries (city_name, weather_main, weather_description,temperature, temperature_feels_like, wind_speed, wind_deg, sunrise,sunset) "
                "VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)"),
        (city_name, weather_main, weather_description,temperature, temperature_feels_like, wind_speed, wind_deg, sunrise,sunset)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_weather_history():
    conn = get_DB_connection()
    cur = conn.cursor()
    cur.execute("SELECT query_timestamp, city_name, weather_main, weather_description,temperature, temperature_feels_like, wind_speed, wind_deg, sunrise,sunset FROM weather_queries ORDER BY query_timestamp DESC")
    history = cur.fetchall()
    cur.close()
    conn.close()
    return history
