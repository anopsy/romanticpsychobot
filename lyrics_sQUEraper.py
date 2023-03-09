import requests
import csv
from bs4 import BeautifulSoup

# initialize a list to store all visited links
visited_links = []
lyrics = []


def scrape(site):

    page_to_scrape = requests.get(site).text
    soup = BeautifulSoup(page_to_scrape, "lxml")
    links = soup.find_all('a')

# get all links
    for link in links:
        href = link.get('href')
        #TODO: ten bool niepotrzebny chyba
        if bool(href) and href.startswith("/quebonafide"):
            if href not in visited_links:
                href= "https://teksciory.interia.pl" + href
                visited_links.append(href)
                

def get_lyrics(visited_links):
    link_set= set(visited_links)
    for link in link_set:
        page_content = requests.get(link).text

        # parse the html content

        page_soup = BeautifulSoup(page_content, "lxml")

        # find all meta tags with the given itemprop attributes
        text_lyrics = page_soup.find_all('div', attrs={'class': 'lyrics--text'})


        # extract the latitude and longitude strings
        if bool(text_lyrics):
           lyrics.append(text_lyrics)
   

            
if __name__ =="__main__":
    site = "https://teksciory.interia.pl/quebonafide,a,36609.html"
    scrape(site)
    get_lyrics(visited_links)
    with open('romanticpsycho.csv', 'w') as f:
        writer =csv.writer(f)
        writer.writerows(lyrics)
