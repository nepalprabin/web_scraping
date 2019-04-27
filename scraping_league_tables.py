from bs4 import BeautifulSoup
import urllib.request
import csv
# specify the url
urlpage =  'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
print(soup)


#Searching for html elements
#Searching results within table as the results are displayed in table(inspect the webpage for this)
table=soup.find('table',attrs={'class':'tableSorter'})
results=table.find_all('tr')
print('Number of results',len(results))

# create and write headers to a list 
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])
print(rows)
#to loop over results
for result in results:
	data=result.find_all('td')
	#checking if column has any data
	if len(data)==0:
		continue
	
data

 # write columns to variables
rank = data[0].getText()
company = data[1].getText()
location = data[2].getText()
yearend = data[3].getText()
salesrise = data[4].getText()
sales = data[5].getText()
staff = data[6].getText()
comments = data[7].getText()

#The above simply gets the text from each of the columns and saves to the variables. Some data needs cleaning
#extract description from name
print('Company is', company)
print('Sales', sales)

#extracting description from name
companyname=data[1].find('span',attrs={'class':'company-name'}).get_Text()
description=company.replace(companyname,'')

#remove unwanted characters
sales=sales.strip('*').strip('†').replace(',','')

#URL of the company website
url=data[1].find('a').get('href')
page1=urllib.request.urlopen(url)

#parse the html 
soup1=BeautifulSoup(page1,'html.parser')
#finding the last result in the tab;e and getting the link
try:
	tableRow=soup.find('table').find_all('tr')[-1]
	webpage=tableRow.find('a').get('href')
except:
	webpage=None
#write each result to rows
rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])
print(rows)

#creating csv file and write rows to output file
with open('techrank100.csv','w',newline='') as f_output:
	csv_output=(csv.writer(f_output))
	csv_output.writerows(rows) 
	