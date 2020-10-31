from bs4 import BeautifulSoup

html_doc = """
<html>
  <body>
    <p class='xd'>Hello</p>
    <p>Here we are</p>
  </body>
</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.body)
# print(soup.head)

# findP = soup.find('p')
# findP = soup.find_all('p')[1]
# findP = soup.find(class_='xd')

# select - used to find things thru css
# select always returns it as a list
# findP = soup.select('p')

# get_text()
# findP = soup.find(class_='xd').get_text()

# for item in soup.select('p'):
#   print(item.get_text())

# Navigation
# el = soup.body.contents[1].contents[0].find_next_sibling()

# el = soup.find(class_='xd').find_previous_sibling()

# el = soup.find(class_='xd').find_parent()

# el = soup.find('p').find_next_sibling('p')

# print(el)

# print(findP)