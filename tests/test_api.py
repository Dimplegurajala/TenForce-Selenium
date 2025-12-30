import requests
import pytest

# Define the base URL of your local mock server
BASE_URL = "http://127.0.0.1:5000"

def test_get_careers_status_and_schema():
    """Validates the Careers endpoint returns 200 OK and correct JSON structure."""
    response = requests.get(f"{BASE_URL}/api/careers")
    
    # 1. Status Code Validation
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    
    # 2. Schema/Data Integrity Validation
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["jobs"], list)
    assert len(data["jobs"]) > 0
    
    # 3. Specific Field Validation (Business Logic)
    assert "SDET" in data["jobs"]


def test_invalid_endpoint_returns_404():
    """Negative test to ensure the server handles unknown routes correctly."""
    response = requests.get(f"{BASE_URL}/api/invalid-route")
    assert response.status_code == 404