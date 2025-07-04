import os

import grpc

from bycrawler.biyao.crawler.gateway.service_pb2_grpc import SignGatewayStub, ProxyGatewayStub, SmsGatewayStub, \
    HeaderGatewayStub

BIYAO_GATEWAY_HEADER_ADDR = os.environ.get("BIYAO_GATEWAY_HEADER_ADDR", '10.6.16.232:32251')
BIYAO_GATEWAY_SIGN_ADDR = os.environ.get("BIYAO_GATEWAY_SIGN_ADDR", '10.6.16.232:32252')
BIYAO_GATEWAY_PROXY_ADDR = os.environ.get("BIYAO_GATEWAY_PROXY_ADDR", '10.6.16.232:32253')
BIYAO_GATEWAY_SMS_ADDR = os.environ.get("BIYAO_GATEWAY_SMS_ADDR", '10.6.16.191:32255')


class GatewayClient(object):
    sign_client: SignGatewayStub = None
    proxy_client: ProxyGatewayStub = None
    header_client: HeaderGatewayStub = None

    def __init__(self):
        # sign client
        self.sign_channel = grpc.insecure_channel(BIYAO_GATEWAY_SIGN_ADDR)
        self.sign_client = SignGatewayStub(self.sign_channel)

        # proxy client
        self.proxy_channel = grpc.insecure_channel(BIYAO_GATEWAY_PROXY_ADDR)
        self.proxy_client = ProxyGatewayStub(self.proxy_channel)

        # header client
        self.header_channel = grpc.insecure_channel(BIYAO_GATEWAY_HEADER_ADDR)
        self.header_client = HeaderGatewayStub(self.header_channel)

        # sms client
        self.sms_channel = grpc.insecure_channel(BIYAO_GATEWAY_SMS_ADDR)
        self.sms_client = SmsGatewayStub(self.sms_channel)


def get_gateway_client() -> GatewayClient:
    return GatewayClient()
