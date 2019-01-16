from bs4 import BeautifulSoup
import os
import re
import json
import csv
import validators


def clean_dir(directory):

    os.chdir(directory)

    for filename in os.listdir(directory):
        clean_file(filename)

def clean_file(filename):
    global links, emailc
    
    with open(filename, 'r') as fhandle:

        response = BeautifulSoup(fhandle,'html.parser')
        row2 = {}
        contactus = list()
        #row2['contact us'] = list()
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        new_emails = list(set(new_emails))

        soclinks = ''
        emailsl = ''
        for emailc in new_emails:
            emailsl = emailc + '\n' + emailsl
      
        row2['hotel-link'] = filename.replace('http://','').replace('www.','').replace('.html','')
   

        for link in response.find_all("a"):
            link1=''
            try:
                link1 = link.get('href').lower()
            except:
                   pass                     
            if ('contact' in link.text.strip().lower()) or ('info' in link.text.strip().lower()):
                if '.' in link1:
                    contactus.extend([link1.encode('utf-8')])
                else:
                    contactus.extend([row2['hotel-link'] + '/' + link1.encode('utf-8')])
            elif ('contact' in link1) or ('info' in link1):
                if '.' in link1:
                    contactus.extend([link1.encode('utf-8')])
                else:
                    contactus.extend([row2['hotel-link'] + '/' +link1.encode('utf-8')])
            else:
                if ('facebook.com' in link1) or ('twitter.com' in link1) or ('instagram.com' in link1) or ('t.co' in link1):
                    soclinks = link1 + '\n' + soclinks
                #print link.text.strip().lower()
                #print link.get('href')
        
        contsl=''
        
        contactus = list(set(contactus))
        for conts in contactus:
            conts = conts.replace('http://','')
            conts = conts.replace('https://','')
            conts = conts.replace('//','/')
            conts = conts.replace('/#','/')
            #print(conts) 
            #print(validators.url(conts))
            if 'mailto' not in conts:
                if validators.url('http' + conts) <> True:
                    conts = (row2['hotel-link'] + '/' + conts).replace('//','')
                contsl = conts + '\n' + contsl
            else:
                emailsl = emailsl + '\n' + conts.replace('mailto','').replace(':','').replace('//','')                

        if len(contactus) == 0:
            contsl = soclinks
                        
        row2['contact us'] = contsl
        row2['emails']  = emailsl

        json.dump(row2,output_file)
        writer_csv.writerow(row2)


links = 0
emailc = 0
row2 = {}
row2['hotel-link'] = ''
row2['contact us'] = ''
row2['emails'] = ''

output_file = open("C:/Users/satish.vengla/iCloudDrive/ISB/Term1/test_mail_link5.json","w")
output_file_csv = open("C:/Users/satish.vengla/iCloudDrive/ISB/Term1/test_mail_link5.csv","wb")

writer_csv = csv.DictWriter(output_file_csv,fieldnames=row2.keys())
writer_csv.writeheader()

clean_dir("C:/Users/satish.vengla/iCloudDrive/ISB/Term1/DC1/GA1/test")
output_file.close()
output_file_csv.close()
print('Done')