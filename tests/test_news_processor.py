"""
Tests for the NewsProcessor class
"""
import unittest
import sys
sys.path.append(".")
from src.news_processor import NewsProcessor
from src.article import Article
class TestNewsProcessor(unittest.TestCase):
    """Example test case for the NewsProcessor class"""
    def setUp(self) -> None:
        self.processor = NewsProcessor()
        self.articles = [
            Article(
                url="http://example.com/1",
                source="Example Source",
                author="Author A",
                title="Breaking News: Python is awesome",
                description="An article about Python.",
                published_at="2023-10-01T10:00:00Z",
                content="Full content of the article."
            ),
            Article(
                url="http://example.com/2",
                source="Example Source",
                author="Author B",
                title="Latest Updates on JavaScript",
                description="An article about JavaScript.",
                published_at="2023-10-02T12:00:00Z",
                content="Full content of the article."
            ),
            Article(
                url="http://example.com/3",
                source="Another Source",
                author="Author C",
                title="Python vs JavaScript: A Comparison",
                description="Comparing Python and JavaScript.",
                published_at="2023-10-03T14:00:00Z",
                content="Full content of the article."
            )
        ]
    def test_to_df_no_sort_no_filter(self) -> None:
        """Test that to_df returns a DataFrame with the correct columns and number of
        rows when no sorting and no filtering is applied"""
        df = self.processor.to_df(self.articles)
        self.assertEqual(len(df), 3)
        self.assertListEqual(
            list(df.columns),
            ['url', 'source', 'author', 'title', 'description', 'published_at', 'content'])
    def test_to_df_filter(self) -> None:
        """Test that to_df correctly filters rows based on filter_func"""
        df = self.processor.to_df(
            self.articles,
            filter_func=lambda a: a.source == "Example Source"
        )
        self.assertEqual(len(df), 2)
        self.assertTrue(all(df["source"] == "Example Source"))
    def test_to_df_sort(self) -> None:
        """Test that to_df correctly sorts rows based on sort_by"""
        df = self.processor.to_df(
            self.articles,
            sort_by=lambda a: a.published_at
        )
        dates = list(df["published_at"])
        self.assertEqual(dates, sorted(dates))
    def test_to_df_sort_and_filter(self) -> None:
        """Test that to_df correctly applies both sort_by and filter_func"""
        df = self.processor.to_df(
            self.articles,
            sort_by=lambda a: a.published_at,
            filter_func=lambda a: "Python" in a.title
        )
        self.assertEqual(len(df), 2)
        dates = list(df["published_at"])
        self.assertEqual(dates, sorted(dates))
    def test_to_df_empty_list(self) -> None:
        """Test that to_df handles an empty list of articles"""
        df = self.processor.to_df([])
        self.assertEqual(len(df), 0)
        self.assertListEqual(
            list(df.columns),
            ['url', 'source', 'author', 'title', 'description', 'published_at', 'content'])
    def test_count_word_in_title_found(self) -> None:
        """Test that _count_word_in_title returns correct count when term is present"""
        count = self.processor._count_word_in_title(  # pylint: disable=protected-access
            "Python is awesome and Python is fun", "python")
        self.assertEqual(count, 2)
    def test_count_word_in_title_not_found(self) -> None:
        """Test that _count_word_in_title returns 0 when term is not present"""
        count = self.processor._count_word_in_title(  # pylint: disable=protected-access
            "Latest Updates on JavaScript", "python")
        self.assertEqual(count, 0)
    def test_count_word_in_title_case_insensitive(self) -> None:
        """Test that _count_word_in_title is case-insensitive"""
        count = self.processor._count_word_in_title(  # pylint: disable=protected-access
            "PYTHON is great", "python")
        self.assertEqual(count, 1)
if __name__ == "__main__":
    unittest.main()