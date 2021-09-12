import requests
import csv 
import io
from bs4 import BeautifulSoup as bs
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r = requests.get('https://finance.yahoo.com/quote/BTC-EUR/history', headers=headers)
soup=bs(r.content, "html.parser")
filename='test.csv'
csv_writer=csv.writer(open(filename,'w'))
def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)

list_of_indeces=[1,2,3,5,6]
for tr in soup.find_all("tr"):
    data = []
    table=[]
    aux=[]
    i=0
    j=0
    for th in tr.find_all('th'):
        data.append(th.text)  
    if data:
        delete_multiple_element(data, list_of_indeces)
        print("Inserting headers: {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue
    
    for td in tr.find_all('td'):
       table.append(td.text.strip())
    
    if table:
        delete_multiple_element(table, list_of_indeces)
        print ("Inserting Table Data: {}".format(','.join(table)))
        csv_writer.writerow(table)
        continue
    
