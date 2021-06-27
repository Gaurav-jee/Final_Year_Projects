# 1. use the Website API
# 2. Use HTML Web Scraping using BS4 
# pip install requests
# pip install html5lib
# pip install bs4    (Beautiful Soap 4) 
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

#step 1: get the HTML
# r is content from the html.
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup)
#print(soup.prettify)
#
#step 3: HTML Tree Traversal
#
#Commonly Used types of objects:
#1. print(type(title)) Tag
#2. print(type(title.string)) NavigableString
#3. print(type(soup)) BeautifulSoup
#4. Comment
#
#get the title of the html page
title = soup.title


# Get all the the paragraphs from the page
#paras =  soup.find_all('p')
#print(paras)


# Get all the anchor tags from the page
anchor =  soup.find_all('a')
#print(anchor)


 #Get the first element in the html page
print(soup.find('p'))    
# #Get classes of any element in the html page
print(soup.find('p')['class'])
# #Get id of any element in the html page
#print(soup.find('p')['id'])

# find if the elements with class lead. 
print(soup.find_all("p", class_ = "lead"))

#get the text from html/soup
#print(soup.find('p').get_text())
print(soup.get_text())

all_links = set()
#Get all the links on the page:
for link in anchor:
    if(link != '#'):
        links = "https://codewithharry.com" + link.get('href')
        all_links.add(links)
        #print(links)

print(all_links)

markup = "<p><!--this is a comment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))
print(soup2.p.string)


navbarSupportedContent = soup.find(id = "navbarSupportedContent")
#print(navbarSupportedContent)
#print(navbarSupportedContent.contents)

# .contents - tag's children are available as a list 
# .children - tag's children are available as a generator  

#for elem in navbarSupportedContent.children:
#    print(elem)

#for item in navbarSupportedContent.strings:
#    print(item)

#for item in navbarSupportedContent.stripped_strings:
#    print(item)

#for item in navbarSupportedContent.parents:
#    print(item.name)

#print(navbarSupportedContent.previous_sibling.previous_sibling)
#print(navbarSupportedContent.next_sibling.next_sibling)

#elem = soup.select('#loginModal')
#print(elem)

#elem = soup.select('.loginModal')
#print(elem)

elem = soup.select('.Modal-footer')
print(elem)