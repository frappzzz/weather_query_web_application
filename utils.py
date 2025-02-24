from datetime import datetime

def timestamp_to_hms_format(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
def wind_direction(degrees):
    directions = [
        "North", "Northeast", "East", "Southeast",
        "South", "Southwest", "West", "Northwest"
    ]
    sector_size = 360 / len(directions)
    sector_index = int((degrees + sector_size / 2) % 360 // sector_size)
    return directions[sector_index]