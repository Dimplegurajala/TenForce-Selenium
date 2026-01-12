import requests
from jsonschema import validate
import pytest

# Your TenForce Career Schema
CAREER_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "jobs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "title": {"type": "string"},
                    "contact": {"type": "string"}
                },
                "required": ["id", "title"]
            }
        }
    },
    "required": ["status", "jobs"]
}

API_URL = "http://127.0.0.1:5000/api/v1/careers"

def test_career_data_integrity():
    """Validates API Data Integrity without external config files."""
    response = requests.get(API_URL)
    data = response.json()
    
    # Ensuring the SDET role is present (Your Resume Project #1) 
    assert any(job.get('title') == "SDET" for job in data['jobs']), "SDET role missing!"
    
    # Data Integrity: Matching the contact email from your mock server
    assert data['jobs'][0].get('contact') == "jobs@tenforce.com"