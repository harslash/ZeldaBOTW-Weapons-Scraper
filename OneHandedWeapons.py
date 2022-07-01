'''
Web scraping for one-handed weapons Zelda BOTW - this scrapes a table from the website.
Packages imported: beautifulsoup4 lxml requests pandas openpyxl

Author: Harlean 
'''

from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    table1 = soup.find('table', class_='a-table a-table a-table tablesorter')

    # obtain every title of columns with tag <th>
    headers = []
    for header in table1.find_all('th'):
        title = header.text
        headers.append(title)

    # create a data frame
    mydata = pd.DataFrame(columns = headers)

    # for loop to fill mydata - each row under <tr> tag, data in <td> tag
    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

    # export data
    mydata.to_excel("zelda-weapons.xlsx")

get_data('https://game8.co/games/LoZ-BotW/archives/292478')
