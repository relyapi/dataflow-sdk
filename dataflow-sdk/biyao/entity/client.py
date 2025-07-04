import os
from typing import Optional

import grpc

from bycrawler.biyao.crawler.flow.service_pb2_grpc import DataHubStub
from bycrawler.biyao.entity.address import Address, new_address_from_string


class Client:
    # settings
    address: Address = None
    timeout: int = 10

    # internals
    channel: grpc.Channel = None

    # dependencies
    data_hub_stub: DataHubStub = None

    # plugin_client: Plugin = None

    def __init__(self):
        try:
            self.address = new_address_from_string(os.getenv('BIYAO_FLOW_GRPC_ADDRESS', "10.6.16.232:31792"))
        except Exception:
            self.address = Address(
                host=os.getenv('BIYAO_FLOW_GRPC_ADDRESS_HOST'),
                port=os.getenv('BIYAO_FLOW_GRPC_ADDRESS_PORT'),
            )
        addr = self.address.string()
        self.channel = grpc.insecure_channel(addr)
        self._register()

    def _register(self):
        self.data_hub_stub = DataHubStub(self.channel)


C: Optional[Client] = None


def get_client() -> Client:
    global C
    if C is not None:
        return C
    C = Client()
    return C
