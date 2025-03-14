####################################################################################################
# Copyright © 2024 Ai-OPs, Inc.
# All rights reserved.
# The source code contained herein is protected by copyright law and international treaties.
# Unauthorized reproduction or distribution of this source code, or any portion of it, may result in
# severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.
# www.ai-op.com
# www.ai-ops.document360.io/docs/end-user-license-agreement
####################################################################################################

from pydantic import BaseModel, Field, model_validator


class DeviceGetRequest(BaseModel):
    device_id: int | None = Field(default=None)
    skip: int = Field(default=0)
    limit: int = Field(default=10)
