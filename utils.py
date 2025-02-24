from datetime import datetime
from zoneinfo import ZoneInfo
def timestamp_to_hms_format(timestamp, timezone_offset):
    tz = ZoneInfo(f"Etc/GMT{'+' if timezone_offset <= 0 else '-'}{abs(timezone_offset) // 3600}")
    dt = datetime.fromtimestamp(timestamp, tz)
    return dt.strftime('%H:%M:%S')
def wind_direction(degrees):
    directions = [
        "North", "Northeast", "East", "Southeast",
        "South", "Southwest", "West", "Northwest"
    ]
    sector_size = 360 / len(directions)
    sector_index = int((degrees + sector_size / 2) % 360 // sector_size)
    return directions[sector_index]