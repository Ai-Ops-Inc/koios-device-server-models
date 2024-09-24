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
from datetime import datetime

import pytest
from pydantic import ValidationError

from models.history import History


class HistoryModelTest(unittest.TestCase):

    def test_valid(self):
        current_date = datetime.now()
        json = {
            "id": 1,
            "value": 1.0,
            "timestamp": current_date.isoformat(),
        }
        history = History(id=1, value=1.0, timestamp=current_date)
        from_json = History.model_validate(json)
        self.assertEqual(history, from_json)

    def test_invalid_extra_value(self):
        current_date = datetime.now()
        json = {
            "id": 1,
            "value": 1.0,
            "timestamp": current_date.isoformat(),
            "extra": "extra",
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_empty(self):
        json = {}
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_id_string(self):
        current_date = datetime.now()
        json = {
            "id": "Hello!",
            "value": 1.0,
            "timestamp": current_date.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_id_missing(self):
        current_date = datetime.now()
        json = {
            "value": 1.0,
            "timestamp": current_date.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_value_missing(self):
        current_date = datetime.now()
        json = {
            "id": 1,
            "timestamp": current_date.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_value_string(self):
        current_date = datetime.now()
        json = {
            "id": 1,
            "value": "string",
            "timestamp": current_date.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_timestamp_missing(self):
        json = {
            "id": 1,
            "value": 1.0,
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_timestamp_seconds(self):
        current_date = datetime.now()
        json = {"id": 1, "value": 1.0, "timestamp": current_date}
        history = History(id=1, value=1.0, timestamp=current_date)
        from_json = History.model_validate(json)
        self.assertEqual(history, from_json)

    def test_timestamp_string(self):
        json = {"id": 1, "value": 1.0, "timestamp": "string"}
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)
