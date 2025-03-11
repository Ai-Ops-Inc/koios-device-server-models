####################################################################################################
# Copyright © 2024 Ai-OPs, Inc.
# All rights reserved.
# The source code contained herein is protected by copyright law and international treaties.
# Unauthorized reproduction or distribution of this source code, or any portion of it, may result in
# severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.
# www.ai-op.com
# www.ai-ops.document360.io/docs/end-user-license-agreement
####################################################################################################

import unittest

import pytest
from pydantic import ValidationError

from models.device import Device
from models.tags import Tag


class TagsModelTest(unittest.TestCase):

    def test_valid_empty_tag_list(self):
        json = {
            "id": 1,
            "name": "Valid Device",
            "description": "This is a valid device",
        }
        device = Device(
            id=1,
            name="Valid Device",
            description="This is a valid device",
        )
        from_json = Device.model_validate(json)
        self.assertEqual(device, from_json)

    def test_valid_tag(self):
        json = {
            "id": 1,
            "name": "Valid Device",
            "description": "This is a valid device",
            "tags": [
                {
                    "id": 1,
                    "device_id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
            ],
        }
        tag = Tag(
            id=1,
            device_id=1,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=0.2,
            range_high=0.8,
        )
        tags = []
        tags.append(tag)
        device = Device(
            id=1,
            name="Valid Device",
            description="This is a valid device",
            tags=tags,
        )
        from_json = Device.model_validate(json)
        self.assertEqual(device, from_json)

    def test_valid_tag_list(self):
        json = {
            "id": 1,
            "name": "Valid Device",
            "description": "This is a valid device",
            "tags": [
                {
                    "id": 1,
                    "device_id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
                {
                    "id": 3,
                    "device_id": 1,
                    "name": "Valid Tag two",
                    "description": "This is a valid tag two",
                    "data_type": "int",
                    "range_low": 2,
                    "range_high": 8,
                },
            ],
        }
        tags = []
        tag = Tag(
            id=1,
            device_id=1,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=0.2,
            range_high=0.8,
        )
        tag2 = Tag(
            id=3,
            device_id=1,
            name="Valid Tag two",
            description="This is a valid tag two",
            data_type="int",
            range_low=2,
            range_high=8,
        )

        tags.append(tag)
        tags.append(tag2)
        device = Device(
            id=1,
            name="Valid Device",
            description="This is a valid device",
            tags=tags,
        )
        from_json = Device.model_validate(json)
        self.assertEqual(device, from_json)

    def test_valid_tag_json_missing_device_id(self):
        json = {
            "id": 1,
            "name": "Valid Device",
            "description": "This is a valid device",
            "tags": [
                {
                    "id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
            ],
        }
        tag = Tag(
            id=1,
            device_id=1,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=0.2,
            range_high=0.8,
        )
        tags = []
        tags.append(tag)
        device = Device(
            id=1,
            name="Valid Device",
            description="This is a valid device",
            tags=tags,
        )
        from_json = Device.model_validate(json)
        self.assertEqual(device, from_json)

    def test_valid_tag_list_json_missing_device_id(self):
        json = {
            "id": 1,
            "name": "Valid Device",
            "description": "This is a valid device",
            "tags": [
                {
                    "id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
                {
                    "id": 3,
                    "name": "Valid Tag two",
                    "description": "This is a valid tag two",
                    "data_type": "int",
                    "range_low": 2,
                    "range_high": 8,
                },
            ],
        }
        tags = []
        tag = Tag(
            id=1,
            device_id=1,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=0.2,
            range_high=0.8,
        )
        tag2 = Tag(
            id=3,
            device_id=1,
            name="Valid Tag two",
            description="This is a valid tag two",
            data_type="int",
            range_low=2,
            range_high=8,
        )

        tags.append(tag)
        tags.append(tag2)
        device = Device(
            id=1,
            name="Valid Device",
            description="This is a valid device",
            tags=tags,
        )
        from_json = Device.model_validate(json)
        self.assertEqual(device, from_json)

    def test_invalid_empty(self):
        json = {}
        with pytest.raises(ValidationError):
            _ = Device.model_validate(json)

    def test_invalid_missing_id(self):
        json = {
            "name": "Valid Device",
            "description": "This is a valid device",
            "tags": [
                {
                    "id": 1,
                    "device_id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = Device.model_validate(json)

    def test_invalid_missing_name(self):
        json = {
            "id": 1,
            "description": "This is a valid device",
            "tags": [
                {
                    "id": 1,
                    "device_id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = Device.model_validate(json)

    def test_invalid_missing_description(self):
        json = {
            "id": 1,
            "name": "Valid Device",
            "tags": [
                {
                    "id": 1,
                    "device_id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = Device.model_validate(json)

    def test_invalid_duplicate_tag_id(self):
        json = {
            "id": 1,
            "name": "Valid Device",
            "description": "This is a valid device",
            "tags": [
                {
                    "id": 1,
                    "name": "Valid Tag",
                    "description": "This is a valid tag",
                    "data_type": "float",
                    "range_low": 0.2,
                    "range_high": 0.8,
                },
                {
                    "id": 1,
                    "name": "Valid Tag two",
                    "description": "This is a valid tag two",
                    "data_type": "int",
                    "range_low": 2,
                    "range_high": 8,
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = Device.model_validate(json)
