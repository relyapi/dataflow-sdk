import json
from typing import List, Optional, Dict

from loguru import logger

from bycrawler.biyao.crawler.flow.data_pb2 import SinkType
from bycrawler.biyao.crawler.flow.message_pb2 import DoSinkRequest, DoVerifyRequest
from bycrawler.biyao.crawler.flow.service_pb2_grpc import DataHubStub
from bycrawler.biyao.entity.client import Client, get_client


class Result(dict):
    """
    _task_id: 任务id
    _task_name: 任务名称
    _task_type: 任务类型 list/detail
    """

    def get_sink_id(self) -> str:
        return self.get('_sink_id')

    def set_sink_id(self, sink_id: str):
        self['_sink_id'] = sink_id

    def get_sink_name(self) -> str:
        return self.get('_sink_name')

    def set_sink_name(self, sink_name: str):
        self['_sink_name'] = sink_name

    def get_sink_type(self) -> str:
        return self.get('_sink_type')

    def set_sink_type(self, sink_type: SinkType):
        self['_sink_type'] = sink_type

    def to_dict(self) -> dict:
        return dict(self)


class ResultService:
    # internal
    c: Client = None
    sink_stub: DataHubStub = None

    def __init__(self, sink_id: str, sink_type: SinkType):
        self.c = get_client()
        self.sink_stub = self.c.data_hub_stub
        self.sink_id = sink_id
        self.sink_type = sink_type
        self.is_verify = False

    def save_protobuf_item(self):
        # todo: 写入protobuf数据
        pass

    def save_item(self, *items: Dict):
        self.save(list(items), batch=1)

    def save_items(self, items: List[Dict]):
        self.save(items, batch=100)

    def save(self, items: List[Dict], batch):
        _items: List[Dict] = []
        for i, item in enumerate(items):
            _items.append(item)
            if i > 0 and i % batch == 0:
                self._save(_items)
                _items = []
        if len(_items) > 0:
            self._save(_items)

    def verify_sink_id(self, sink_id) -> bool:
        if self.is_verify:
            return True
        try:
            result = self.sink_stub.DoVerify(DoVerifyRequest(
                sinkId=str(sink_id)
            ))
            logger.info(f'sink_id verify success: {result}')
            self.is_verify = True
            return True
        except Exception as e:
            logger.error(e)
            return False

    def _save(self, items: List[Dict]):
        if not self.sink_id:
            logger.info("task_id is null, please set task_id.")
            return
        # 校验sink_id合法
        if not self.verify_sink_id(self.sink_id):
            logger.info("invalid's task_id, please set correct task_id.")
            return

        records = []
        for item in items:
            result = Result(item)
            result.set_sink_id(self.sink_id)
            result.set_sink_type(self.sink_type)
            logger.info(item)
            records.append(result)

        data = json.dumps({
            "data": records
        }).encode('utf-8')
        msg = DoSinkRequest(
            sinkId=self.sink_id,
            sinkType=self.sink_type,
            data=data,
        )
        self.sink_stub.DoSink(iter([msg]))


RS: Optional[ResultService] = None


def get_result_service(task_id: str, task_type: SinkType) -> ResultService:
    global RS
    if RS is not None:
        return RS
    RS = ResultService(task_id, task_type)
    return RS


def save_item(sink_id: str, *items: Dict):
    get_result_service(sink_id, SinkType.INSERT).save_item(*items)


def save_items(sink_id: str, items: List[Dict]):
    get_result_service(sink_id, SinkType.INSERT).save_items(items)


def save_log(sink_id: str, *items: Dict):
    get_result_service(sink_id, SinkType.LOG).save_item(*items)


def save_logs(sink_id: str, items: List[Dict]):
    get_result_service(sink_id, SinkType.LOG).save_items(items)
