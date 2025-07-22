from datetime import datetime
from typing import Optional, Any, Dict

from pydantic import BaseModel, Field


class Record(BaseModel):
    store_key: Optional[str] = Field(default='')
    crawl_time: Optional[str] = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    data: Optional[Any]
    metadata: Optional[Dict[str, Any]] = Field(default=None)
