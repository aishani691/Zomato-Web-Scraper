# Zomato-Web-Scraper

Scrapes data from top restuarants of different cities listed in Zomato, mainly:

1. 'ID'   : Unique ID of the restuarant
2. 'Name'  : Name of the restuarant
3. 'Cuisine' : Cuisines of food available
4. 'Delivery_rating'   : Ratings for delivery
5. 'Dining_rating'   : Ratings for dining
6. 'Overall_rating'   : Overall ratings
7. 'Area'  : Location
8. 'Offer'  : Zomato Pro offers available
9. 'Votes'  : Number of votes recieved
10. 'Featured'   : Featured on Zomato

# Steps to install :
1. Clone the repo
2. Create a virtual environment : python3 -m venv venv
3. Install requirements : pip3 install -r requirements.txt
4. Run scrape.py : python3 scrape.py
5. Results stored in out.csv

# References:
https://datascienceplus.com/zomato-web-scraping-with-beautifulsoup-in-python/
https://github.com/nikitperiwal/Zomato-Scraper

Thanks for reading! Also, any suggestion to improve this repo is extremely welcome :) 

# Further work:
- Build a more generic scraper
- Can we optimise the process using selenium
