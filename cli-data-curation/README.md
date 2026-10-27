# Cultural Media Collection

## Project Description

This project collects information about films from different countries and cultures. Users can record a film's title, country, release year, genre, and cultural notes.

I created two versions of the application: a Python command-line interface (CLI) and an HTML webpage.

## Python CLI

The Python version uses the Rich library to display film information in formatted tables. Users can enter a film, review their information, and confirm whether they want to save it.

Confirmed entries are saved to `cultural_media.json`. Previously saved records are loaded when the program runs again.

### How to Run

1. Create a virtual environment: `python3 -m venv .venv`
2. Activate it on Mac/Linux: `source .venv/bin/activate`
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run the program: `python cli_data_entry.py`

## HTML Interface

The HTML version collects the same information through a webpage. Users can review and confirm entries, see saved films in a table, and download their data as a JSON file.

To use it, open `index.html` in a web browser.

The webpage uses browser local storage, so its saved records are separate from the Python CLI's JSON file.

## Data Fields

- Film title
- Country
- Release year
- Genre
- Cultural notes

## Files

- `cli_data_entry.py`: Python CLI application
- `index.html`: HTML data collection interface
- `cultural_media.json`: Sample data collected using Python
- `requirements.txt`: Python dependencies
- `ai-chat-log.md`: Documentation of AI assistance

## AI Assistance

I used ChatGPT to help with setting up my Python virtual environment, writing and understanding the code, and testing both versions of the application. The process is documented in `ai-chat-log.md`.