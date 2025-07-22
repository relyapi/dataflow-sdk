from datetime import datetime
from typing import Optional, Any, Dict

from pydantic import BaseModel, Field, ConfigDict

from dataflow_sdk.libs.sink.sink_pb2 import SinkType


class Record(BaseModel):
    parent_url: str = Field(description='parent url')
    sink_type: SinkType = Field(description='sink type')
    store_key: Optional[str] = Field(default='')
    crawl_time: Optional[str] = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    data: Optional[Any]
    metadata: Optional[Dict[str, Any]] = Field(default=None)

    model_config = ConfigDict(arbitrary_types_allowed=True)
