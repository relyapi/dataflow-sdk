from bycrawler import save_item
from bycrawler.biyao.entity.result import Result
from bycrawler.utils import calculate_md5


class DatdPipeline:
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
        result = Result(item)
        result.set_sink_name(spider.name)
        save_item(calculate_md5(spider.name), result)
        return item
