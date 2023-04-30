"""Test dummy"""

from fastapi.testclient import TestClient
import dummy


def test_addition():
    """
    Test dummy::addition
    """
    assert dummy.addition(1, 2) == 3

app = dummy.app()
client = TestClient(app)


def test_get_device():
    """
    test get devices
    """
    response = client.get("/devices")
    assert response.status_code == 200
    assert response.json() == ["device_01","device_02","device_03"]
