# parsers.py
from abc import ABC, abstractmethod
import pandas as pd
from bs4 import BeautifulSoup

class Parser(ABC):
    """ABC Protocol class for parsing data from Transfermarkt."""
    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        pass

class PlayerNames(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        elements = soup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
        names = [td.get("title") if td.get("title") else None for td in elements]
        return pd.DataFrame(names, columns=["name"])

class PlayerAges(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        age_cells = soup.select('table.items tbody tr td:nth-of-type(3)')
        ages = [self._parse_age(td.text) for td in age_cells]
        return pd.DataFrame(ages, columns=["age"])
    
    def _parse_age(self, text):
        if not text:
            return None
        try:
            return int(text.strip().split("(")[1].split(")")[0])
        except (IndexError, ValueError):
            return None

class PlayerCountries(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        countries_td = [stat for stat in soup.find_all("td", {"class": "zentriert"}) if 'flaggenrahmen' in str(stat)]
        countries = [", ".join([img.get('title') for img in td.find_all('img')]) if td else None for td in countries_td]
        return pd.DataFrame(countries, columns=["country"])

class PlayerValues(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        values = soup.find_all("td", {"class": "rechts hauptlink"})
        values = [td.find('a').text if td.find('a') else '€0' for td in values]
        return pd.DataFrame(values, columns=["value"])

class PlayerPositions(Parser):
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        pos_soup = soup.find_all("td", {"class": "posrela"})
        positions = [td.find_all("tr")[1].find("td").text.strip() if td.find_all("tr") else None for td in pos_soup]
        return pd.DataFrame(positions, columns=["position"])