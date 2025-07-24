from datetime import datetime

from dataflow_sdk import save_items, Record
from dataflow_sdk.entity.model import SinkType

result = {
    'name': 'xiaoming',
    "age": 25,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "hello": "world",
    "world": 1121211
}

records = [Record(
    request_url=f"https://add.weee.tsinghua.edu.cn/{x}",
    sink_type=SinkType.ITEM,
    data=result,
    metadata={"name": "gage"},
) for x in range(10)]

save_items('77963b7a931377ad4ab5ad6a9cd718aa', records)
