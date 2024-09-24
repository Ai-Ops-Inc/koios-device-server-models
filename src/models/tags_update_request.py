####################################################################################################
# Copyright © 2024 Ai-OPs, Inc.
# All rights reserved.
# The source code contained herein is protected by copyright law and international treaties.
# Unauthorized reproduction or distribution of this source code, or any portion of it, may result in
# severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.
# www.ai-op.com
# www.ai-ops.document360.io/docs/end-user-license-agreement
####################################################################################################

from pydantic import (BaseModel, ConfigDict, Field, ValidationError,
                      model_validator)


class TagUpdateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    range_low: float | None = Field(default=None)
    range_high: float | None = Field(default=None)

    @model_validator(mode="before")
    def check_at_least_one_field(cls, values):
        if len(values) == 1:
            raise ValueError()
        return values

    @model_validator(mode="after")
    def check_range_low_high(self):
        # Ensure both range_low and range_high are provided and validate the range
        if self.range_low is not None and self.range_high is not None:
            if self.range_low >= self.range_high:
                raise ValueError()
        return self
