from bs4 import BeautifulSoup
import requests

base_url = "https://www.espncricinfo.com/live-cricket-score"

def get_soup(url):
    """ send get request to html web page and return soup"""
    # Set the user-agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_match_links(soup):
    match_json=[]
    match_links = {}

    # Find all match elements
    match_elements = soup.find("div", class_="ds-flex ds-flex-wrap")
    with open('new.html','w') as file:
        file.write(str(match_elements))


    
    matches_elem=match_elements.find_all("div",class_="ds-border-b ds-border-line ds-border-r ds-w-1/2")
    # print(matches_elem)
    teams=[]
    team2_list=[]
    for match in matches_elem:
        link = match.find("a")
        team1=match.find('p',class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate").text
        team2_elem=match.find_all('div',class_="ds-flex ds-items-center ds-min-w-0 ds-mr-1")
        for team in team2_elem:
            team2=team['title']
        if team1==team2:
            team2=match.find('div',class_="ds-flex ds-items-center ds-min-w-0 ds-mr-1")['title']


        title=f'{team1} vs {team2}'
        print(title)
        
 
        href = 'https://www.espncricinfo.com' + link['href']
        match_links[title] = href
        match_json.append(match_links)

    
    return match_links

print(extract_match_links(get_soup(base_url)))


def get_matchlink():
    soup = get_soup(base_url)
    matchlink_map = extract_match_links(soup)
    return matchlink_map

    
       



    



