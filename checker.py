from tranco import Tranco
import dns.resolver  
import csv
import os
os.system('clear')
from datetime import datetime, timedelta
yesterday=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
#get top1m domains
t = Tranco(cache=True, cache_dir='.tranco')
latest_list = t.list()
date_list = t.list(date=yesterday)
list_1k=latest_list.top(1000)
def get_spf(domain):
  answers = dns.resolver.resolve(domain, 'TXT')
  for answer in answers:
    if "spf" in answer.to_text():     
      return answer.to_text()
    else:
      return "No SPF"
header  = ['domain', 'SPF']
for host  in list_1k:
  try:
    with open('result.csv', 'a', encoding='UTF8') as f:
     writer = csv.writer(f)
     writer.writerow([host,get_spf(host)])
  except Exception as e:
    print(e.__doc__)



