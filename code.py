import requests
from pyquery import PyQuery as pq

resultNTD = 0
print("Sample Input: yyyy/mm/dd USD 1000 | Stop by [Enter]")

while 1:
    try:
        date,currency,money = map(str,input().split(' '))
        params = {"all_year":date[0:4], "all_month":date[5:7],"all_day":date[8:10]}
        res = requests.post(url="https://rate.bot.com.tw/xrt/all/{}-{}-{}".format(date[0:4],date[5:7],date[8:10]),data=params)
        doc = pq(res.text)
        for info in doc("tbody tr:nth-child(n)").items():
            if (info("td:nth-child(1).currency.phone-small-font > div > div.hidden-phone.print_show").text()[-4:-1]) == currency:
                resultNTD += int(money)*float(info("td:nth-child(5)").text())
    except ValueError:
        break
        
print('Total Equal to ${} NTD.'.format(round(resultNTD)))
