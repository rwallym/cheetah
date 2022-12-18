import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://en.wikipedia.org/wiki/Nikola_Tesla"
page = requests.get(url)

# Parse the HTML of the webpage
soup = BeautifulSoup(page.text, "html.parser")

# Find the data you want to scrape
data = soup.find_all("p")

# Write the data to a local file
with open("data.txt", "w") as file:
    for item in data:
        file.write(str(item))