import json
from bs4 import BeautifulSoup
import requests
import pandas as pd


states = ['alabama',
        'alaska',
        'arizona',
        'arkansas',
        'california',
        'colorado',
        'connecticut',
        'delaware',
        'florida',
        'georgia',
        'hawaii',
        'idaho',
        'illinois',
        'indiana',
        'iowa',
        'kansas',
        'kentucky',
        'louisiana',
        'maine',
        'maryland',
        'massachusetts',
        'michigan',
        'minnesota',
        'mississippi',
        'missouri',
        'montana',
        'nebraska',
        'nevada',
        'new-hampshire',
        'new-jersey',
        'new-mexico',
        'new-york',
        'north-carolina',
        'north-dakota',
        'ohio',
        'oklahoma',
        'oregon',
        'pennsylvania',
        'rhode-island',
        'south-carolina',
        'south-dakota',
        'tennessee',
        'texas',
        'utah',
        'vermont',
        'virginia',
        'washington',
        'west-virginia',
        'wisconsin',
        'wyoming',
        ]

urls = ['https://www.nytimes.com/interactive/2020/11/03/us/elections/results-alabama.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-alaska.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-arizona.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-arkansas.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-california.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-colorado.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-connecticut.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-delaware.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-florida.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-georgia.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-hawaii.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-idaho.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-illinois.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-indiana.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-iowa.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-kansas.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-kentucky.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-louisiana.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-maine.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-maryland.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-massachusetts.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-michigan.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-minnesota.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-mississippi.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-missouri.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-montana.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-nebraska.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-nevada.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-new-hampshire.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-new-jersey.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-new-mexico.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-new-york.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-north-carolina.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-north-dakota.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-ohio.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-oklahoma.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-oregon.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-pennsylvania.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-rhode-island.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-south-carolina.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-south-dakota.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-tennessee.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-texas.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-utah.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-vermont.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-virginia.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-washington.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-west-virginia.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-wisconsin.html',
        'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-wyoming.html',
        ]

for index, u in enumerate(urls):
    html_content = requests.get(u).text
    soup = BeautifulSoup(html_content, "lxml")
    results_table = soup.find("table", attrs={"class": "e-table e-county-table"})
    results_table_data = results_table.tbody.find_all("tr")

    county_names = []
    margin_2020 = []
    margin_2016 = []
    est_v_share = []
    total_vote = []
    abs_vote = []

    for i in results_table_data:
        # county_names = []
        for th in i.find_all("th"):
            # margin_2020 = []
            county_names.append(th.text.strip())
        for td in i.find_all("td", {"class": "e-cell e-margin"}):
        # remove any newlines and extra spaces from left and right
            margin_2020.append(td.text.strip())
        for td in i.find_all("td", {"class": "e-cell e-16-margin"}):
        # remove any newlines and extra spaces from left and right
            margin_2016.append(td.text.strip())
        for td in i.find_all("td", {"class": "e-cell e-est-v-share e-est-pct"}):
        # remove any newlines and extra spaces from left and right
            est_v_share.append(td.text.strip())
        for td in i.find_all("td", {"class": "e-cell e-total e-v"}):
        # remove any newlines and extra spaces from left and right
            total_vote.append(td.text.strip())
        for td in i.find_all("td", {"class": "e-cell e-abs-v e-v"}):
        # remove any newlines and extra spaces from left and right
            abs_vote.append(td.text.strip())

    df = pd.DataFrame(list(zip(county_names, margin_2020, 
                                margin_2016, est_v_share, 
                                total_vote, abs_vote)),
                        columns = ['county', '2020_margin', 
                                '2016_margin', 'estim_vote_share', 
                                'tot_vote_2020', 'abs_vote_2020'])

    df['state'] = states[index]
    df.to_csv(states[index] + '.csv')


