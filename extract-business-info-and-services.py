from bs4 import BeautifulSoup
import os
import re
import json
import csv
def clean_dir(directory):

    os.chdir(directory)

    for filename in os.listdir(directory):
        print(filename)
        clean_file(filename)

def clean_file(filename):

    with open(filename, 'r') as fhandle:
        row1 = {}
        line = ' '
        row1['Business Name'] = 'NA'
        row1['Business Phone'] = 'NA'
        row1['Business Website'] = 'NA'
        row1['Business Address'] = 'NA'
        row1['Business Name'] = 'NA'
        row1['Opening Hours'] = 'NA'
        row1['Takes Reservations'] = 'NA'
        row1['Delivery'] = 'NA' 
        row1['Take-out'] = 'NA' 
        row1['Aceepts-Credit-Cards'] = 'NA'
        row1['Accepts-Apple-Pay'] = 'NA' 
        row1['Accepts-Android-Pay'] = 'NA' 
        row1['Accepts-Bitcoin'] = 'NA' 
        row1['Good-For'] = 'NA' 
        row1['Parking'] = 'NA' 
        row1['Bike-Parking'] = 'NA'
        row1['Good-For-Kids'] = 'NA' 
        row1['Good-For-Groups'] = 'NA'
        row1['Attire'] = 'NA' 
        row1['Ambience'] = 'NA'
        row1['Noise-Level'] = 'NA' 
        row1['Alcohol'] = 'NA'
        row1['Outdoor-Seating'] = 'NA' 
        row1['Wi-Fi'] = 'NA' 
        row1['Caters'] = 'NA' 
        row1['Gender-Neutral-Restrooms'] = 'NA' 




        text = BeautifulSoup(fhandle,'html.parser')

        
        try:
            binfo = text.find('h1',class_='biz-page-title')
            row1['Business Name'] = binfo.text.strip().encode('utf-8')
        except:
            row1['Business Name'] = 'NA'
        
        
        try:
            bphone = text.find('span',class_='biz-phone')
            row1['Business Phone'] = bphone.text.strip().encode('utf-8')
        except:
            row1['Business Phone'] = 'NA'
        
        try:
            bweb = text.find('span',class_='biz-website')
            bweb1 = bweb.find("a")
            row1['Business Website'] = bweb1.text.strip().encode('utf-8')
        except:
            row1['Business Website'] = 'NA'
            
        
        try:
            badd = text.find('div',class_='map-box-address')
            badd1 = re.sub('  +', '', badd.text.strip())
            row1['Business Address'] = badd1.encode('utf-8')
        except:
            row1['Business Address'] = 'NA'
        
        try:
            badd = text.find('div',class_='map-box-address')
            badd1 = re.sub('  +', '', badd.text.strip())
            row1['Business Address'] = badd1.encode('utf-8') 
        except:
            row1['Business Address'] = 'NA'

        
                        
        
############ More Business Info #############        
        
        
        h3a = text.find_all('h3')
        for h3 in h3a:
            try:
                if h3.text.strip() == 'Hours':
                    h3h1 = h3.find_next_sibling('table')
                    ##print(h3h1)
                    h3h2 = h3h1.find_all('tr')
                    for h3h3 in h3h2:
                        row1['Opening Hours'] = (h3h3.find("th").text.strip() + ' - ' + h3h3.find("td").text.strip()).encode('utf-8') + ' \n '
            except:
                row1['Opening Hours'] = 'NA'
            if 'More business info' == h3.text:
                h3ul = h3.find_next_sibling("ul")
                h3dt = h3ul.find_all("dt")                
                
                for h3dta in h3dt:
                    
                    ## Check if Restaurant takes reservations
                    if h3dta.text.strip() == 'Takes Reservations':
                        row1['Takes Reservations'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')

                    ## Check for Delivery
                    if h3dta.text.strip() == 'Delivery':
                        row1['Delivery'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
                        
                    ## Check for Take-out
                    if h3dta.text.strip() == 'Take-out' :
                        row1['Take-out'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')

                    ## Check for Credit Card Acceptance
                    if 'Accepts Credit Cards' == h3dta.text.strip():
                        row1['Aceepts-Credit-Cards'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')

                    ## Check for Apple Pay Acceptance
                    if 'Accepts Apple Pay' == h3dta.text.strip():
                        row1['Accepts-Apple-Pay'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')

                    ## Check for Android Pay Acceptance
                    if 'Accepts Android Pay' == h3dta.text.strip():
                        row1['Accepts-Android-Pay'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')                   

                    ## Check for Bitcoin Acceptance
                    if 'Accepts Bitcoin' == h3dta.text.strip():
                        row1['Accepts-Bitcoin'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')                
                        
                    ## Check for Whats the restaurant is good for?
                    if 'Good For' == h3dta.text.strip():
                        row1['Good-For'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')     
                        
                    ## Check if Parking is available
                    if 'Parking' == h3dta.text.strip():
                        row1['Parking'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')    
                        
                    ## Check if Parking is available
                    if 'Bike Parking' == h3dta.text.strip():
                        row1['Bike-Parking'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')                    
                                                
                    ## Check if Restaurant is good for kids
                    if 'Good for Kids' == h3dta.text.strip():
                        row1['Good-For-Kids'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')

                    ## Check if Restaurant is good for kids
                    if 'Good for Groups' == h3dta.text.strip():
                        row1['Good-For-Groups'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
                        
                    ## Check if Restaurant's Attire
                    if 'Attire' == h3dta.text.strip():
                        row1['Attire'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
                        
                    ## Check if Restaurant's Ambience
                    if 'Ambience' == h3dta.text.strip():
                        row1['Ambience'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
                        
                    ## Check if Restaurant's Noise Level
                    if 'Noise Level' == h3dta.text.strip():
                        row1['Noise-Level'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')

                    ## Check if Restaurant's Alcohol Availability
                    if 'Alcohol' == h3dta.text.strip():
                        row1['Alcohol'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
                   
                    ## Check if Restaurant has Outdoor Seating
                    if 'Outdoor Seating' == h3dta.text.strip():
                        row1['Outdoor-Seating'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')

                    ## Check if Restaurant has Wi-Fi
                    if 'Wi-Fi' == h3dta.text.strip():
                        row1['Wi-Fi'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                    ## Check if Restaurant Caters
                    if 'Caters' == h3dta.text.strip():
                        row1['Caters'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
                        
                    ## Check if Restaurant has Gender Neutral Restrooms
                    if 'Gender Neutral Restrooms' == h3dta.text.strip():
                        row1['Gender-Neutral-Restrooms'] = h3dta.find_next_sibling("dd").text.strip().encode('utf-8')
    json.dump(row1,output_file)

    writer_csv.writerow(row1)
    
############ End of More Business Info ##############

row1 = {}
row1['Business Name'] = 'NA'
row1['Business Phone'] = 'NA'
row1['Business Website'] = 'NA'
row1['Business Address'] = 'NA'
row1['Business Name'] = 'NA'
row1['Opening Hours'] = 'NA'
row1['Takes Reservations'] = 'NA'
row1['Delivery'] = 'NA' 
row1['Take-out'] = 'NA' 
row1['Aceepts-Credit-Cards'] = 'NA'
row1['Accepts-Apple-Pay'] = 'NA' 
row1['Accepts-Android-Pay'] = 'NA' 
row1['Accepts-Bitcoin'] = 'NA' 
row1['Good-For'] = 'NA' 
row1['Parking'] = 'NA' 
row1['Bike-Parking'] = 'NA'
row1['Good-For-Kids'] = 'NA' 
row1['Good-For-Groups'] = 'NA'
row1['Attire'] = 'NA' 
row1['Ambience'] = 'NA'
row1['Noise-Level'] = 'NA' 
row1['Alcohol'] = 'NA'
row1['Outdoor-Seating'] = 'NA' 
row1['Wi-Fi'] = 'NA' 
row1['Caters'] = 'NA' 
row1['Gender-Neutral-Restrooms'] = 'NA' 

output_file = open("C:/Users/satish.vengla/iCloudDrive/ISB/Term1/test_output14.json","w")
output_file_csv = open("C:/Users/satish.vengla/iCloudDrive/ISB/Term1/test_output14.csv","wb")

print([row1.keys()])
writer_csv = csv.DictWriter(output_file_csv,fieldnames=row1.keys())
writer_csv.writeheader()
clean_dir("C:/Users/satish.vengla/iCloudDrive/ISB/Term1/DC1/assignmentData/")

output_file.close()
output_file_csv.close()

print("Done")