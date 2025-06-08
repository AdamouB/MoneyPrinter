import requests
from Backend import search


def test_search_for_stock_videos(monkeypatch):
    mock_response = {
        "videos": [
            {
                "duration": 5,
                "video_files": [
                    {"link": "https://example.com/video-files/low.mp4", "width": 640, "height": 480},
                    {"link": "https://example.com/video-files/high.mp4", "width": 1280, "height": 720},
                ],
            }
        ]
    }

    class MockResp:
        def json(self):
            return mock_response

    def mock_get(url, headers):
        assert "cats" in url
        assert headers.get("Authorization") == "APIKEY"
        return MockResp()

    monkeypatch.setattr(requests, "get", mock_get)

    result = search.search_for_stock_videos("cats", "APIKEY", it=1, min_dur=2)
    assert result == ["https://example.com/video-files/high.mp4"]
