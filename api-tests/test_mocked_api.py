from unittest.mock import patch
import requests

@patch("requests.get")
def test_get_videos(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "videos": ["video1", "video2"]
    }

    
    response = requests.get("http://localhost:8000/videos")

    
    assert response.status_code == 200
    assert "videos" in response.json()
    assert len(response.json()["videos"]) == 2
