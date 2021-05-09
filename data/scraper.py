"""
Debate Results Scraper | Tabroom

@author: Ishan Bhatt

"""

from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
import numpy as np
from scipy import stats

def tournament_scrape(tourn, yr, link, win_type = "WinPm", point_type = "PtsPm -1HL", code = "Code", name = "Name"):
    file = rq.get(link)

    soup = BeautifulSoup(file.text, 'html.parser')

    data = []

    table = soup.find('table')
    rows = table.find_all('tr')
    header = table.find_all('thead')

    # Get title elements

    for item in header:
        title = item.find_all('th')
        title = [name.text.strip() for name in title]
        data.append(title)

    # Get data in each row

    for row in rows:
        cols = row.find_all('td')
        col = [element.text.strip() for element in cols]
        data.append(col)

    data = [item for item in data if item != []]

    tidy = pd.DataFrame(data)
    headers = [tidy.iloc[0]].pop(0).tolist()
    final = tidy[1:]
    final.columns = headers
    final = final[["Place", code, name, "State", win_type, point_type]]
    final["Tournament"] = tourn
    final["Season"] = yr
    final = final.rename(columns={point_type: 'Score'})
    final = final.rename(columns={win_type: 'Win'})
    final["Score"] = final["Score"].astype(float)
    final["Z"] = stats.zscore(final["Score"])

    return final
