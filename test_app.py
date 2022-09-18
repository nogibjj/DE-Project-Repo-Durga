'''Test File'''
from fastapi.testclient import TestClient
import app as ap

client = TestClient(ap.app)

def test_root():
    '''Test the root'''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Databricks"}

test_root()
