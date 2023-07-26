import requests
from bs4 import BeautifulSoup
import pymysql
db = pymysql.connect(host='localhost', user='zaarahirani', password='zh10', db='your_database_name')
cursor = db.cursor()
url = "https://ww.oyoroons.com/hotels-in-mumbai/"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content,'html.parser')
hotel_names = soup.find_all('h3', class_='listingHotelDescription_hotelName')
hotel_prices = soup.find_all('span', class_='listingPrice_finalPrice')
for i in range(len(hotel_names)):
   name = hotel_names[i].text.strip()
   price = hotel_prices[i].text.strip().replace("Rs.", "").replace(",", "")
   sql = "INSERT INTO hotels(name, price) VALUES(%s, %s)"
   values = (name, price)
   cursor.executed(sql, values)
   db.commit()
db.close()
