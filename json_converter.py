import csv
import json
import random

# Set your CSV filename here
CSV_FILENAME = 'cleaned_medical_Mira_Road.csv'
OUTPUT_FILENAME = 'medical_mira_road.json'


# Helper function to generate keywords
def generate_keywords(title):
    base_keywords = ["clinic", "hospital", "doctor", "healthcare", "medical"]
    title_words = [word.lower() for word in title.replace('&', 'and').replace(',', '').split()]
    keywords = list(set(base_keywords + title_words))
    return json.dumps(keywords)

# Helper function to generate description
def generate_description(title, city, district):
    return (
        f"{title} offers trusted medical services in {city}, {district}. "
        "Providing quality care and expert treatment."
    )

# Read CSV and process rows
output = []
with open(CSV_FILENAME, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Format phone numbers as a JSON array, if present
        phone = row.get('Phone', '').strip()
        phone_json = json.dumps([phone]) if phone else "[]"

        # Random subcategoryId between 124 and 127
        subcategory_id = random.randint(136, 138)

        # Compose the address (add state if needed)
        address = row['Address']
        if 'Maharashtra' not in address:
            address = f"{address}, {row['District']}, Maharashtra {row['pincode']}"

        entry = {
            "title": row['Name'],
            "description": generate_description(row['Name'], row['City'], row['District']),
            "address": address,
            "city": row['City'],
            "district": row['District'],
            "pincode": row['pincode'],
            "lat": float(row['Latitude']),
            "lng": float(row['Longitude']),
            "priceFrom": 1000,
            "priceTo": 10000,
            "timings": "24/7",
            "phoneNumbersJson": phone_json,
            "keywordsJson": generate_keywords(row['Name']),
            "categoryId": 26,
            "subcategoryId": subcategory_id
        }
        output.append(entry)

# Output as JSON array
with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
    json.dump(output, jsonfile, indent=2, ensure_ascii=False)

print(f"✅ JSON data written to: {OUTPUT_FILENAME}")