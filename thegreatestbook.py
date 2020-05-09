import requests
from bs4 import BeautifulSoup as bs

URL = 'https://thegreatesbooks.org'
hitung = 0
# for page in range(1,5):
req = requests.get(URL)
soup = bs(req.text, 'html.parser')
area = soup.findAll('item pb-3 pt-3 border-bottom')
for x in range(1,5):
    hitung +=1
    judul = x.find('h4', 'a').text
    print(hitung, judul)





    # containter = soup.find('div', attrs={'class' 'container'})
    # books = containter.find_all('h4')
    # for b in books:
    #     links = b.find_all('a')
    #     title= links[0].text
    #     author = ''
    #     try :
    #         author = links[1].text
    #     except:
    #         pass
    #     print('title: %s \n author:%s' % (title, author))