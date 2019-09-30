# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class DeviceInfoMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    uniqueIdentifier = ... # type: typing___Text
    name = ... # type: typing___Text
    localizedModelName = ... # type: typing___Text
    systemBuildVersion = ... # type: typing___Text
    applicationBundleIdentifier = ... # type: typing___Text
    applicationBundleVersion = ... # type: typing___Text
    protocolVersion = ... # type: int
    lastSupportedMessageType = ... # type: int
    supportsSystemPairing = ... # type: bool
    allowsPairing = ... # type: bool
    connected = ... # type: bool
    systemMediaApplication = ... # type: typing___Text
    supportsACL = ... # type: bool
    supportsSharedQueue = ... # type: bool
    supportsExtendedMotion = ... # type: bool
    bluetoothAddress = ... # type: bytes
    sharedQueueVersion = ... # type: int
    localReceiverPairingIdentity = ... # type: typing___Text

    def __init__(self,
        *,
        uniqueIdentifier : typing___Text,
        name : typing___Text,
        systemBuildVersion : typing___Text,
        applicationBundleIdentifier : typing___Text,
        protocolVersion : int,
        localizedModelName : typing___Optional[typing___Text] = None,
        applicationBundleVersion : typing___Optional[typing___Text] = None,
        lastSupportedMessageType : typing___Optional[int] = None,
        supportsSystemPairing : typing___Optional[bool] = None,
        allowsPairing : typing___Optional[bool] = None,
        connected : typing___Optional[bool] = None,
        systemMediaApplication : typing___Optional[typing___Text] = None,
        supportsACL : typing___Optional[bool] = None,
        supportsSharedQueue : typing___Optional[bool] = None,
        supportsExtendedMotion : typing___Optional[bool] = None,
        bluetoothAddress : typing___Optional[bytes] = None,
        sharedQueueVersion : typing___Optional[int] = None,
        localReceiverPairingIdentity : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceInfoMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"allowsPairing",u"applicationBundleIdentifier",u"applicationBundleVersion",u"bluetoothAddress",u"connected",u"lastSupportedMessageType",u"localReceiverPairingIdentity",u"localizedModelName",u"name",u"protocolVersion",u"sharedQueueVersion",u"supportsACL",u"supportsExtendedMotion",u"supportsSharedQueue",u"supportsSystemPairing",u"systemBuildVersion",u"systemMediaApplication",u"uniqueIdentifier"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"allowsPairing",u"applicationBundleIdentifier",u"applicationBundleVersion",u"bluetoothAddress",u"connected",u"lastSupportedMessageType",u"localReceiverPairingIdentity",u"localizedModelName",u"name",u"protocolVersion",u"sharedQueueVersion",u"supportsACL",u"supportsExtendedMotion",u"supportsSharedQueue",u"supportsSystemPairing",u"systemBuildVersion",u"systemMediaApplication",u"uniqueIdentifier"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"allowsPairing",b"allowsPairing",u"applicationBundleIdentifier",b"applicationBundleIdentifier",u"applicationBundleVersion",b"applicationBundleVersion",u"bluetoothAddress",b"bluetoothAddress",u"connected",b"connected",u"lastSupportedMessageType",b"lastSupportedMessageType",u"localReceiverPairingIdentity",b"localReceiverPairingIdentity",u"localizedModelName",b"localizedModelName",u"name",b"name",u"protocolVersion",b"protocolVersion",u"sharedQueueVersion",b"sharedQueueVersion",u"supportsACL",b"supportsACL",u"supportsExtendedMotion",b"supportsExtendedMotion",u"supportsSharedQueue",b"supportsSharedQueue",u"supportsSystemPairing",b"supportsSystemPairing",u"systemBuildVersion",b"systemBuildVersion",u"systemMediaApplication",b"systemMediaApplication",u"uniqueIdentifier",b"uniqueIdentifier"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"allowsPairing",b"allowsPairing",u"applicationBundleIdentifier",b"applicationBundleIdentifier",u"applicationBundleVersion",b"applicationBundleVersion",u"bluetoothAddress",b"bluetoothAddress",u"connected",b"connected",u"lastSupportedMessageType",b"lastSupportedMessageType",u"localReceiverPairingIdentity",b"localReceiverPairingIdentity",u"localizedModelName",b"localizedModelName",u"name",b"name",u"protocolVersion",b"protocolVersion",u"sharedQueueVersion",b"sharedQueueVersion",u"supportsACL",b"supportsACL",u"supportsExtendedMotion",b"supportsExtendedMotion",u"supportsSharedQueue",b"supportsSharedQueue",u"supportsSystemPairing",b"supportsSystemPairing",u"systemBuildVersion",b"systemBuildVersion",u"systemMediaApplication",b"systemMediaApplication",u"uniqueIdentifier",b"uniqueIdentifier"]) -> None: ...

deviceInfoMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
