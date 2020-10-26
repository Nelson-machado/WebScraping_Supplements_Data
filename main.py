from bs4 import BeautifulSoup as soup
import requests
from datetime import datetime

# Open the connection and then download the web page.
my_url = requests.get("https://www.amazon.in/s?k=whey+protein+isolate&ref=nb_sb_noss")
page_html = my_url.text

# html parsing. 
page_soup = soup(page_html, "html.parser")

# All the products.
all_products = page_soup.findAll("div", {"class": "a-section a-spacing-medium"})

# Creating the file as of today's date.
filename = "protien_details"
today_date = str(datetime.today()).split(' ')[0]
extn = ".csv"
protien_details_today_date = filename + '_' + today_date + extn

fh = open(protien_details_today_date, "w")

headers = "Name, price, rating, image \n"
fh.write(headers)

# Extracting details of each product.
for product in all_products:
    prod_title = product.findAll("span", {"class": "a-size-medium a-color-base a-text-normal"})
    name = prod_title[0].text.replace(',','|')

    prod_price = product.findAll("span",  {"class": "a-offscreen"})
    price = prod_price[0].text.replace('₹', '')

    prod_rating = product.findAll("span", {"class": "a-icon-alt"})
    rating = prod_rating[0].text

    prod_image = product.findAll("img", {"class": "s-image"})
    image2 = prod_image[0]['src']

    print(name)
    print(price)
    print(rating)
    print(image2)

    fh.write(name + "," + price.replace(',', '') + "," + rating + "," + image2 + "\n")

fh.flush()
#fh.close()
print(f'\033[92m File ready: {protien_details_today_date} \033[0m')