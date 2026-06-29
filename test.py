import asyncio
from src.main import FrankfurterAPI


async def main():
    print("Initializing Frankfurter API...")
    api = FrankfurterAPI()

    try:
        print("\nFetching currencies...")
        currencies = await api.get_currencies()
        usd_info = next((c for c in currencies if c.get("iso_code") == "USD"), None)
        print(
            f"Found {len(currencies)} currencies. (e.g. USD: {usd_info.get('name') if usd_info else 'Unknown'})"
        )

        base_currency = "USD"
        target_currency = "EUR"
        print(f"\nFetching exchange rate from {base_currency} to {target_currency}...")
        rate_data = await api.get_rate(base=base_currency, target=target_currency)

        print(f"Rate Data: {rate_data}")

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    asyncio.run(main())
