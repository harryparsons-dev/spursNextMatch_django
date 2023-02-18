import requests
from bs4 import BeautifulSoup
from datetime import datetime
# getting the date today
now = datetime.now().date()




fbref = requests.get('https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats#all_matchlogs')
soup2 = BeautifulSoup(fbref.text, 'html.parser')


# opp = soup2.findAll('td', {'data-stat': 'opponent'})
# venue = soup2.findAll('td', {'data-stat': 'venue'})
# # dates = soup2.findAll('th', {'data-stat': 'date'})
# fixtures = soup2.findAll('tbody', 'th', {'data-stat': 'date'})
# print(soup2.select_one('tbody', 'th', {'data-stat': 'date'}).decompose())
# print(fixtures)
table = soup2.findAll('tbody')


for tab in table:
    opp = tab.findAll('td', {'data-stat': 'opponent'})
    venue = tab.findAll('td', {'data-stat': 'venue'})

    fixtures = tab.findAll('th', {'data-stat': 'date'})
    for op,ven,fixture in zip(opp,venue,fixtures):


        teams = op.findAll('a')


        for team in teams:
            date_obj = datetime.strptime(fixture.text, '%Y-%m-%d').date()
            if(date_obj > now):
                if(ven.text == "Home"):
                    print(team.text + "/" + ven.text + "/" + fixture.text)

                else:
                     print(team.text + "/" + ven.text+ "/" + fixture.text)


