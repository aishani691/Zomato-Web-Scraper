from bs4 import BeautifulSoup
import re

def parse_info_string(info_tag):
    info_string = info_tag.split("JSON.parse(")[-1].split(");")[0]
    info_string = re.sub(r"\\", "", info_string)

    info_string = info_string.split("SECTION_ENTITIES_DATA\":")[-1].split(",\"SECTION_MORE_COLLECTIONS")[0]
    info_string = info_string.rstrip(r"/]")
    return info_string


def get_longest_tag_index(data):
    data_len = [len(str(tag)) for tag in data]
    max_len = max(data_len)
    ind = data_len.index(max_len)

    return ind


def get_data_from_json(json):
    id = json['id']
    name = json['name']
    cuisine_str_ = []
    for i in json['subtitleData']['cuisines']:
        cuisine_str_.append(i['name'])
    cuisine = ", ".join(cuisine_str_)

    if 'newlyOpenedObj' in json['rating_new'] and json['rating_new']['newlyOpenedObj'] != None:
        delivery_rating = json['rating_new']['newlyOpenedObj']['text']
    elif 'ratings' in json['rating_new'] and 'rating' in json['rating_new']['ratings']['DELIVERY']:
        delivery_rating = json['rating_new']['ratings']['DELIVERY']['rating']

    if 'newlyOpenedObj' in json['rating_new'] and json['rating_new']['newlyOpenedObj'] != None:
        dining_rating = json['rating_new']['newlyOpenedObj']['text']
    elif 'ratings' in json['rating_new'] and 'rating' in json['rating_new']['ratings']['DINING']:
        dining_rating = json['rating_new']['ratings']['DINING']['rating']

    overall_rating = json['rating']['aggregate_rating']

    area = json['subtitleData']['locality']['text']

    if 'proOfferText' in json:
        offer = json['proOfferText']
    else:
        offer = "None"

    votes = json['rating']['votes']

    if 'featuredLabel' in json:
        featured = json['featuredLabel']
    else:
        featured = "NO"

    return id, name, cuisine, delivery_rating, dining_rating, overall_rating, area, offer, votes, featured

'''Sample JSON string :
{
   "id":19868137,
   "type":"restaurant",
   "name":"Backstreet Brewery",
   "url":"https://www.zomato.com/bangalore/backstreet-brewery-sarjapur-road-bangalore?zrp_bid=951523&zrp_pid=14&zrp_cid=923357",
   "imageUrl":"https://b.zmtcdn.com/data/pictures/7/19868137/f3bb4b048d5c09cf71c9d3e461b5f785.jpg",
   "subtitleData":{
      "cuisines":[
         {
            "deeplink":"zomato://search?deeplink_filters=WyJ7XCJjb250ZXh0XCI6XCJhbGxcIn0iLCJ7XCJjdWlzaW5lX2lkXCI6W1wiNTVcIl19Il0%3D",
            "url":"https://www.zomato.com/bangalore/restaurants/italian/",
            "name":"Italian"
         },
         {
            "deeplink":"zomato://search?deeplink_filters=WyJ7XCJjb250ZXh0XCI6XCJhbGxcIn0iLCJ7XCJjdWlzaW5lX2lkXCI6W1wiMjI3XCJdfSJd",
            "url":"https://www.zomato.com/bangalore/restaurants/bar-food/",
            "name":"Bar Food"
         },
         {
            "deeplink":"zomato://search?deeplink_filters=WyJ7XCJjb250ZXh0XCI6XCJhbGxcIn0iLCJ7XCJjdWlzaW5lX2lkXCI6W1wiODJcIl19Il0%3D",
            "url":"https://www.zomato.com/bangalore/restaurants/pizza/",
            "name":"Pizza"
         },
         {
            "deeplink":"zomato://search?deeplink_filters=WyJ7XCJjb250ZXh0XCI6XCJhbGxcIn0iLCJ7XCJjdWlzaW5lX2lkXCI6W1wiNTBcIl19Il0%3D",
            "url":"https://www.zomato.com/bangalore/restaurants/north-indian/",
            "name":"North Indian"
         }
      ],
      "locality":{
         "text":"Sarjapur Road, Bangalore",
         "url":"https://www.zomato.com/bangalore/sarjapur-road-restaurants"
      }
   },
   "proOfferText":"Pro - Get 20% off",
   "rating":{
      "has_fake_reviews":0,
      "aggregate_rating":"3.9",
      "rating_text":"3.9",
      "rating_subtitle":"Good",
      "rating_color":"9ACD32",
      "votes":"549",
      "subtext":"REVIEWS",
      "is_new":false
   },
   "rating_new":{
      "newlyOpenedObj":"None",
      "suspiciousReviewObj":"None",
      "ratings":{
         "DINING":{
            "rating_type":"DINING",
            "rating":"4.2",
            "reviewCount":"524",
            "reviewTextSmall":"524 Reviews",
            "subtext":"524 Dining Reviews",
            "color":"#1C1C1C",
            "ratingV2":"4.2",
            "subtitle":"DINING",
            "sideSubTitle":"Dining Reviews",
            "bgColorV2":{
               "type":"green",
               "tint":"700"
            }
         },
         "DELIVERY":{
            "rating_type":"DELIVERY",
            "rating":"3.6",
            "reviewCount":"25",
            "reviewTextSmall":"25 Reviews",
            "subtext":"25 Delivery Reviews",
            "color":"#E23744",
            "ratingV2":"3.6",
            "subtitle":"DELIVERY",
            "sideSubTitle":"Delivery Reviews",
            "bgColorV2":{
               "type":"green",
               "tint":"600"
            },
            "newOnDelivery":false
         }
      }
   },
   "isBookmarked":false,
   "featuredLabel":"Featured"
}'''