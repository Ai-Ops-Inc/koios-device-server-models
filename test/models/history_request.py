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

from models.history_request import HistoryRequest


class HistoryRequestModelTest(unittest.TestCase):
    def test_valid(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "id": 1,
            "count": 10,
            "start": start.isoformat(),
            "stop": now.isoformat(),
        }
        history_request = HistoryRequest(id=1, start=start, stop=now, count=10)
        from_json = HistoryRequest.model_validate(json)
        self.assertEqual(history_request, from_json)

    def test_valid_count_missing(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "id": 1,
            "start": start.isoformat(),
            "stop": now.isoformat(),
        }

        history_request = HistoryRequest(id=1, start=start, stop=now)
        from_json = HistoryRequest.model_validate(json)
        self.assertEqual(history_request, from_json)

    def test_valid_start_missing(self):
        now = datetime.now()
        json = {
            "id": 1,
            "count": 10,
            "stop": now.isoformat(),
        }
        history_request = HistoryRequest(id=1, count=10, stop=now)
        from_json = HistoryRequest.model_validate(json)
        self.assertEqual(history_request, from_json)

    def test_valid_stop_missing(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "id": 1,
            "count": 10,
            "start": start.isoformat(),
        }
        history_request = HistoryRequest(id=1, start=start, count=10)
        from_json = HistoryRequest.model_validate(json)
        self.assertEqual(history_request, from_json)

    def test_valid_timestamp_seconds(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "id": 1,
            "count": 10,
            "start": start,
            "stop": now,
        }
        history_request = HistoryRequest(id=1, start=start, stop=now, count=10)
        from_json = HistoryRequest.model_validate(json)
        self.assertEqual(history_request, from_json)

    def test_valid_timestamp_mismatch(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "id": 1,
            "count": 10,
            "start": start.isoformat(),
            "stop": now,
        }
        history_request = HistoryRequest(id=1, start=start, stop=now, count=10)
        from_json = HistoryRequest.model_validate(json)
        self.assertEqual(history_request, from_json)

    def test_invalid_empty(self):
        json = {}
        with pytest.raises(ValidationError):
            _ = HistoryRequest.model_validate(json)

    def test_invalid_id_missing(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "count": 10,
            "start": start.isoformat(),
            "stop": now.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = HistoryRequest.model_validate(json)

    def test_id_just(self):
        json = {
            "id": 1,
        }
        history_request = HistoryRequest(id=1)
        from_json = HistoryRequest.model_validate(json)
        self.assertEqual(history_request, from_json)

    def test_invalid_id_string(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "count": 10,
            "start": start.isoformat(),
            "stop": now.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = HistoryRequest.model_validate(json)

    def test_invalid_count_string(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "id": 1,
            "count": "string",
            "start": start.isoformat(),
            "stop": now.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = HistoryRequest.model_validate(json)

    def test_invalid_start_string(self):
        now = datetime.now()
        json = {
            "id": 1,
            "count": 10,
            "start": "hello",
            "stop": now.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = HistoryRequest.model_validate(json)

    def test_invalid_stop_string(self):
        now = datetime.now()
        start = now - timedelta(hours=24)
        json = {
            "id": 1,
            "count": 10,
            "start": start.isoformat(),
            "stop": "hello",
        }
        with pytest.raises(ValidationError):
            _ = HistoryRequest.model_validate(json)

    def test_invalid_stop_before_start(self):
        now = datetime.now()
        start = now + timedelta(hours=24)
        json = {
            "id": 1,
            "count": 10,
            "start": start.isoformat(),
            "stop": now.isoformat(),
        }
        with pytest.raises(ValidationError):
            _ = HistoryRequest.model_validate(json)
