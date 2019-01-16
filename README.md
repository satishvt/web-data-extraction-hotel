(1) Program Names and Information
------------------------------------

extract-business-info-and-services.py (Extract the basic business information & services provided from the 1000 html pages provided)

download-home-pages.py (Downloads the home pages of all the restaurants which have a valid website, website URL retrieved from the 1000 pages)

extract-contact-us-email.py (Extracts the contact-us and email id information)


		
####################################################################	
			
(2) Logic for email ID and Contact Us 
------------------------------------


Logic used for email ID extraction:

Logic#1 - from the HTML page, find all the text which matches the regex of the email "[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+". 
Logic#2 - In some places in the html code, mailto: or mailto:// is used. Email ID has been extracted basis the same


Logic used for contact-us extraction:

Logic#1: Extracted all the anchor tags from the html text and if the word 'contact' or 'info' is present in the text of the anchor tag OR the href link (URL). Then extract the URL (or sub-domain) from the link. Basis this build the full URL

Logic#2: If the contact or info pages are not present, then extract any links of social media like Facebook, Twitter or Instagram of the restaurants

Note: 
(a) Used a URL validator package to validate if the URL is proper
(b) Sometimes in the HTML code, full URL is not provided for contact, only sub-domain is provided. Using the sub-domain, full URL was built in the code


####################################################################

(3) Overall Logic Used
------------------------------------


Step 1: Parse thru all the 1000 web pages (downloaded and provided to us) & extract all the business information and the services. (extract-business-info-and-services.py

Step 2: Get the website name for all the restaurants (available), from the Step1 & download them 'Scrapy'. (download-home-pages.py)

Step 3: Parse the downloaded home pages and retrieve the Contact Us and Email ID information. (extract-contact-us-email.py )
