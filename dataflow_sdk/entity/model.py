from datetime import datetime
from typing import Optional, Dict, Any, List, Union

from pydantic import BaseModel


class Metadata(BaseModel):
    source: Optional[str] = ''
    url: Optional[str] = ''
    crawl_time: Optional[str] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Record(BaseModel):
    item: Union[Dict[str, Any], List[Dict[str, Any]]]
    metadata: Optional[Metadata] = None
