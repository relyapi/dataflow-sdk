import os

from loguru import logger

from dataflow_sdk.entity.result import  save_item


class DataFlowPipeline:
    def process_item(self, item, spider):
        """
        task_id和task_name必须有一个
        scrapy项目取 spider_name
        普通项目取 task_id

        默认的pipeline（如果task_id不存在，则取task_name 优先取task_id）
        task_name 不校验task_id 是否合法
        :param item:
        :param spider:
        :return:
        """
        try:
            DATAFLOW_SINK_ID = os.environ["DATAFLOW_SINK_ID"]
            # result = Result(item)
            # result.set_sink_name(spider.name)
            # save_item(DATAFLOW_SINK_ID, result)
            return item
        except Exception as e:
            logger.error("未配置DATAFLOW_SINK_ID环境变量")
