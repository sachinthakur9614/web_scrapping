import requests
import csv
import re
import lxml.html
GLOBAL_LINK ='https://www.homify.in'
TOTAL_PAGE = 15186

f1  = open("homefy_in.csv", 'w')
writer = csv.writer(f1)
writer.writerow([
"Company name",
"Category",
"Mobile no",
"Website link",
"State and City",
"Email",
"Address"
])

def write_row(title,category,mobile,website,address,city_state):
    csv_row = []
    csv_row.append(" ".join(title))
    csv_row.append(" ".join(category))
    csv_row.append(" ".join(mobile))
    csv_row.append(" ".join(website)) 
    csv_row.append(" ".join(city_state))
    csv_row.append(" ")
    csv_row.append(" ".join(address))
    writer.writerow(csv_row)


pages = int(TOTAL_PAGE/20)
k = 1
count = 0


for i in range(0,(pages+1)):
    html = requests.get('https://www.homify.in/professionals/interior-architects?page='+str(k))
    doc = lxml.html.fromstring(html.content)
    link = doc.xpath('//a[@class="-flex- -flex-1- professionals--item-picture--holder"]/@href')
    k= k +1
    for i in link:
        inside_link =requests.get(GLOBAL_LINK+i)
        doc1 = lxml.html.fromstring(inside_link.content)
        title = doc1.xpath('//div[@class="user-header--public-name"]/text()')
        category = doc1.xpath('//a[@class="category-city--category"]/text()')
        mobile  =  doc1.xpath('//a[@class="button -outlined js-call-button -up-to-xs-"]/@href')
        address = doc1.xpath('//dd[@class="key-value--value"]/text()')
        city_state = doc1.xpath('//a[@class="category-city--city -themed-"]/text()')
        website = doc1.xpath('//a[@class="external-link"]/text()')
        write_row(title,category,mobile,website,address,city_state)
        print(title,category,mobile,website,address,city_state)

        
        
