import requests
import csv
import re
import lxml.html
from bs4 import BeautifulSoup
f1  = open("tile_stone_couuntertops2.csv", 'w')


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
    csv_row.append(title)
    csv_row.append(mobile)
    csv_row.append(website) 
    csv_row.append(address_city)
    csv_row.append(email)
    # csv_row.append(category)
    # try:
        
    # except:
    #     csv_row.append("")

    # try:
        
    # except:
    #     csv_row.append("")   

    # try:
        
    # except:
    #     csv_row.append("") 

    # try:
        
    # except:
    #     csv_row.append("")  
    # try:
        
    # except:
    #     csv_row.append("")  
    writer.writerow(csv_row)




k =45
count = 0
for i in range(0,890):
    
    html = requests.get('https://www.houzz.in/professionals/searchDirectory?topicId=26701&query=Tile%2C+Stone+%26amp%3B+Countertops&location=India&distance=50&sort=4&p='+str(k))
    doc = lxml.html.fromstring(html.content)
    new_pro = doc.xpath('//span[@itemprop="name"]/text()')
    link = doc.xpath('//a[@class="pro-card-carousel__slide"]/@href')
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
        # email = doc1.xpath('//div[@class="profile-meta__content text-s"]/text()')
        email = doc1.xpath('//span[@class="profile-meta__block"]/text()')
        category = doc1.xpath('//a/text()')


        print(title,mobile,website,address_city,email)
        write_row(title,mobile,website,address_city,email)
        










