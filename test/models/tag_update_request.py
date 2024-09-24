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

from models.tags_update_request import TagUpdateRequest


class TagsModelTest(unittest.TestCase):

    def test_valid(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }
        tag = TagUpdateRequest(
            id=1,
            name="Valid Tag",
            description="This is a valid tag",
            range_low=0.2,
            range_high=0.8,
        )
        from_json = TagUpdateRequest.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_invalid_empty(self):
        json = {}
        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_invalid_extra_value(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
            "extra": "extra",
        }
        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_invalid_id_missing(self):
        json = {
            "name": "Valid Tag",
            "description": "This is a valid tag",
            "range_low": 0.2,
            "range_high": 0.8,
        }

        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_invalid_id_just(self):
        json = {"id": 1}

        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_invalid_id_string(self):
        json = {"id": "TEST"}

        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_invalid_range_low_string(self):
        json = {
            "id": 1,
            "range_low": "hello",
        }
        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_invalid_range_high_string(self):
        json = {
            "id": 1,
            "range_high": "hello",
        }
        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_invalid_range_low_higher_than_range_high(self):
        json = {
            "id": 1,
            "range_low": 1,
            "range_high": 0.1,
        }
        with pytest.raises(ValidationError):
            _ = TagUpdateRequest.model_validate(json)

    def test_name(self):
        json = {
            "id": 1,
            "name": "Valid Tag",
        }
        tag = TagUpdateRequest(
            id=1,
            name="Valid Tag",
        )
        from_json = TagUpdateRequest.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_description(self):
        json = {
            "id": 1,
            "description": "This is a valid tag",
        }
        tag = TagUpdateRequest(
            id=1,
            description="This is a valid tag",
        )
        from_json = TagUpdateRequest.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_range_low(self):
        json = {
            "id": 1,
            "range_low": 0.2,
        }
        tag = TagUpdateRequest(
            id=1,
            range_low=0.2,
        )
        from_json = TagUpdateRequest.model_validate(json)
        self.assertEqual(tag, from_json)

    def test_range_high(self):
        json = {
            "id": 1,
            "range_high": 0.8,
        }
        tag = TagUpdateRequest(
            id=1,
            range_high=0.8,
        )
        from_json = TagUpdateRequest.model_validate(json)
        self.assertEqual(tag, from_json)
