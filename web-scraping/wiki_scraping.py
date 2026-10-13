
import requests
from bs4 import BeautifulSoup
import time
import csv
from pathlib import Path

base_url = "https://minecraft.wiki"
category_url = base_url + "/w/Category:Items"

headers = {
    "User-Agent": "IS310StudentResearch/1.0 (educational project)"
}

# Get the category page
response = requests.get(category_url, headers=headers, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
content = soup.find(id="mw-content-text")

# Find the equipment table
equipment_table = None

for table in content.find_all("table"):
    if "Equipment" in table.get_text(" ", strip=True):
        equipment_table = table
        break

if equipment_table is None:
    raise ValueError("Equipment table not found.")

# Collect five unique item links
items = []
seen = set()

skip_names = {
    "Items", "Tools", "Weapons", "Equipment",
    "Wearable", "Player", "Animals", "Ammunition"
}

for link in equipment_table.find_all("a", href=True):
    name = link.get_text(strip=True)
    href = link["href"]

    if (
        href.startswith("/w/")
        and ":" not in href
        and name not in skip_names
        and name
        and href not in seen
    ):
        items.append((name, base_url + href))
        seen.add(href)

    if len(items) == 5:
        break

# Visit each article and collect its information
data = []

for name, url in items:
    time.sleep(2)

    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("h1")
        paragraph = soup.select_one(".mw-parser-output > p")

        item_name = title.get_text(strip=True) if title else name
        description = (
            paragraph.get_text(" ", strip=True)
            if paragraph else "Not found"
        )

        data.append({
            "item_name": item_name,
            "category": "Equipment",
            "description": description,
            "source_url": url
        })

        print("Collected:", item_name)
    else:
        print("Skipped:", name, "Status:", response.status_code)

# Save data to a CSV in the same folder as this script
output_file = Path(__file__).parent / "wiki_data.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "item_name",
            "category",
            "description",
            "source_url"
        ]
    )

    writer.writeheader()
    writer.writerows(data)

print("--------------------")
print("Saved", len(data), "items to wiki_data.csv")
