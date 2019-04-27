import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url='http://www.hubertiming.com/results/2017GPTR10K'
html=urlopen(url)
soup=BeautifulSoup(html,'lxml')
text=soup.get_text()
print(soup.text)

title=soup.title
print(title)

table_rows=soup.find_all('tr')
print(table_rows)
print(soup.find_all('a'))

all_links=soup.find_all('a')
for link in all_links:
	print(link.get('href'))

rows=soup.find_all('tr')
print(rows[:10])

for row in rows:
	row_td=row.find_all('td')
print(row_td)

str_cells=str(row_td)
cleantext=BeautifulSoup(str_cells,'lxml').get_text()
print(cleantext)

import re
list_rows=[]
for row in rows:
	cells=row.find_all('td')
	str_cells=str(cells)
	clean=re.compile('<.*?>')
	clean2=(re.sub(clean,'',str_cells))
	list_rows.append(clean2)
print(clean2)

df=pd.DataFrame(list_rows)
df.head()


df1=df[0].str.split(',',expand=True)
df1.head()

df1[0]=df1[0].str.strip('[')
df1.head()

col_header=soup.find_all('th')
all_header=[]
col_str=str(col_header)
cleantext2=BeautifulSoup(col_str,'lxml').get_text()
all_header.append(cleantext2)


df2=pd.DataFrame(all_header)

df3=df2[0].str.split(',',expand=True)

frames=[df3,df1]
df4=pd.concat(frames)

df5=df4.rename(columns=df4.iloc[0])
df6=df5.dropna(axis=0,how='any')

df7=df6.drop(df6.index[0])
df7.rename(columns={'[Place':'Place'},inplace=True)
df7.rename(columns={' Team]':'Team'},inplace=True)
df7['Team']=df7['Team'].str.strip(']')















