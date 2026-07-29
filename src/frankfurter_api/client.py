from typing import Any, TypedDict

import aiohttp


class FrankfurterAPIError(Exception):
    """Raised when the Frankfurter API request fails."""


class CurrencyResponse(TypedDict):
    iso_code: str
    iso_numeric: str
    name: str
    symbol: str
    start_date: str
    end_date: str

class ExchangeRateResponse(TypedDict):
    date: str
    base: str
    quote: str
    rate: float


class FrankfurterAPI:
    """
    A simple wrapper for the Frankfurter Currency API.
    """

    BASE_URL = "https://api.frankfurter.dev/v2"

    def __init__(self, timeout: int = 10):
        self.timeout = aiohttp.ClientTimeout(total=timeout)

    async def get_currencies(self) -> list[CurrencyResponse]:
        """
        Fetches the list of available currencies.

        Returns:
            A list of dictionaries containing currency details.
        """
        url = f"{self.BASE_URL}/currencies"
        return await self._request(url)

    async def get_rate(self, base: str, target: str) -> ExchangeRateResponse:
        """
        Fetches the exchange rate between the base currency and the target currency.

        Args:
            base (str): The base currency code (e.g., 'USD').
            target (str): The target currency code (e.g., 'EUR').

        Returns:
            A dictionary containing the exchange rate data.
        """
        url = f"{self.BASE_URL}/rate/{base.upper()}/{target.upper()}"
        return await self._request(url)

    async def _request(self, url: str) -> Any:
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session, session.get(url) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as error:
            raise FrankfurterAPIError(f"HTTP Error {error.status}: {error.message}") from error
        except aiohttp.ClientError as error:
            raise FrankfurterAPIError(f"Request Error: {error}") from error
