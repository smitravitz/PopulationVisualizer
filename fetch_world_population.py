import requests
import json

def fetch_population_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = response.json()

    result = []
    for c in countries:
        try:
            result.append({
                "country": c["name"]["common"],
                "population": c.get("population", 0),
                "flag": c.get("flags", {}).get("svg", ""),
                "capital": c.get("capital", ["Unknown"])[0],
                "region": c.get("region", "Unknown")
            })
        except Exception:
            continue

    with open("population_data.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved {len(result)} countries to population_data.json")

if __name__ == "__main__":
    fetch_population_data()
