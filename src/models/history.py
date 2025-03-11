####################################################################################################
# Copyright © 2024 Ai-OPs, Inc.
# All rights reserved.
# The source code contained herein is protected by copyright law and international treaties.
# Unauthorized reproduction or distribution of this source code, or any portion of it, may result in
# severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.
# www.ai-op.com
# www.ai-ops.document360.io/docs/end-user-license-agreement
####################################################################################################

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator


class Value(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
    )

    value: float
    timestamp: datetime


class History(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
    )
    id: int
    values: list[Value] = Field(min_length=1)

    # @model_validator(mode="after")
    # def check_unique_date_time(self):
    #     timestamps = []
    #     for value in self.values:
    #         if value.timestamp in timestamps:
    #             raise ValueError()
    #         timestamps.append(value.timestamp)
    #     return self


#
# class HistoryError(Exception):
#     """
#     General device exception
#     """
#
#
# class HistoryNotFoundError(HistoryError):
#     """Exception raised when attempting to create a history that already exists."""
#
#     def __init__(self, history_id, message="History item not found"):
#         self.history_id = history_id
#         self.message = f"{message}: {history_id}"
#         super().__init__(self.message)
#
#
# class HistoryAlreadyExistError(HistoryError):
#     """Exception raised when attempting to create a history that already exists."""
#
#     def __init__(
#         self, history_id, history_timestamp, message="History item already exists"
#     ):
#         self.history_id = history_id
#         self.history_timestamp = history_timestamp
#         self.message = f"{message}: {history_id} {history_timestamp}"
#         super().__init__(self.message)
#
#
# class HistoryValueOutOfRangeError(HistoryError):
#     def __init__(
#         self, history_id, history_timestamp, message="History value out of range"
#     ):
#         self.history_id = history_id
#         self.history_value = history_value
#         self.message = f"{message}: {history_id} {history_timestamp}"
#         super().__init__(self.message)
