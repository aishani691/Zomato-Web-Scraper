import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from helper import parse_info_string, get_longest_tag_index, get_data_from_json
import time

start = time.time()

# Make a GET HTTP request to server
# access denied while scraping : https://stackoverflow.com/questions/44865673/access-denied-while-scraping
urls = ['https://www.zomato.com/bangalore/top-restaurants', 'https://www.zomato.com/kolkata/top-restaurants', 'https://www.zomato.com/ncr/top-restaurants', \
        'https://www.zomato.com/hyderabad/top-restaurants', 'https://www.zomato.com/bhubaneswar/top-restaurants', 'https://www.zomato.com/manali/top-restaurants', \
        'https://www.zomato.com/mumbai/top-restaurants', 'https://www.zomato.com/kochi/top-restaurants', 'https://www.zomato.com/chennai/top-restaurants', \
        'https://www.zomato.com/lucknow/top-restaurants', 'https://www.zomato.com/jaipur/top-restaurants', 'https://www.zomato.com/kanpur/top-restaurants', \
        'https://www.zomato.com/ahmedabad/top-restaurants', 'https://www.zomato.com/pune/top-restaurants', 'https://www.zomato.com/surat/top-restaurants', \
        'https://www.zomato.com/chandigarh/top-restaurants', 'https://www.zomato.com/visakhapatnam/top-restaurants']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh;'
                         ' Intel Mac OS X 10_15_4)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/83.0.4103.97 Safari/537.36'}

info_string_list = []

for url in urls:
    res = requests.get(url, headers=headers)

    # Get the parsed HTML from the response string res.text in soup variable
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.find_all('script')

    # Data we need is stored in the longest script tag string
    ind = get_longest_tag_index(data)
    info_tag = str(data[ind])
    info_tag.encode(encoding = 'UTF-8')

    # Parsed string # Specific to zomato
    info_string = parse_info_string(info_tag)
    info_string_list.extend(info_string.split(r'id":'))

df = pd.DataFrame( columns=['ID', 'Name', 'Cuisine', 'Delivery_rating', 'Dining_rating', 'Overall_rating', 'Area', 'Offer', 'Votes', 'Featured'])

for i, tag in enumerate(info_string_list):
    try:
        tag = tag.rstrip('"').rstrip('{').rstrip(",") # Remove trailing ,{"
        tag = '{"id":'+tag # Create completed jsons

        if "{" in tag and "}" in tag:
            json_tag = json.loads(tag)
            id, name, cuisine, delivery_rating, dining_rating, overall_rating, area, offer, votes, featured = get_data_from_json(json_tag)
            df = df.append({'ID':id, 'Name':name, 'Cuisine':cuisine, 'Delivery_rating':delivery_rating, 'Dining_rating':dining_rating, 'Overall_rating': overall_rating, 'Area':area, 'Offer':offer,  'Votes':votes, 'Featured':featured}, ignore_index = True)
    except:
        pass
    print(i, tag, "\n")

df.to_csv("out.csv",index=False)
print(time.time()- start, "s taken!")