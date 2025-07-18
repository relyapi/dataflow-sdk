from datetime import datetime

from dataflow_sdk import save_items, Record, Metadata

result = {
    'name': 'xiaoming',
    "age": 25,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "hello": "world",
    "world": 1121211
}

records = [Record(
    item=result,
    metadata=Metadata(url=f"https://www.json.cn{x}/"),
) for x in range(10)]

save_items('77963b7a931377ad4ab5ad6a9cd718aa', records)
