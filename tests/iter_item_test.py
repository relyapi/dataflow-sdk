from datetime import datetime

from bycrawler import save_items

result = [{
    'name': 'gage',
    "age": 25,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "hello": "world",
    "world": 1121211
}] * 10
save_items('95b74bd2-c3a3-4ded-9248-4dc623a01e69', result)
