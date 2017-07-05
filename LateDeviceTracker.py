from bs4 import BeautifulSoup
import requests
import


r =  requests.get("https://www.repairwatch.com/admin/ops-shipping-outbound.php")

c = r.content

soup = BeautifulSoup(c, 'html.parser')
print(soup.find_all("a"))
# soup = BeautifulSoup(r)
# print(soup.prettify())







