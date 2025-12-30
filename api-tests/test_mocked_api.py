from unittest.mock import patch
import requests

@patch('requests.get')
def test_mocked_api(mock_get):
    mock_get.return_value.status_code = 200
    r = requests.get("http://fake-api.com/videos")
    assert r.status_code == 200
