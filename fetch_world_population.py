import requests
from bs4 import BeautifulSoup
import json

URLS = {
    'Asia': 'https://www.worldometers.info/population/countries-in-asia-by-population/',
    'Africa': 'https://www.worldometers.info/population/countries-in-africa-by-population/',
    'Europe': 'https://www.worldometers.info/population/countries-in-europe-by-population/',
    'North America': 'https://www.worldometers.info/population/countries-in-northern-america-by-population/',
    'South America': 'https://www.worldometers.info/population/countries-in-latin-america-and-the-caribbean-by-population/',
    'Oceania': 'https://www.worldometers.info/population/countries-in-oceania-by-population/'
}

def fetch_table(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table')
    rows = table.tbody.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2:
            country = cols[1].text.strip()
            population = int(cols[2].text.strip().replace(',', ''))
            data.append((country, population))
    return data

def build_population_data():
    master = []
    for continent, url in URLS.items():
        for country, pop in fetch_table(url):
            master.append({
                'country': country,
                'population': pop,
                'continent': continent
            })
    return master

if __name__ == '__main__':
    data = build_population_data()
    with open('population_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} entries to population_data.json")
