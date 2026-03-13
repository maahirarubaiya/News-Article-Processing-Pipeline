"""
Tests for the SearchNews class
"""
import unittest
import sys
from unittest.mock import patch, mock_open, MagicMock
sys.path.append(".")
from src.search_news import SearchNews
from src.article import Article

FAKE_RESPONSE = {
    "articles": [
        {
            "url": "https://example.com/1",
            "source": {"name": "Example Source"},
            "author": "John Doe",
            "title": "Example Title",
            "description": "Example description.",
            "publishedAt": "2023-10-01T12:00:00Z",
            "content": "Example content."
        }
    ]
}

class TestSearchNews(unittest.TestCase):
    """Example test case for the SearchNews class"""

    def setUp(self) -> None:
        with patch("builtins.open", mock_open(read_data="fake_api_key")):
            self.searcher = SearchNews('key.txt')

    def test_invalid_key_file_raises_error(self) -> None:
        """Test that FileNotFoundError is raised when key file does not exist"""
        with self.assertRaises(FileNotFoundError):
            SearchNews('nonexistent_key.txt')

    def test_get_top_headlines_returns_list(self) -> None:
        """Test that get_top_headlines returns a list"""
        mock_resp = MagicMock()
        mock_resp.json.return_value = FAKE_RESPONSE
        with patch("requests.get", return_value=mock_resp):
            result = self.searcher.get_top_headlines()
        self.assertIsInstance(result, list)

    def test_get_top_headlines_returns_articles(self) -> None:
        """Test that get_top_headlines returns a list of Article objects"""
        mock_resp = MagicMock()
        mock_resp.json.return_value = FAKE_RESPONSE
        with patch("requests.get", return_value=mock_resp):
            result = self.searcher.get_top_headlines()
        for article in result:
            self.assertIsInstance(article, Article)

    def test_get_top_headlines_with_term_returns_list(self) -> None:
        """Test that get_top_headlines with a search term returns a list"""
        mock_resp = MagicMock()
        mock_resp.json.return_value = FAKE_RESPONSE
        with patch("requests.get", return_value=mock_resp):
            result = self.searcher.get_top_headlines("technology")
        self.assertIsInstance(result, list)

    def test_get_everything_returns_list(self) -> None:
        """Test that get_everything returns a list"""
        mock_resp = MagicMock()
        mock_resp.json.return_value = FAKE_RESPONSE
        with patch("requests.get", return_value=mock_resp):
            result = self.searcher.get_everything("python", language="en")
        self.assertIsInstance(result, list)

    def test_get_everything_returns_articles(self) -> None:
        """Test that get_everything returns a list of Article objects"""
        mock_resp = MagicMock()
        mock_resp.json.return_value = FAKE_RESPONSE
        with patch("requests.get", return_value=mock_resp):
            result = self.searcher.get_everything("python", language="en")
        for article in result:
            self.assertIsInstance(article, Article)

    def test_article_properties_are_strings_or_none(self) -> None:
        """Test that Article properties returned by API are strings or None"""
        mock_resp = MagicMock()
        mock_resp.json.return_value = FAKE_RESPONSE
        with patch("requests.get", return_value=mock_resp):
            result = self.searcher.get_top_headlines()
        if result:
            article = result[0]
            for prop in [article.url, article.source, article.author,
                         article.title, article.description,
                         article.published_at, article.content]:
                self.assertTrue(prop is None or isinstance(prop, str))

if __name__ == "__main__":
    unittest.main()