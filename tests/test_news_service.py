import unittest
from unittest.mock import patch, Mock
from app.services.news_service import NewsService
from fastapi import HTTPException

class TestNewsService(unittest.TestCase):

    def setUp(self):
        self.news_service = NewsService()

    @patch('app.services.news_service.feedparser.parse')
    def test_get_headlines_success(self, mock_parse):
        # Arrange: Mock the return value of feedparser.parse
        mock_feed = Mock()
        mock_feed.bozo = 0
        mock_feed.entries = [
            {'title': 'Test Headline 1', 'link': 'http://example.com/1'},
            {'title': 'Test Headline 2', 'link': 'http://example.com/2'},
        ]
        mock_parse.return_value = mock_feed

        # Act
        headlines = self.news_service.get_headlines()

        # Assert
        self.assertEqual(len(headlines), 2)
        self.assertEqual(headlines[0]['title'], 'Test Headline 1')
        mock_parse.assert_called_with(self.news_service.rss_url)

    @patch('app.services.news_service.feedparser.parse')
    def test_get_headlines_failure_bozo(self, mock_parse):
        # Arrange: Mock a malformed feed
        mock_feed = Mock()
        mock_feed.bozo = 1
        mock_feed.bozo_exception = "It broke"
        mock_parse.return_value = mock_feed

        # Act & Assert
        with self.assertRaises(HTTPException) as cm:
            self.news_service.get_headlines()
        self.assertEqual(cm.exception.status_code, 500)

    @patch('app.services.news_service.requests.get')
    def test_get_summary_success(self, mock_get):
        # Arrange: Mock the return value of requests.get
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_html = """
        <html><body>
            <div id="detail">
                <p>这是第一句话。</p>
                <p>这是第二句话！</p>
                <p>这是第三句话？</p>
                <p>这是第四句话，不应出现在摘要中。</p>
            </div>
        </body></html>
        """
        mock_response.content = mock_html.encode('utf-8')
        mock_get.return_value = mock_response

        # Act
        result = self.news_service.get_summary("http://example.com/article")

        # Assert
        expected_summary = "这是第一句话。这是第二句话！这是第三句话？"
        self.assertIn("summary", result)
        self.assertEqual(result["summary"], expected_summary)
        mock_get.assert_called_with("http://example.com/article", timeout=10)

    def test_summarize_text_chinese(self):
        # Test the internal _summarize_text method directly with Chinese text
        text = "这是第一句。这是第二句！这是第三句话？这是第四句。"
        summary = self.news_service._summarize_text(text, sentence_count=3)
        self.assertEqual(summary, "这是第一句。这是第二句！这是第三句话？")

    def test_summarize_text_empty(self):
        # Test summarizing empty text
        summary = self.news_service._summarize_text("", sentence_count=3)
        self.assertEqual(summary, "")

if __name__ == '__main__':
    unittest.main()
