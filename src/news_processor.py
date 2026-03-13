"""
Module for processing and visualizing news articles data.
"""
from typing import Callable, Optional, Any
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from src.article import Article

class NewsProcessor:
    """
    Class to process and visualize news articles data.
    """

    def to_df(self, articles: list[Article],
              sort_by: Optional[Callable[[Article], Any]] = None,
              filter_func: Optional[Callable[[Article], bool]] = None
    ) -> pd.DataFrame:
        """
        Convert list of Article objects to a Pandas DataFrame.
        Args:
            articles (list[Article]): List of Article objects
            sort_by (Optional[Callable[[Article], Any]]): Optional function to sort rows by
            filter_func (Optional[Callable[[Article], bool]]): Optional function to filter rows
                    (include rows where function returns True)
        Returns:
            pd.DataFrame: Pandas DataFrame with articles data
        """
        if filter_func is not None:
            articles = [a for a in articles if filter_func(a)]

        if sort_by is not None:
            articles = sorted(articles, key=sort_by)

        data = [
            {
                "url": a.url,
                "source": a.source,
                "author": a.author,
                "title": a.title,
                "description": a.description,
                "published_at": a.published_at,
                "content": a.content,
            }
            for a in articles
        ]
        columns = ['url', 'source', 'author', 'title', 'description', 'published_at', 'content']
        return pd.DataFrame(data, columns=columns)

    def plot_word_popularity(self, articles: list[Article], search_term: str) -> None:
        """
        Plot the frequency of a search term in article titles over time.
        Args:
            articles (list[Article]): List of Article objects
            search_term (str): The term to search for in titles
        """
        date_counts: dict[datetime.date, int] = {}
        for article in articles:
            date = self._extract_date_from_published_at(article.published_at)
            if date is None:
                continue
            count = self._count_word_in_title(article.title or "", search_term)
            date_counts[date] = date_counts.get(date, 0) + count

        sorted_dates = sorted(date_counts.keys())
        counts = [date_counts[d] for d in sorted_dates]
        date_strings = [str(d) for d in sorted_dates]

        plt.figure(figsize=(10, 5))
        plt.plot(date_strings, counts, marker="o")
        plt.title(f'Popularity of "{search_term}" in Article Titles Over Time')
        plt.xlabel("Date")
        plt.ylabel(f'Number of Articles Containing "{search_term}"')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def _extract_date_from_published_at(
            self, published_at: Optional[str]) -> Optional[datetime.date]:
        """
        Helper method to extract date from publishedAt timestamp.
        Args:
            published_at (Optional[str]): ISO format timestamp string
                    (e.g., '2023-10-01T12:34:56Z')
        Returns:
            Optional[datetime.date]: Date object or None if input is None
        """
        if not published_at:
            return None
        return datetime.datetime.fromisoformat(published_at.replace('Z', '+00:00')).date()

    def _count_word_in_title(self, title: str, search_term: str) -> int:
        """
        Helper method to count occurrences of search term in title.
        Args:
            title (str): Article title
            search_term (str): Term to search for
        Returns:
            int: Number of occurrences (case-insensitive)
        """
        return title.lower().count(search_term.lower())