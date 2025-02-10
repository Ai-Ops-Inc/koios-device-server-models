####################################################################################################
# Copyright © 2024 Ai-OPs, Inc.
# All rights reserved.
# The source code contained herein is protected by copyright law and international treaties.
# Unauthorized reproduction or distribution of this source code, or any portion of it, may result in
# severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.
# www.ai-op.com
# www.ai-ops.document360.io/docs/end-user-license-agreement
####################################################################################################
from pydantic import BaseModel, ConfigDict, model_validator


class Tag(BaseModel):
    model_config = ConfigDict(extra="forbid", from_attributes=True)

    id: int
    name: str
    description: str
    range_low: float
    range_high: float

    @model_validator(mode="after")
    def check_range_low_high(self):
        # Ensure both range_low and range_high are provided and validate the range
        if self.range_low >= self.range_high:
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
