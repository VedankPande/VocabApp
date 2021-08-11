from bs4 import BeautifulSoup
import pandas as pd
import requests

#driver = webdriver.Chrome(executable_path='C:/Users/vedan/Desktop/chromedriver.exe')


meaning_list = []

meaning_class = "O5uR6d LTKOO"
word_class = "c8d6zd"
sentence_class = "ubHt5c"
query = "pandemonium+meaning"
#root = f'https://www.google.com/search?q={query}'


#driver.get(root)
lst = []
for i in range(1,6):
    root = f"https://www.graduateshotline.com/gre/load.php?file=list{i}.html"
    db = pd.DataFrame()
    content = requests.get(root).text
    soup = BeautifulSoup(content,'html.parser')
    table = soup.find_all('table',attrs={'class':'tablex border1'})[0]


    for row in table.find_all("tr"):
        tds = row.find_all("td")
        print([tds[0].text,tds[1].text])
        lst.append([tds[0].text,tds[1].text])

df = pd.DataFrame(lst,columns=['word','meaning'])
df.to_csv('word_db.csv',index=False)
print(df.head())
print(df.info())



