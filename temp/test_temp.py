from unittest.mock import MagicMock, patch
from requests import HTTPError, Timeout
from temp import google_query


class TestRequestsCall:
    """
    example text that mocks requests.get and
    returns a mock Response object
    """

    def _mock_response(
        self,
        status=200,
        content="CONTENT",
        json_data=None,
        raise_for_status=None,
    ):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things
        """
        mock_resp = MagicMock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = MagicMock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = MagicMock(return_value=json_data)
        return mock_resp

    @patch("temp.requests.get")
    def test_google_query(self, mock_get):
        """test google query method"""
        mock_resp = self._mock_response(content="ELEPHANTS")
        mock_get.return_value = mock_resp

        result = google_query("elephants")
        assert result == "ELEPHANTS"
        mock_resp.raise_for_status.assert_called()

    @patch("temp.requests.get", side_effect=HTTPError)
    def test_failed_query_http(self, mock_get):
        """test case where google is down"""
        resp = google_query("elephants")
        assert resp is False

    @patch("temp.requests.get")
    def test_failed_query_http_2(self, mock_get):
        """test case where google is down"""
        mock_resp = self._mock_response(status=400, raise_for_status=HTTPError)
        mock_get.return_value = mock_resp
        resp = google_query("elephants")
        assert resp is False

    @patch("temp.requests.get", side_effect=Timeout)
    def test_failed_query_tout(self, mock_get):
        """test case where google is down"""
        resp = google_query("elephants")
        assert resp is True
