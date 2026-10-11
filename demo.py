import csv
import os

FILE_NAME = "points_50_usgs_temoins.csv"


def main():
    print("=" * 45)
    print("TERRASAFE HAITI")
    print("AI-Powered Landslide Risk Research")
    print("=" * 45)

    if not os.path.exists(FILE_NAME):
        print("\nDataset not found:", FILE_NAME)
        print("Please add the study CSV file.")
        print("No predictions have been generated.")
        return

    with open(FILE_NAME, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames or []
        rows = list(reader)

    print("\nNumber of study points:", len(rows))
    print("Available columns:", ", ".join(columns))

    if rows:
        print("\nDataset loaded successfully.")
        print("Next step: validate coordinates and labels.")
    else:
        print("\nThe dataset is empty.")

    print("\nThis is a research prototype.")
    print("No validated AI predictions are available yet.")


if __name__ == "__main__":
    main()
