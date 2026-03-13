"""
Module to interact with the News API and retrieve news articles.
"""
from typing import Optional, Any
import requests
from src.article import Article

class SearchNews:
    """
    Class to interact with the News API and retrieve news articles.
    """

    def __init__(self, api_key_file: str):
        """
        Initialize SearchNews by reading API key from file.
        Args:
            api_key_file (str): Path to file containing the API key
        Raises:
            FileNotFoundError: If the API key file does not exist
        """
        with open(api_key_file, 'r', encoding='utf-8') as f:
            self.__api_key = f.read().strip()

    def get_top_headlines(self, *terms: str) -> list[Article]:
        """
        Get top headlines from the News API.
        Args:
            *terms (str): Variable number of search terms
        Returns:
            list[Article]: List of Article objects
        Raises:
            requests.exceptions.RequestException: If the API request fails
            KeyError: If expected keys are missing in the API response data
        """
        raw_params: dict[str, Optional[str]] = {
            "apiKey": self.__api_key,
            "q": " ".join(terms) if terms else None,
            "country": "us",
        }
        params: dict[str, str] = {k: v for k, v in raw_params.items() if v is not None}
        response_data = self._make_request("top-headlines", params)
        return self._create_articles_from_response(response_data)

    def get_everything(
        self,
        *terms: str,
        date: Optional[str] = None,
        domains: Optional[list[str]] = None,
        language: Optional[str] = None
    ) -> list[Article]:
        """
        Get everything from the News API.
        Args:
            *terms (str): Variable number of search terms
            date (Optional[str]): Optional date filter (YYYY-MM-DD format)
            domains (Optional[list[str]]): Optional domain filter (e.g., 'bbc.co.uk')
            language (Optional[str]): Optional language filter (e.g., 'en')
        Returns:
            list[Article]: List of Article objects
        Raises:
            requests.exceptions.RequestException: If the API request fails
            KeyError: If expected keys are missing in the API response data
        """
        raw_params: dict[str, Optional[str]] = {
            "apiKey": self.__api_key,
            "q": " ".join(terms) if terms else None,
            "from": date,
            "domains": ",".join(domains) if domains else None,
            "language": language,
        }
        params: dict[str, str] = {k: v for k, v in raw_params.items() if v is not None}
        response_data = self._make_request("everything", params)
        return self._create_articles_from_response(response_data)

    def _make_request(self, endpoint: str, params: dict[str, str]) -> Any:
        """
        Helper method to make API requests.
        Args:
            endpoint (str): API endpoint (e.g., 'top-headlines')
            params (dict[str, str]): Query parameters for the request
        Returns:
            dict[str, Any]: Dictionary of JSON response
        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        url = f"https://newsapi.org/v2/{endpoint}"
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def _create_articles_from_response(self, response_data: dict[str, Any]) -> list[Article]:
        """
        Helper method to create Article objects from API response.
        Args:
            response_data (dict[str, Any]): JSON response from API
        Returns:
            list[Article]: List of Article objects
        Raises:
            KeyError: If expected keys are missing in the response data
        """
        articles = []
        for item in response_data["articles"]:
            article = Article(
                url=item.get("url"),
                source=item.get("source", {}).get("name"),
                author=item.get("author"),
                title=item.get("title"),
                description=item.get("description"),
                published_at=item.get("publishedAt"),
                content=item.get("content"),
            )
            articles.append(article)
        return articles