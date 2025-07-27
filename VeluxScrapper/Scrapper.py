import requests
from bs4 import BeautifulSoup

# List of websites to check
websites = [
    "https://www.veluxblindsdirect.co.uk/",
    # Add more websites here
]

def extract_links(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags and extract the href attribute
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

def check_for_string(url, search_string):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Search for the specified string in the HTML content
        if search_string in soup.prettify():
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return False

# Search string
search_string = "velux.23video.com"

# Dictionary to store results
results = {}

# Extract links and check each link for the search string
for website in websites:
    print(f"Processing website: {website}")
    links = extract_links(website)
    found_links = []
    for link in links:
        # Normalize the link
        if not link.startswith('http'):
            if link.startswith('/'):
                link = website + link
            else:
                link = website + '/' + link

        if check_for_string(link, search_string):
            found_links.append(link)
    
    results[website] = found_links

# Output the results
for website, found_links in results.items():
    if found_links:
        print(f"Found '{search_string}' in the following links for {website}:")
        for link in found_links:
            print(link)
    else:
        print(f"No occurrences of '{search_string}' found in any links for {website}.")