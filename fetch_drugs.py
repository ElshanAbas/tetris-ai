import json
import sys
from urllib.request import urlopen, Request

API_URL = "https://api.fda.gov/drug/drugsfda.json?limit=100"


def fetch_drugs(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as resp:
        return json.load(resp)


def main():
    try:
        data = fetch_drugs(API_URL)
        results = data.get('results', [])
        for entry in results:
            app = entry.get('openfda', {})
            brand = app.get('brand_name', ['Unknown'])[0]
            manufacturer = app.get('manufacturer_name', ['Unknown'])[0]
            app_num = entry.get('application_number', 'N/A')
            print(f"{brand} - {manufacturer} (Application: {app_num})")
    except Exception as e:
        print("Failed to fetch data from open.fda.gov:", e, file=sys.stderr)
        print("Ensure network access is enabled and try again.")


if __name__ == '__main__':
    main()
