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


class HistoryRequest(BaseModel):

    model_config = ConfigDict(extra="forbid")
    id: int
    start: datetime | None = Field(default=None)
    stop: datetime | None = Field(default=None)
    count: int | None = Field(default=None)

    @model_validator(mode="after")
    def check_range_low_high(self):
        # Ensure both range_low and range_high are provided and validate the range
        if self.start is not None and self.stop is not None:
            if self.start >= self.stop:
                raise ValueError()

        return self
