import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app  # noqa: E402
from parsers import parse_evidence  # noqa: E402

DATA = {
    "role": "owner",
    "user_details": {"id": 120000, "first_name": "anec", "last_name": "dotes"},
    "groups": ["admins"],
}


class ParserTest(unittest.TestCase):
    def test_single_and_combined(self):
        config = {"id": [["user_details", "id"]],
                  "name": [["user_details", "first_name"], ["user_details", "last_name"]]}
        self.assertEqual(parse_evidence(DATA, config), {"id": 120000, "name": "anec dotes"})

    def test_combined_non_string(self):
        config = {"x": [["user_details", "id"], ["role"]]}
        self.assertEqual(parse_evidence(DATA, config), {"x": "120000 owner"})

    def test_missing_paths(self):
        config = {"a": [["role", "x"]], "b": [["groups", 5]], "c": [["nope"]],
                  "d": [["user_details", "first_name"], ["nope"]]}
        self.assertEqual(parse_evidence(DATA, config), {"a": "", "b": "", "c": "", "d": "anec"})

    def test_list_index(self):
        self.assertEqual(parse_evidence(DATA, {"g": [["groups", 0]]}), {"g": "admins"})


class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_ok(self):
        res = self.client.post("/parse", json={
            "parsing_configuration": {"id": [["user_details", "id"]]},
            "payload": {"evidence_id": 1, "evidence_data": [DATA]}})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"evidence_id": 1, "headers": ["id"], "rows": [{"id": 120000}]})

    def test_bad_requests(self):
        bodies = [
            None,
            {"payload": {}},
            {"parsing_configuration": {}, "payload": {"evidence_id": 1}},
            {"parsing_configuration": {"id": ["user_details", "id"]},
             "payload": {"evidence_id": 1, "evidence_data": []}},
        ]
        for body in bodies:
            res = self.client.post("/parse", json=body) if body else self.client.post("/parse", data="x")
            self.assertEqual(res.status_code, 400, body)
            self.assertIn("error", res.get_json())


if __name__ == "__main__":
    unittest.main()
