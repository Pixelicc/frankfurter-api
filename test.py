import pytest
from src.main import FrankfurterAPI


@pytest.fixture
def api():
    """Fixture to initialize the FrankfurterAPI."""
    return FrankfurterAPI()


@pytest.mark.asyncio
async def test_get_currencies(api):
    """Test fetching currencies."""
    currencies = await api.get_currencies()

    assert isinstance(currencies, list)
    assert len(currencies) > 0

    usd_info = next((c for c in currencies if c.get("iso_code") == "USD"), None)
    assert usd_info is not None
    assert usd_info.get("name") == "United States Dollar"


@pytest.mark.asyncio
async def test_get_rate(api):
    """Test fetching the exchange rate between USD and EUR."""
    rate_data = await api.get_rate(base="USD", target="EUR")

    assert isinstance(rate_data, dict)
    assert rate_data.get("base") == "USD"
    assert rate_data.get("quote") == "EUR"
    assert "rate" in rate_data
    assert isinstance(rate_data.get("rate"), (int, float))
