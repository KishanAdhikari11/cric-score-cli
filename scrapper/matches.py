from bs4 import BeautifulSoup
import requests
class Match:
    def __init__(self) -> None:
        self.base_url = "https://www.espncricinfo.com/live-cricket-score"


    def get_soup(self,url):
        """ send get request to html web page and return soup"""
        # Set the user-agent header
        headers = {
            
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def extract_match_links(self,soup):
        match_info_json=[]

        # Find all match elements
        
        match_elements = soup.find("div", class_="ds-flex ds-flex-wrap")
        for match in match_elements:
            link = match.find("a")
            team1_elem=match.find('div',class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
            
            try:
                
                team1=team1_elem.find('p',class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate").text
            except AttributeError:
                team1_elem=match.find_all('div',class_="ds-flex ds-items-center ds-min-w-0 ds-mr-1")
                for team in team1_elem:
                    team1=team['title']
            team2_elem=match.find('div',class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1")
            
            
            try:
                team2=team2_elem.find('p',class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate").text
            except AttributeError:
                team2_elem=match.find_all('div',class_="ds-flex ds-items-center ds-min-w-0 ds-mr-1")
                for team in team2_elem:
                    team2=team['title']
                if team1==team2:
                    team2=match.find('div',class_="ds-flex ds-items-center ds-min-w-0 ds-mr-1")['title']  #for live
            status=match.find('span',class_="ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5").text
            tournament=match.find('div',class_="ds-text-tight-xs ds-truncate ds-text-typo-mid3").text
            
            if status=="RESULT":
                status="Finished"
            if status== 'Live' or status=='Drinks' or status=='Stumps':
                match_elem=match.find('div',class_='ds-relative')
                try:
                    team1_score=match_elem.find('strong',class_="ds-text-typo-mid3").text
                except AttributeError:
                    team1_score=None
                try:
                    team2_score=match_elem.find('strong',class_='').text
                except AttributeError:
                    team2_score=None
               
            try:
                result_elem=match.find('p',class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
                result=result_elem.find('span').text
            except AttributeError:
                if status=="Match delayed - wet outfield" or "Match delayed - rain":
                    result="Match delayed"
        
            # if status != "Finished":
            #     team1_score = "None"
            #     team2_score="None"
            else:
            
                try:
                    team1_score_elem = team1_elem.find("div", class_="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap")
                    team1_score = team1_score_elem.find('strong').text
                except AttributeError:
                    try:
                        team1_score_elem=match.find("div",class_="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap")
                        team1_score=team1_score_elem.find('strong').text
                    except AttributeError:
                        team1_score="None"
                                                
                try:
                    team2_score_elem = team2_elem.find("div", class_="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap")
                    team2_score = team2_score_elem.find('strong').text
                except AttributeError:
                    team2_score = match.find('div',class_="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap fadeIn")  # Set a default value or handle the case when the element is not found

            match_info = {
            "title": f'{team1} vs {team2}',
            "team1": team1,
            "team2": team2,
            "status": status,
            "tournament": tournament,
            "result": result,
            "team1_score": team1_score,
            "team2_score": team2_score,
            "link": 'https://www.espncricinfo.com' + link['href']
                }
            match_info_json.append(match_info)
        return match_info_json


    def get_matchlink(self):
        soup = self.get_soup(self.base_url)
        matchlink_map = self.extract_match_links(soup)
        return matchlink_map
    
