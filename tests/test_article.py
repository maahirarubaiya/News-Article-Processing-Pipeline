"""
Tests for the Article class
"""
import unittest
import sys
sys.path.append(".")
from src.article import Article
# You may use # type: ignore to ignore the mypy error when accessing a
# read-only property (which should raise an AttributeError).
class TestArticle(unittest.TestCase):
    """Example test case for the Article class"""
    def test_url_is_read_only(self) -> None:
        """Test that the url property is set correctly"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.url, "https://example.com/article")
        with self.assertRaises(AttributeError):
            article.url = "https://example.com/new-article" # type: ignore
        self.assertEqual(article.url, "https://example.com/article")

    def test_source_is_read_only(self) -> None:
        """Test that the source property is read-only"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.source, "Example Source")
        with self.assertRaises(AttributeError):
            article.source = "New Source" # type: ignore

    def test_author_is_read_only(self) -> None:
        """Test that the author property is read-only"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.author, "John Doe")
        with self.assertRaises(AttributeError):
            article.author = "Jane Doe" # type: ignore

    def test_title_is_read_only(self) -> None:
        """Test that the title property is read-only"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.title, "Example Title")
        with self.assertRaises(AttributeError):
            article.title = "New Title" # type: ignore

    def test_description_is_read_only(self) -> None:
        """Test that the description property is read-only"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.description, "This is an example description.")
        with self.assertRaises(AttributeError):
            article.description = "New description." # type: ignore

    def test_published_at_is_read_only(self) -> None:
        """Test that the published_at property is read-only"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.published_at, "2023-10-01T12:00:00Z")
        with self.assertRaises(AttributeError):
            article.published_at = "2024-01-01T00:00:00Z" # type: ignore

    def test_content_is_read_only(self) -> None:
        """Test that the content property is read-only"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.content, "This is the content of the example article.")
        with self.assertRaises(AttributeError):
            article.content = "New content." # type: ignore

    def test_str(self) -> None:
        """Test the __str__ method"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        expected = "Example Title by John Doe from Example Source on 2023-10-01T12:00:00Z"
        self.assertEqual(str(article), expected)

    def test_repr(self) -> None:
        """Test the __repr__ method"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        expected = (
            "Article(title=Example Title, author=John Doe, "
            "source=Example Source, publishedAt=2023-10-01T12:00:00Z)"
        )
        self.assertEqual(repr(article), expected)

if __name__ == "__main__":
    unittest.main()