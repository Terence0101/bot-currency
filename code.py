import requests
from pyquery import PyQuery as pq

date = input()

infoset = []
params = {"all_year":date[0:4], "all_month":date[5:7],"all_day":date[8:10]}
res = requests.post(url="https://rate.bot.com.tw/xrt/all/{}-{}-{}".format(date[0:4],date[5:7],date[8:10]),data=params)
doc = pq(res.text)

for info in doc("tbody tr:nth-child(n)").items():
    infodict = {}
    if (len(doc('tbody tr'))) > 1:
        infodict['Currency'] = info("td:nth-child(1).currency.phone-small-font > div > div.hidden-phone.print_show").text()[-4:-1]
        infodict['Rate'] = info("td:nth-child(5)").text()
        infoset.append(infodict)
        
    else:
        print("Today is Holiday.")
        
print(doc("#ie11andabove > div > p.text-info").text())
for i in infoset:
    data = [j for j in i.values()]
    print(" ".join(data))
