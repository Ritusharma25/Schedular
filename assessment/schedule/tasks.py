# tasks.py

import requests
from bs4 import BeautifulSoup
from .models import Proxy
from celery import shared_task

@shared_task
def scrape_proxies():
    url = 'https://geonode.com/free-proxy-list'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxies = soup.find_all('tr')

    for proxy in proxies:
        data = proxy.find_all('th')
        if len(data) == 12:
            ip = data[0].text.strip()
            port = int(data[1].text.strip())
            country = data[2].text.strip()
            protocol = data[3].text.strip()
            uptime = data[7].text.strip()

            # Saving the scraped data into the database
            Proxy.objects.create(ip=ip, port=port, protocol=protocol, country=country, uptime=uptime)
