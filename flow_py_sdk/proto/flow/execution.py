# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: flow/execution/execution.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from ..flow import entities


@dataclass
class PingRequest(betterproto.Message):
    pass


@dataclass
class PingResponse(betterproto.Message):
    pass


@dataclass
class GetAccountAtBlockIDRequest(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)
    address: bytes = betterproto.bytes_field(2)


@dataclass
class GetAccountAtBlockIDResponse(betterproto.Message):
    account: entities.Account = betterproto.message_field(1)


@dataclass
class ExecuteScriptAtBlockIDRequest(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)
    script: bytes = betterproto.bytes_field(2)
    arguments: List[bytes] = betterproto.bytes_field(3)


@dataclass
class ExecuteScriptAtBlockIDResponse(betterproto.Message):
    value: bytes = betterproto.bytes_field(1)


@dataclass
class GetEventsForBlockIDsResponse(betterproto.Message):
    results: List["GetEventsForBlockIDsResponseResult"] = betterproto.message_field(1)


@dataclass
class GetEventsForBlockIDsResponseResult(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)
    block_height: int = betterproto.uint64_field(2)
    events: List[entities.Event] = betterproto.message_field(3)


@dataclass
class GetEventsForBlockIDsRequest(betterproto.Message):
    type: str = betterproto.string_field(1)
    block_ids: List[bytes] = betterproto.bytes_field(2)


@dataclass
class GetTransactionResultRequest(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)
    transaction_id: bytes = betterproto.bytes_field(2)


@dataclass
class GetTransactionResultResponse(betterproto.Message):
    status_code: int = betterproto.uint32_field(1)
    error_message: str = betterproto.string_field(2)
    events: List[entities.Event] = betterproto.message_field(3)


class ExecutionAPIStub(betterproto.ServiceStub):
    """ExecutionAPI is the API provided by the execution nodes."""

    async def ping(self) -> PingResponse:
        """Ping is used to check if the access node is alive and healthy."""

        request = PingRequest()

        return await self._unary_unary(
            "/flow.execution.ExecutionAPI/Ping",
            request,
            PingResponse,
        )

    async def get_account_at_block_i_d(
        self, *, block_id: bytes = b"", address: bytes = b""
    ) -> GetAccountAtBlockIDResponse:
        """
        GetAccountAtBlockID gets an account by address at the given block ID
        """

        request = GetAccountAtBlockIDRequest()
        request.block_id = block_id
        request.address = address

        return await self._unary_unary(
            "/flow.execution.ExecutionAPI/GetAccountAtBlockID",
            request,
            GetAccountAtBlockIDResponse,
        )

    async def execute_script_at_block_i_d(
        self, *, block_id: bytes = b"", script: bytes = b"", arguments: List[bytes] = []
    ) -> ExecuteScriptAtBlockIDResponse:
        """
        ExecuteScriptAtBlockID executes a ready-only Cadence script against the
        execution state at the block with the given ID.
        """

        request = ExecuteScriptAtBlockIDRequest()
        request.block_id = block_id
        request.script = script
        request.arguments = arguments

        return await self._unary_unary(
            "/flow.execution.ExecutionAPI/ExecuteScriptAtBlockID",
            request,
            ExecuteScriptAtBlockIDResponse,
        )

    async def get_events_for_block_i_ds(
        self, *, type: str = "", block_ids: List[bytes] = []
    ) -> GetEventsForBlockIDsResponse:
        """
        GetEventsForBlockIDs retrieves events for all the specified block IDs
        that have the given type
        """

        request = GetEventsForBlockIDsRequest()
        request.type = type
        request.block_ids = block_ids

        return await self._unary_unary(
            "/flow.execution.ExecutionAPI/GetEventsForBlockIDs",
            request,
            GetEventsForBlockIDsResponse,
        )

    async def get_transaction_result(
        self, *, block_id: bytes = b"", transaction_id: bytes = b""
    ) -> GetTransactionResultResponse:
        """GetTransactionResult gets the result of a transaction."""

        request = GetTransactionResultRequest()
        request.block_id = block_id
        request.transaction_id = transaction_id

        return await self._unary_unary(
            "/flow.execution.ExecutionAPI/GetTransactionResult",
            request,
            GetTransactionResultResponse,
        )
