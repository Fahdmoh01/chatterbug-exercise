from fastapi.testclient import TestClient
from app.main import app


class TestGeneratePasswordRoute:
    def setup_class(self):
        self.client = TestClient(app)

    def test_valid_request(self):
        response = self.client.post("/generate-password", json={"length": 12})
        assert response.status_code == 200
        data = response.json()
        assert "generated_password" in data
        assert data["length"] == 12

    def test_invalid_request(self):
        response = self.client.post(
            "/generate-password",
            json={
                "length": 12,
                "symbols": False,
                "digits": False,
                "lowercase": False,
                "uppercase": False,
            },
        )
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert (
            "One of (lowercase, uppercase, digits, or symbols) must be set to True"
            in data["detail"]["error"]
        )

    def test_minimum_length_validation(self):
        response = self.client.post("/generate-password", json={"length": 5})
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert (
            "length must be a positive integer greater than or equal to 8 but not longer than 256"
            in data["detail"]["error"]
        )

    def test_maximum_length_validation(self):
        response = self.client.post("/generate-password", json={"length": 512})
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert (
            "length must be a positive integer greater than or equal to 8 but not longer than 256"
            in data["detail"]["error"]
        )
