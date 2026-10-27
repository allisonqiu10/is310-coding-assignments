
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

# Save the data in the same folder as this script
DATA_FILE = Path(__file__).parent / "cultural_media.json"


def load_data():
    """Load previously saved media records."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_data(records):
    """Save all records to a JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False)


def show_table(records):
    """Display cultural media records in a table."""
    table = Table(title="Cultural Media Collection")

    table.add_column("Title")
    table.add_column("Country")
    table.add_column("Year")
    table.add_column("Genre")
    table.add_column("Notes")

    for record in records:
        table.add_row(
            record["title"],
            record["country"],
            record["year"],
            record["genre"],
            record["notes"]
        )

    console.print(table)


def get_input(prompt):
    """Ask for a value until the user enters something."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def main():
    console.print("[bold cyan]Cultural Media Collection[/bold cyan]")
    print("Document films from different countries and cultures.\n")

    records = load_data()

    if records:
        print("Previously saved records:")
        show_table(records)

    while True:
        print("\nEnter a film:")
        new_record = {
            "title": get_input("Film title: "),
            "country": get_input("Country: "),
            "year": get_input("Release year: "),
            "genre": get_input("Genre: "),
            "notes": get_input("Cultural notes: ")
        }

        print("\nReview your entry:")
        show_table([new_record])

        confirm = input("Save this entry? (y/n): ").strip().lower()

        if confirm == "y":
            records.append(new_record)
            save_data(records)
            print("Entry saved successfully!")
        else:
            print("Entry not saved.")

        again = input("Add another film? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"\nYour data is saved in: {DATA_FILE}")


if __name__ == "__main__":
    main()
