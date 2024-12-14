import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Fetch the webpage
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
else:
    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant data (facts and stats)
    data = {}
    sections = soup.find_all('section')  # Modify based on the HTML structure

    for section in sections:
        # Example: Extract headings and associated content
        heading = section.find('h2')
        if heading:
            key = heading.get_text(strip=True)
            values = section.find_all('p')
            content = [value.get_text(strip=True) for value in values]
            data[key] = content

    # Save the extracted data to a JSON file
    output_file = 'bu_facts_stats.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data has been saved to {output_file}")
