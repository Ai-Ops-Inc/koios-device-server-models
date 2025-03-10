####################################################################################################
# Copyright © 2024 Ai-OPs, Inc.
# All rights reserved.
# The source code contained herein is protected by copyright law and international treaties.
# Unauthorized reproduction or distribution of this source code, or any portion of it, may result in
# severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.
# www.ai-op.com
# www.ai-ops.document360.io/docs/end-user-license-agreement
####################################################################################################
from enum import Enum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class Tag(BaseModel):
    model_config = ConfigDict(extra="forbid", from_attributes=True)

    id: int
    name: str
    device_id: int
    description: str
    range_low: int | float | None = Field(default=None)
    range_high: int | float | None = Field(default=None)
    max_length: int | None = Field(default=None)
    data_type: Literal["int", "float", "string", "bool"]

    @model_validator(mode="after")
    def check_type(self):
        if (
            self.range_low is None
            and self.range_high is None
            and self.max_length is None
            and self.data_type != "bool"
        ):
            raise ValueError()
        return self

    @model_validator(mode="after")
    def check_float(self):
        # Ensure both range_low and range_high are provided and validate the range
        if self.data_type in ["int", "float"]:
            if self.max_length is not None:
                raise ValueError()
            if self.range_low is None or self.range_high is None:
                raise ValueError()
            if self.data_type == "int":
                if not isinstance(self.range_low, int) or not isinstance(
                    self.range_high, int
                ):
                    raise ValueError()

            if self.range_low >= self.range_high:
                raise ValueError()
        return self

    @model_validator(mode="after")
    def check_string(self):
        # Ensure if a string then only max length is there.
        if self.data_type == "string":
            if self.range_low is not None or self.range_high is not None:
                raise ValueError()
            if self.max_length is None or self.max_length <= 0:
                raise ValueError()
        return self

    @model_validator(mode="after")
    def check_bool(self):
        # Ensure if Boolean then make sure the other types are not valid.
        if self.data_type == "bool":
            if (
                self.range_low is not None
                or self.range_high is not None
                or self.max_length is not None
            ):
                raise ValueError()
        return self


class TagError(Exception):
    """
    General device exception
    """


class TagBadRequestError(TagError):
    """Exception raised when there is a bad request."""

    def __init__(self, tag_name, message="Request is bad"):
        self.tag_name = tag_name
        self.message = f"{message}: {tag_name}"
        super().__init__(self.message)


class TagAlreadyExistError(TagError):
    """Exception raised when attempting to create a tag that already exists."""

    def __init__(self, tag_name, message="Tag already exists"):
        self.tag_name = tag_name
        self.message = f"{message}: {tag_name}"
        super().__init__(self.message)


class TagNotFoundError(TagError):
    """Exception raised when attempting to create a tag that already exists."""

    def __init__(self, tag_name, message="Tag not found"):
        self.tag_name = tag_name
        self.message = f"{message}: {tag_name}"
        super().__init__(self.message)
