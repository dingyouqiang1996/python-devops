from datetime import datetime, timedelta
import pytz

# 获取当前时间(格式: 2024-01-05T11:30:04+08:00)
def get_current_time_YYYYmmddTHHMMSZ() -> str:
    desired_timezone = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(pytz.utc).astimezone(desired_timezone)
    return current_time.strftime("%Y-%m-%dT%H:%M:%S%z").replace("+0800", "+08:00")

# 获取n天前的时间(格式：2024-01-04T11:57:15+08:00)
def get_ndays_ago_time_YYYYmmddTHHMMSZ(days_ago=1) -> str:
    desired_timezone = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(pytz.utc).astimezone(desired_timezone)
    days_ago = current_time - timedelta(days=days_ago)
    formatted_days_ago = days_ago.strftime("%Y-%m-%dT%H:%M:%S%z").replace("+0800", "+08:00")
    return formatted_days_ago

# 获取n小时前的时间(格式：2024-01-05T10:18:39+08:00)
def get_nhours_ago_time_YYYYmmddTHHMMSZ(hours_ago=1) -> str:
    desired_timezone = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(pytz.utc).astimezone(desired_timezone)
    hours_ago = current_time - timedelta(hours=hours_ago)
    formatted_hours_ago = hours_ago.strftime("%Y-%m-%dT%H:%M:%S%z").replace("+0800", "+08:00")
    return formatted_hours_ago

