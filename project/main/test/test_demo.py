from starlette.testclient import TestClient
from .conftest  import test_app
from app.server.app import app

client = TestClient(app)


def test_demo(test_app):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"demo": "demo!"}
