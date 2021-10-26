from tranco import Tranco
import dns.resolver  
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
for host  in list_1k:
  try:
    print(host+','+get_spf(host))
  except Exception as e:
    print(e)


# my_resolver = dns.resolver.Resolver()

# for domain  in one_m_list:
#   try:
#     answer_txt = my_resolver.resolve(domain, "TXT")
#     for TXT in answer_txt.rrset:
#       if "spf" in str(TXT):
#         result=domain+','+str(TXT).strip("\"")+'\n'
#         with open ("out4.txt" , "a") as out_put:
#           out_put.write(result)
#           out_put.close()
#       break    
#   except Exception as e:
#     print(domain + ' ' +str(e))