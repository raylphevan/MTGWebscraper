import requests
from bs4 import BeautifulSoup
from csv import writer

def get_page(url):
  response = requests.get(url)

  if not response.ok:
    print('Server response: ', response.status_code)
  else:
    soup = BeautifulSoup(response.text, 'html.parser')
  return soup



def get_listing_name(soup):
  # List is needed to separate the actual listing name with the span tag
  # Should be okay because there needs to be a listing name

  contents = []
  for item in soup.find('h1', id='itemTitle'):
    contents.append(item)
  
  print(contents[1])
  return contents[1]



def get_price(soup):
  try:
    price = soup.find('span', id='prcIsum').get_text()
  except:
    price = ''

  print(price)
  return price



def get_condition(soup):
  try: 
    condition = soup.find('div', id='vi-itm-cond').get_text()
  except:
    condition = ''

  print(condition)
  return condition



def get_satisfaction(soup):
  try:
    satisfaction = soup.find('span', class_="w2b-sgl").get_text()
  except:
    satisfaction = ''
  
  print(satisfaction)
  return satisfaction



def get_total_sold(soup):
  try:
    total = soup.find('div', class_="w2b-cnt w2b-3 w2b-brdr").find('span', class_="w2b-sgl").get_text()
  except:
    total = ''

  print(total)
  return total



def get_listing_url(soup):
  return 0



def pack_info(soup):
  data = {
    'name': get_listing_name(soup),
    'price': get_price(soup),
    'condition': get_condition(soup),
    'satisfaction': get_satisfaction(soup),
    'total sold': get_total_sold(soup)
  }
  return data



def main():
  url = 'https://www.ebay.com/itm/Magic-The-Gathering-Zendikar-Rising-Set-Booster-Box-IN-STOCK-FREE-PRIORITY-SHIP/363143481926?hash=item548d09ca46:g:ZPEAAOSwzV5fiaUa'
  print(pack_info(get_page(url)))

if __name__ == "__main__":
  main()