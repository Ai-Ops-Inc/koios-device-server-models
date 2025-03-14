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

from models.tags_get_request import TagGetRequest


class TagGetRequestTest(unittest.TestCase):
    def test_valid_device_id(self):
        json = {"device_id": 10}
        tag_get_request = TagGetRequest(device_id=10)

        from_json = TagGetRequest.model_validate(json)
        self.assertEqual(tag_get_request, from_json)

    def test_valid_device_id_with_pagination(self):
        json = {"id": 10, "skip": 100, "limit": 10}
        tag_get_request = TagGetRequest(id=10, skip=100, limit=10)

        from_json = TagGetRequest.model_validate(json)
        self.assertEqual(tag_get_request, from_json)

    def test_valid_id(self):
        json = {"id": 10}
        tag_get_request = TagGetRequest(id=10)

        from_json = TagGetRequest.model_validate(json)
        self.assertEqual(tag_get_request, from_json)

    def test_valid_id_with_pagination(self):
        json = {"id": 10, "skip": 100, "limit": 10}
        tag_get_request = TagGetRequest(id=10, skip=100, limit=10)

        from_json = TagGetRequest.model_validate(json)
        self.assertEqual(tag_get_request, from_json)

    def test_invalid_pagination_both_device_and_id(self):
        json = {"device_id": 10, "id": 10, "skip": 100, "limit": 10}

        with pytest.raises(ValidationError):
            _ = TagGetRequest.model_validate(json)

    def test_invalid_device_id_string(self):
        json = {"device_id": "bob"}

        with pytest.raises(ValidationError):
            _ = TagGetRequest.model_validate(json)

    def test_invalid_id_string(self):
        json = {"id": "bob"}

        with pytest.raises(ValidationError):
            _ = TagGetRequest.model_validate(json)

    def test_invalid_skip_string(self):
        json = {"id": 10, "skip": "bob"}

        with pytest.raises(ValidationError):
            _ = TagGetRequest.model_validate(json)

    def test_invalid_limit_string(self):
        json = {"id": 10, "limit": "bob"}

        with pytest.raises(ValidationError):
            _ = TagGetRequest.model_validate(json)
