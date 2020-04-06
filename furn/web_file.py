import requests
import csv
import re
import lxml.html
from bs4 import BeautifulSoup
TOTALPAGE =532



f1  = open("Furniture_and_Accessories_new_delhi.csv", 'w')
writer = csv.writer(f1)
writer.writerow([
"company name",
"mobile no",
"website link",
"state and city",
"email",
])

def write_row(title,mobile,website,address_city,email):
    csv_row = []
    csv_row.append(" ".join(title))
    csv_row.append(" ".join(mobile))
    csv_row.append(" ".join(website)) 
    csv_row.append(" ".join(address_city))
    csv_row.append(" ".join(email))
    writer.writerow(csv_row)

pages = int(TOTALPAGE/15)
k = 0
count = 0
for i in range(0,(pages+1)):
    
    html = requests.get('https://www.houzz.in/professionals/searchDirectory?topicId=26728&query=Furniture+%26amp%3B+Accessories&location=Delhi%2C+India&distance=100&sort=4&p='+str(k))
    doc = lxml.html.fromstring(html.content)
    new_pro = doc.xpath('//span[@itemprop="name"]/text()')
    link = doc.xpath('//a[@itemprop="url"]/@href')
    check = doc.xpath('//span[@itemprop="name"]/text()')
    total = count
    k  = k + 15

    for j in link:
        count = count + 1
        inside_link =requests.get(j)
        doc1 = lxml.html.fromstring(inside_link.content)
        title = doc1.xpath('//h1[@class="hz-profile-header__name"]/text()')
        mobile  =  doc1.xpath('//a[@class="hz-profile-header__contact-method hz-track-me"]/@href')
        website = doc1.xpath('//a[@data-compid="Profile_Website"]/@href')
        address = doc1.xpath('//div[@class="profile-meta__val"]/text()')
        address_city = doc1.xpath('//div[@class="hz-profile-header__location"]/text()')
        email = doc1.xpath('//div[@class="profile-meta__content text-s"]/text()')
        category = doc1.xpath('//div[@class="profile-meta__content text-s"]')
        print(title,mobile,website,address_city,email)
        write_row(title,mobile,website,address_city,email)
        print("count",i,k)
        










