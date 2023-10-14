import argparse
import aiohttp
import asyncio

API_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"

async def fetch_exchange_rate(date):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL.format(date=date)) as response:
            return await response.json()

async def get_exchange_rates(days, currencies):
    rates = []
    today = datetime.date.today()

    for i in range(days):
        date = today - datetime.timedelta(days=i)
        exchange_rate_data = await fetch_exchange_rate(date.strftime("%d.%m.%Y"))

        exchange_rates = exchange_rate_data.get("exchangeRate", [])
        date_rates = {date.strftime("%d.%m.%Y"): {}}

        for rate in exchange_rates:
            currency = rate.get("currency")
            if not currencies or currency in currencies:
                date_rates[date.strftime("%d.%m.%Y")][currency] = {
                    "sale": rate.get("saleRate", 0.0),
                    "purchase": rate.get("purchaseRate", 0.0),
                }

        rates.append(date_rates)

    return rates

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get exchange rates for selected currencies from PrivatBank.")
    parser.add_argument("days", type=int, help="Number of days to retrieve exchange rates for (up to 10 days).")
    parser.add_argument("currencies", nargs="*", help="Currencies to retrieve exchange rates for (e.g., EUR USD GBP).")

    args = parser.parse_args()

    if args.days > 10:
        print("Error: You can retrieve exchange rates for up to 10 days only.")
    else:
        import datetime

        async def main():
            if not args.currencies:
                args.currencies = ["EUR", "USD"]
            exchange_rates = await get_exchange_rates(args.days, args.currencies)
            print(exchange_rates)

        asyncio.run(main())
