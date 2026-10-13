# Minecraft Wiki Web Scraping Project

## Research Question

How are different Minecraft equipment items described, and what purposes do they serve in the game?

## Wiki Selection

I chose the [Minecraft Wiki](https://minecraft.wiki/) because it is a community-maintained resource containing information about Minecraft items, blocks, mechanics, and gameplay. I was interested in exploring how the wiki documents different items and their functions.

## Scraping Permissions

Before scraping, I reviewed the wiki's [robots.txt](https://minecraft.wiki/robots.txt) file. The general rules restrict certain pages and technical endpoints, including API paths and special wiki pages. The category and item article URLs used in this project were not explicitly disallowed under the general rules.

I limited the scraper to a small number of public pages, avoided restricted paths, and added a two-second delay between article requests to reduce the load on the website.

## Data Collection Process

I used Python with the `requests` and `BeautifulSoup` libraries to collect information from the Minecraft Wiki.

First, the scraper accessed the Category:Items page and located the table containing equipment links. It extracted five unique item links and then visited each item's individual article.

For each item, I collected:

- Item name
- Broad category
- Introductory description
- Source URL

I saved the results in `wiki_data.csv`.

## Dataset

The dataset contains five Minecraft equipment items: Axe, Brush, Fishing Rod, Carrot on a Stick, and Warped Fungus on a Stick.

The `category` field is assigned as "Equipment" based on the navigation table used to select the items. It is not an independently extracted category from each article.

## Limitations

The dataset is small and only represents five equipment items, so it cannot be used to compare all Minecraft item categories.

The scraper collects the introductory paragraph rather than detailed item properties such as durability, rarity, or stack size. Some descriptions also contain formatting artifacts from the wiki, including extra spaces and edition-specific notes.

Because the Minecraft Wiki can be edited, the information may change over time. The scraper also depends on the wiki's current HTML structure, so changes to the website could affect how it works.

## Files

- `wiki_scraping.py` — Python script used to collect the data.
- `wiki_data.csv` — CSV dataset containing the five scraped items.
- `README.md` — Documentation of the project.