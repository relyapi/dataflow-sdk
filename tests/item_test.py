from bycrawler.biyao.crawler.site.message_pb2 import Spu
import json
spu = Spu(id="1", title='hello world')

print(json.dumps(spu, indent=2))
