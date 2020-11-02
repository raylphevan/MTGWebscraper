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
  for item in soup.find('h1', id="itemTitle"):
    contents.append(item)
  
  return contents[1]



def get_price(soup):
  try:
    price = soup.find('span', id="prcIsum").get_text()
  except:
    try:
      price = soup.find('span', id="prcIsum_bidPrice").get_text()
    except:
      price = ''

  return price



def get_condition(soup):
  try: 
    condition = soup.find('div', id="vi-itm-cond").get_text()
  except:
    condition = ''

  return condition



def get_total_sold(soup):
  try:
    total = soup.find('span', class_="vi-qtyS-hot-red").find('a').text.strip().split(' ')[0]
  except:
    total = ''

  return total



def get_seller_feedback(soup):
  try:
    feedback = soup.find('div', id="si-fb").get_text()
    feedback = feedback.replace('\xa0', ' ')
  except:
    feedback = ''
  
  return feedback



def get_feeback_score(soup):
  try:
    score = soup.find('span', class_="mbg-l").find('a').get_text()
  except:
    score = ''

  return score



def get_urls(soup):
  try:
    links = soup.find_all('a', class_="s-item__link")
  except:
    links = []

  urls = [item.get('href') for item in links]

  return urls



def pack_info(soup):
  data = {
    'name': get_listing_name(soup),
    'price': get_price(soup),
    'condition': get_condition(soup),
    'total sold': get_total_sold(soup),
    'feedback': get_seller_feedback(soup),
    'feedback score': get_feeback_score(soup)
  }

  return data



def write_csv(data, url):
  with open('output.csv', 'a') as csvfile:
    w = writer(csvfile)

    row = [data['name'], data['price'], data['condition'], data['total sold'], data['feedback'], data['feedback score'], url]
    w.writerow(row)



def main():
  url = 'https://www.ebay.com/sch/i.html?_nkw=magic+the+gathering+zendikar+rising+booster+box&_pgn=1'

  products = get_urls(get_page(url))

  for link in products:
    data = pack_info(get_page(link))
    write_csv(data, link)


if __name__ == "__main__":
  main()