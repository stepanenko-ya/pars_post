import requests
import cfscrape
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()


url = 'https://www.iparts.pl/'


ip = "45.76.236.83:3128"
file_csv = open("poland.csv", "r")

for line in file_csv.readlines():
    lst_elements = line.strip().split("|")
    finders_el = ' '.join(lst_elements[1:3])
    finders = finders_el.replace(" ", "+")
    url_find = 'znajdz/?idCar=&query='
    item_url = f"{url}{url_find}{finders}"
    head_iparts = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   'Cookie': 'widok=lista; customerid=7e816edaa3faec1a67cb63a0b2c0bce9; _gcl_au=1.1.356962340.1622115574; _ga=GA1.2.1555252983.1622115575; _gid=GA1.2.1989884371.1622115575; _fbp=fb.1.1622115575993.1515875615; cto_bundle=Ap553V9GTkFPYWp3UEtLdzZSbjhjSFVJZzhSV2Y1VnFIVjdYa3NaMDZSVUY4eHpOZyUyRjN0MFBIaHY1VFBwenZsVzdoVmExbiUyQlVDb094NVUzJTJGZ1p3JTJCcG5JRXYlMkJveng3b0NnOWtQZkZ4T05BJTJCajd1ZGtNaGw1TkdyaTl4Tm1DbTFFck5vV2htcm1wdG9YeE5ud0pNS1V4OHFIZWclM0QlM0Q; analytic_id=1622115577813484; CMS=mh0oq80khgq56kk1hjnbun2l33; _gat_UA-9320418-1=1',
                   'Host': 'www.iparts.pl',
                   'TE': 'Trailers',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': ua.random}

    prox = {"http": "http://" + ip, "https": "http://" + ip}

    req = requests.get(item_url, headers=head_iparts, proxies=prox)


    #
    # soup = BeautifulSoup(req.content, "html.parser")
    # res = soup.find(class_="produkt middle-12")
    # link_half = res.find("a").get("href")
    # finish_url = url + link_half
    # file_result = open("iparts.csv", "a+")
    # file_result.write(f'{finders_el}|{finish_url}')
    #
