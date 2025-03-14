####################################################################################################
# Copyright © 2024 Ai-OPs, Inc.
# All rights reserved.
# The source code contained herein is protected by copyright law and international treaties.
# Unauthorized reproduction or distribution of this source code, or any portion of it, may result in
# severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.
# www.ai-op.com
# www.ai-ops.document360.io/docs/end-user-license-agreement
####################################################################################################

from pydantic import (BaseModel, ConfigDict, Field, field_validator,
                      model_validator)

from models.tags import Tag


class Device(BaseModel):
    model_config = ConfigDict(extra="forbid", from_attributes=True)
    id: int
    name: str
    description: str
    tags: list[Tag] = Field(default=[])

    @field_validator("tags", mode="before")
    @classmethod
    def add_device_id(cls, tags, values):
        if "id" in values.data:
            device_id = values.data["id"]
            for tag in tags:
                if not isinstance(tag, Tag):
                    if "device_id" not in tag:
                        tag["device_id"] = device_id
        return tags

    @model_validator(mode="after")
    def check_tag_list(self):
        ids = []
        for tag in self.tags:
            if tag.id in ids:
                raise ValueError()
            ids.append(tag.id)
        return self
