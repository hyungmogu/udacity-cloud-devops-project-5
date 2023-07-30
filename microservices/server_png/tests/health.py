import unittest
from fastapi.testclient import TestClient

from server_png.app import app

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_test_client_server_is_running(self):
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
    
if __name__ == "__main__":
    unittest.main()