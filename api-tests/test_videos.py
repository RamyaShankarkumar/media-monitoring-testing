import requests

@pytest.mark.integration
def test_get_videos():
    r = requests.get("http://localhost:8000/videos")
    assert r.status_code == 200
