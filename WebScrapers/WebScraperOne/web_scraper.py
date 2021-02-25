"""
    [DESCRIPTION]: This is a webscraper in python 3.

    We are scraping all of the commands and descriptions off of a tutorials points
    website.
    
    The result of all of this will be pushed to a file, this file will be made
    in the local directory if it does not exist !

    This my first webscraper !
"""
__title__ = "Web Scraper"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

import requests
from bs4 import BeautifulSoup

class WebScraper:
    """
    Name        :   Webscraper
    Purpose     :   This class will hold methods relevent
                    to a webscraper.
    """

    def __init__(self, url):
        self.url = url

    def scrape_commands(self):
        webpage = requests.get(self.url)
        soup = BeautifulSoup(webpage.content, "html.parser")
        commands = soup.find_all("td")
        with open("output.txt", 'w') as outputFile:
            for os in commands:
                outputFile.writelines(os.text + "\n\n")

if __name__ == "__main__":
    
    _url = "https://www.tutorialspoint.com/batch_script/batch_script_commands.htm"
    scrape = WebScraper(_url)
    scrape.scrape_commands()
    
