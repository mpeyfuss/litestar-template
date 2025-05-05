def test_index(api_client):
    r = api_client.get("/")

    assert r.text == "Hello World."


def test_health(api_client):
    r = api_client.get("/health")
    data = r.json()
    assert data["status"] == "ok"
