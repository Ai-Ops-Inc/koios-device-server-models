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
from datetime import datetime, timedelta

import pytest
from pydantic import ValidationError

from models.history import History, Value


class HistoryModelTest(unittest.TestCase):

    def test_valid_single(self):
        timestamp = datetime.now()
        json = {
            "id": 1,
            "values": [
                {
                    "value": 1.0,
                    "timestamp": timestamp.isoformat(),
                },
            ],
        }
        value = Value(value=1.0, timestamp=timestamp)
        values = []
        values.append(value)
        history = History(id=1, values=values)
        from_json = History.model_validate(json)
        self.assertEqual(history, from_json)

    def test_valid_list(self):
        timestamp = datetime.now()
        json = {
            "id": 1,
            "values": [
                {
                    "value": 1.0,
                    "timestamp": timestamp.isoformat(),
                },
                {
                    "value": 2.0,
                    "timestamp": (timestamp + timedelta(seconds=10)).isoformat(),
                },
            ],
        }
        value = Value(value=1.0, timestamp=timestamp)
        values = []
        values.append(value)
        new_value = Value(value=2.0, timestamp=(timestamp + timedelta(seconds=10)))
        values.append(new_value)
        history = History(id=1, values=values)
        from_json = History.model_validate(json)
        self.assertEqual(history, from_json)

    def test_invalid_duplicate_timestamps(self):
        timestamp = datetime.now()
        json = {
            "id": 1,
            "values": [
                {
                    "value": 1.0,
                    "timestamp": timestamp.isoformat(),
                },
                {
                    "value": 2.0,
                    "timestamp": timestamp.isoformat(),
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_empty(self):
        json = {
            "id": 1,
            "values": [],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_extra_value(self):
        timestamp = datetime.now()

        json = {
            "id": 1,
            "values": [
                {
                    "value": 1.0,
                    "timestamp": timestamp.isoformat(),
                },
            ],
            "extra": "extra",
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_id_string(self):
        timestamp = datetime.now()
        json = {
            "id": "Hello!",
            "values": [
                {
                    "value": 1.0,
                    "timestamp": timestamp.isoformat(),
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_id_missing(self):
        timestamp = datetime.now()
        json = {
            "values": [
                {
                    "value": 1.0,
                    "timestamp": timestamp.isoformat(),
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_value_missing(self):
        timestamp = datetime.now()
        json = {
            "id": 1,
            "values": [
                {"timestamp": timestamp.isoformat()},
            ],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_value_string(self):
        timestamp = datetime.now()
        json = {
            "id": 1,
            "values": [
                {
                    "value": "string",
                    "timestamp": timestamp.isoformat(),
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_timestamp_missing(self):
        json = {
            "id": 1,
            "values": [
                {
                    "value": 1.0,
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)

    def test_invalid_timestamp_seconds(self):
        timestamp = datetime.now()
        json = {
            "id": 1,
            "values": [
                {
                    "value": 1.0,
                    "timestamp": timestamp,
                },
            ],
        }
        value = Value(value=1.0, timestamp=timestamp)
        values = []
        values.append(value)
        history = History(id=1, values=values)
        from_json = History.model_validate(json)
        self.assertEqual(history, from_json)

    def test_invalid_timestamp_string(self):
        json = {
            "id": 1,
            "values": [
                {
                    "value": 1.0,
                    "timestamp": "string",
                },
            ],
        }
        with pytest.raises(ValidationError):
            _ = History.model_validate(json)
