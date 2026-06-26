import unittest
from unittest.mock import patch
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


class AuthRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_register_requires_all_fields(self):
        response = self.client.post('/api/register', json={"username": "Alice"})
        self.assertEqual(response.status_code, 400)
        self.assertIn('missing', response.get_json()['message'].lower())

    @patch('routes.auth.User.get_user_by_email', return_value=None)
    def test_login_unknown_user_returns_401(self, _mock_get_user):
        response = self.client.post('/api/login', json={
            "email": "missing@example.com",
            "password": "secret"
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('invalid', response.get_json()['message'].lower())


if __name__ == '__main__':
    unittest.main()
