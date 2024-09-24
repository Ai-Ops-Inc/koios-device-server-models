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
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        tag = Tag(
            id=1,
            name="Valid Tag",
            description="This is a valid tag",
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
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
            "extra": 1,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_id_missing(self):
        json = {
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_id_string(self):
        json = {
            "id": "TEST_STRING",
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_name_missing(self):
        json = {
            "id": 1,
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_description_missing(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_missing(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_string(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": "hello",
            "range_high": 0.8,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_high_missing(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_high_string(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": "hello",
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)

    def test_invalid_range_low_higher_than_range_hi(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.8,
            "range_high": 0.2,
        }
        with pytest.raises(ValidationError):
            _ = Tag.model_validate(json)
