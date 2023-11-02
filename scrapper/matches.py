from bs4 import BeautifulSoup
import requests

base_url = "https://www.cricbuzz.com/cricket-match/live-scores"

def get_soup(url):
    # Set the user-agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_match_links(soup):
    match_links = {}

    # Find all match elements
    match_elements = soup.find_all("div", class_="cb-col-100 cb-col cb-schdl")

    for match in match_elements:
        link = match.find("a")
        title = link['title']
        href = 'https://www.cricbuzz.com' + link['href']
        match_links[title] = href

    return match_links


def get_matchlink():
    soup = get_soup(base_url)
    matchlink_map = extract_match_links(soup)
    return matchlink_map

    
       



    



