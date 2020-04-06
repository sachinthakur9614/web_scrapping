import requests
import csv
import re
import lxml.html
from bs4 import BeautifulSoup
f1  = open("Furniture_and_Accessories_new_delhi7.csv", 'w')


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
    csv_row.append(website) 
    csv_row.append(" ".join(address_city))
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




k =210
count = 0
for i in range(0,532):
    
    html = requests.get('https://www.houzz.in/professionals/searchDirectory?topicId=26728&query=Furniture+%26amp%3B+Accessories&location=Delhi%2C+India&distance=100&sort=4&p='+str(k))
    doc = lxml.html.fromstring(html.content)
    new_pro = doc.xpath('//span[@itemprop="name"]/text()')
    link = doc.xpath('//a[@itemprop="url"]/@href')
    check = doc.xpath('//span[@itemprop="name"]/text()')
    total = count
    k  = k + 15
    print(k)
    print(new_pro,link)
    for j in link:
        count = count + 1
        inside_link =requests.get(j)
        doc1 = lxml.html.fromstring(inside_link.content)
        title = doc1.xpath('//h1[@class="hz-profile-header__name"]/text()')
        mobile  =  doc1.xpath('//a[@class="hz-profile-header__contact-method hz-track-me"]/@href')
        website = doc1.xpath('//a[@data-compid="Profile_Website"]/@href')
        address = doc1.xpath('//div[@class="profile-meta__val"]/text()')
        address_city = doc1.xpath('//div[@class="hz-profile-header__location"]/text()')
        email = doc1.xpath('//div[@class="profile-meta__content text-s"]')
        category = doc1.xpath('//div[@class="profile-meta__content text-s"]')
        categ =  doc1.xpath('//span[@claas="profile-meta__block"]/@text')


        pin = doc1.xpath('//div[@class="profile-meta__val"]/text()')
        # for  p in pin:
        #     pin2 = p.xpath('//span/text()')
        #     print("this is pin2 ",pin2)
            
        print("this is",categ)
        for mail in email:
            catego =   mail.xpath('//span[@claas="profile-meta__block"]/text()')
            print("this is cat",catego)
            





        # print(title,mobile,website,address_city,email)
        write_row(title,mobile,website,address_city,email)
        print("count",i,k)
        










