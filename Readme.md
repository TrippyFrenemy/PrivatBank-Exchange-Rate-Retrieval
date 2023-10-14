# PrivatBank Exchange Rate Retrieval

This Python script allows you to retrieve exchange rates for selected currencies from PrivatBank's API for a specified number of days (up to 10 days). You can also specify the currencies you're interested in, and if no currencies are specified, it defaults to EUR and USD.

## Prerequisites

Before running this script, make sure you have the following dependencies installed:

- Python 3.7 or higher
- aiohttp library

You can install aiohttp using pip:

```bash
pip install aiohttp
```

## Usage

To use this script, follow these steps:

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```bash
python exchange.py <days> [currencies]
```

Replace `<days>` with the number of days for which you want to retrieve exchange rates (up to 10 days). You can also provide an optional list of currencies separated by spaces (e.g., EUR USD GBP) that you're interested in. If no currencies are specified, the script defaults to EUR and USD.

For example, to retrieve exchange rates for the last 7 days for EUR and USD, you would run:

```bash
python exchange.py 7 EUR USD
```

To retrieve exchange rates for the last 5 days without specifying currencies (defaults to EUR and USD), you would run:

```bash
python exchange.py 5
```

4. The script will make API requests to PrivatBank and display the exchange rates for the specified currencies over the specified number of days.

## Important Notes

- You can retrieve exchange rates for up to 10 days only. If you specify more than 10 days, the script will display an error message.

- The exchange rate data is fetched from PrivatBank's API, and the accuracy and availability of the data depend on their service.

## Disclaimer

This script is for educational and informational purposes only. It is not intended for financial or investment decisions. Use the retrieved data responsibly and ensure its accuracy before making any financial transactions.
