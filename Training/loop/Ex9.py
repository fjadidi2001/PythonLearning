  import requests
  url = 'http://github.com'
  r = requests.get(url)
  r_html = r.text
  from bs4 import BeautifulSoup

  # some requests code here for getting r_html 

  soup = BeautifulSoup(r_html)
  title = soup.find('span', 'articletitle').string
k
