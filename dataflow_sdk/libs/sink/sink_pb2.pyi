from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RAW: _ClassVar[SinkType]
    ITEM: _ClassVar[SinkType]
    COMMENT: _ClassVar[SinkType]
    PROFILE: _ClassVar[SinkType]
RAW: SinkType
ITEM: SinkType
COMMENT: SinkType
PROFILE: SinkType

class DoSinkRequest(_message.Message):
    __slots__ = ("sinkId", "data", "sinkType")
    SINKID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SINKTYPE_FIELD_NUMBER: _ClassVar[int]
    sinkId: str
    data: bytes
    sinkType: SinkType
    def __init__(self, sinkId: _Optional[str] = ..., data: _Optional[bytes] = ..., sinkType: _Optional[_Union[SinkType, str]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...
