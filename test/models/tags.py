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

from models.tags import Tag


class TagsModelTest(unittest.TestCase):

    def test_valid(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=0.2,
            range_high=0.8,
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_invalid_empty(self):
        json = {}
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_extra_value(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
            "extra": 1,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_id_missing(self):
        json = {
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_device_id_missing(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_id_string(self):
        json = {
            "id": "TEST_STRING",
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_name_missing(self):
        json = {
            "id": 1,
            "device_id": 12,
            "description": "This is a invalid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_description_missing(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_datatype_missing(self):
        json = {
            "id": 1,
            "device_id": 12,
            "description": "This is a invalid tag",
            "name": "Valid Tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_datatype(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "testing",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)


class TagsModelFloat(unittest.TestCase):
    def test_valid_float(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=0.2,
            range_high=0.8,
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_invalid_max_length(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "max_length": "8",
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_valid_float_int_range(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 2,
            "range_high": 8,
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=2,
            range_high=8,
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_valid_float_range_low_int(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 2,
            "range_high": 2.8,
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=2,
            range_high=2.8,
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_valid_float_range_high_int(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": 8,
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="float",
            range_low=0.2,
            range_high=8,
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_invalid_range_low_higher_than_range_hi(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "float",
            "range_low": 0.8,
            "range_high": 0.2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_missing(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "float",
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_string(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "float",
            "range_low": "hello",
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_high_missing(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "float",
            "range_low": 0.2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_high_string(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "float",
            "range_low": 0.2,
            "range_high": "hello",
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)


class TagsModelInt(unittest.TestCase):
    def test_valid_int(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "int",
            "range_low": 2,
            "range_high": 8,
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="int",
            range_low=2,
            range_high=8,
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_invalid_max_length(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "max_length": "8",
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_float(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "range_low": 0.2,
            "range_high": "8",
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_high_float(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "range_low": 2,
            "range_high": "0.8",
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_higher_than_range_hi(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "range_low": 8,
            "range_high": 2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_missing(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "range_high": 8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_string(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "range_low": "hello",
            "range_high": 8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_high_string(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "range_low": 2,
            "range_high": "hello",
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_high_missing(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a invalid tag",
            "data_type": "int",
            "range_low": 2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)


class TagsModelString(unittest.TestCase):
    def test_valid_string(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "string",
            "max_length": 12,
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="string",
            max_length=12,
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_invalid_all(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "string",
            "max_length": 12,
            "range_low": 2,
            "range_high": 2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "string",
            "range_low": 2,
            "range_high": 2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)


class TagsModelBool(unittest.TestCase):
    def test_valid_string(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "bool",
        }
        tag = Tag(
            id=1,
            device_id=12,
            name="Valid Tag",
            description="This is a valid tag",
            data_type="bool",
        )
        from_json = Tag.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_invalid_max_length(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "bool",
            "max_length": 12,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range(self):
        json = {
            "id": 1,
            "device_id": 12,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "data_type": "bool",
            "range_low": 2,
            "range_high": 2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)
