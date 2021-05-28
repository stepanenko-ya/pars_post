# head_2407 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#      'Accept-Encoding': 'gzip, deflate, br',
#      'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#      'Cache-Control': 'max-age=0',
#      'Connection': 'keep-alive',
#      'Cookie': '__cf_bm=0a505d97a4613681aac74898811cecbf05d9ff10-1622113884-1800-AQRNzt0Yp9hKDrI/JY1F6tbNN1UoFOIlg6UP5+zHpYI3rDfIqeFeSjectipKAcKfuyN8Lj9p2k2QEH0x4Ex10OzAxSKAlFmqkLeM8lWgxN6H7N0vL84KTRH3Q8h3tMiPjA==; _ga=GA1.2.1497699223.1622113886; _gid=GA1.2.703650004.1622113886; _gat=1; _gat_UA-155313880-2=1; supportOnlineTalkID=LwWPd0kgt2O4GtRkzVns2H4RGMEdW8Q2',
#      'Host': '2407.pl',
#      'TE': 'Trailers',
#      'Upgrade-Insecure-Requests': '1',
#      'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

import requests
import cfscrape
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
ip = '178.62.127.204:8080'
prox = {"http": "http://" + ip, "https": "http://" + ip}
head_iparts = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Cookie': 'widok=lista; customerid=7e816edaa3faec1a67cb63a0b2c0bce9; _gcl_au=1.1.356962340.1622115574; _ga=GA1.2.1555252983.1622115575; _gid=GA1.2.1989884371.1622115575; _fbp=fb.1.1622115575993.1515875615; cto_bundle=Ap553V9GTkFPYWp3UEtLdzZSbjhjSFVJZzhSV2Y1VnFIVjdYa3NaMDZSVUY4eHpOZyUyRjN0MFBIaHY1VFBwenZsVzdoVmExbiUyQlVDb094NVUzJTJGZ1p3JTJCcG5JRXYlMkJveng3b0NnOWtQZkZ4T05BJTJCajd1ZGtNaGw1TkdyaTl4Tm1DbTFFck5vV2htcm1wdG9YeE5ud0pNS1V4OHFIZWclM0QlM0Q; analytic_id=1622115577813484; CMS=mh0oq80khgq56kk1hjnbun2l33; _gat_UA-9320418-1=1',
               'Host': 'www.iparts.pl',
               'TE': 'Trailers',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

# req = requests.get("https://www.iparts.pl/znajdz/?idCar=&query=YT-8152+Yato", headers=head_iparts, proxies=prox)
# print(req.content)
d =b'\xa3\xfa\x86\xc0\x88\xe4\xa4\xd5\x03\xa0\x11'
print(convert_to_unicode(d))