import server
import pytest


@pytest.fixture
def client():
    server.app.config["TESTING"] = True
    client = server.app.test_client()
    yield client
    
